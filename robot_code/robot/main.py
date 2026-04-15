"""Robot Segway Suiveur de Ligne — point d'entrée principal.

Combine :
  - Équilibre  → IMU LSM6DSOX + filtre complémentaire + PID balance
  - Suivi de ligne → capteurs IR sur MCP3208 + PID direction
  - Commande moteurs → deux TMC2225 en pas à pas (thread continu)

Lancement :
    python3 main.py              # mode complet (équilibre + suivi ligne)
    python3 main.py --balance    # équilibre seul (sans suivi de ligne)
    python3 main.py --calibrate  # calibrer l'offset d'angle vertical

Architecture de la boucle (100 Hz) :
  ┌─────────────────────────────────────────────────────────┐
  │  1. BalanceController.update(dt)                        │
  │     → lit IMU, filtre complémentaire, PID balance       │
  │     → retourne speed_cmd (RPM base)                     │
  │                                                         │
  │  2. get_line_error(adc)                                 │
  │     → lit 8 capteurs IR via MCP3208 / SPI               │
  │     → retourne erreur normalisée [-1 … +1]              │
  │                                                         │
  │  3. PID ligne → steer_cmd (différentiel de vitesse)     │
  │                                                         │
  │  4. Fusion :                                            │
  │       motor_gauche  = speed_cmd + steer_cmd             │
  │       motor_droite  = speed_cmd − steer_cmd             │
  └─────────────────────────────────────────────────────────┘
"""

from __future__ import annotations

import argparse
import signal
import time
from importlib import import_module

# ── Mock GPIO pour test hors Raspberry Pi ──────────────────────────────────────
try:
    GPIO = import_module("RPi.GPIO")
except ModuleNotFoundError:
    class _MockGPIO:
        BOARD = "BOARD"

        @staticmethod
        def setmode(mode):
            return None

        @staticmethod
        def cleanup(channel=None):
            return None

    GPIO = _MockGPIO()
    print("[WARN] RPi.GPIO introuvable (hors Raspberry Pi) : mode simulation GPIO activé.")

# ── Imports projet ─────────────────────────────────────────────────────────────
from code_sl.MCP3208 import MCP3208
from code_sl.line_detector import get_line_error
from motor.motor_controller import DualMotorController
from motor.motor_config import (
    MOTOR1_STEP_PIN, MOTOR1_DIR_PIN, MOTOR1_DIRECTION,
    MOTOR2_STEP_PIN, MOTOR2_DIR_PIN, MOTOR2_DIRECTION,
    MAX_SPEED_RPM,
    BALANCE_KP, BALANCE_KI, BALANCE_KD, BALANCE_KG,
    LINE_KP, LINE_KI, LINE_KD,
    ALPHA, OUTPUT_BETA, IMU_AXIS, ANGLE_OFFSET, DEADBAND_DEG,
    LINE_THRESHOLD, SEARCH_SPEED_RPM, FALL_ANGLE,
)
from control.pid import PID
from control.balance_controller import BalanceController

# ── Configuration boucle ───────────────────────────────────────────────────────
LOOP_HZ      = 100      # fréquence cible de la boucle principale
DISPLAY_HZ   = 10       # fréquence d'affichage télémetrie console

# ── Arrêt propre ───────────────────────────────────────────────────────────────
_running = True


def _signal_handler(sig, frame):
    global _running
    print("\nArrêt demandé…")
    _running = False


signal.signal(signal.SIGINT,  _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)


# ══════════════════════════════════════════════════════════════════════════════
# Boucle principale
# ══════════════════════════════════════════════════════════════════════════════

def run(balance_only: bool = False) -> None:
    """Lance la boucle de contrôle complète (équilibre + suivi de ligne).

    Parameters
    ----------
    balance_only : si True, le suivi de ligne est désactivé.
    """
    global _running

    print(f"Initialisation — axe IMU : {IMU_AXIS}, offset : {ANGLE_OFFSET:.2f}°")
    GPIO.setmode(GPIO.BOARD)

    # ── Contrôleur d'équilibre ────────────────────────────────────────────────
    bc = BalanceController(
        kp=BALANCE_KP,
        ki=BALANCE_KI,
        kd=BALANCE_KD,
        kg=BALANCE_KG,
        max_speed=MAX_SPEED_RPM,
        angle_offset=ANGLE_OFFSET,
        alpha=ALPHA,
        output_beta=OUTPUT_BETA,
        axis=IMU_AXIS,
        deadband=DEADBAND_DEG,
    )

    # ── ADC pour les capteurs infrarouges ─────────────────────────────────────
    adc = MCP3208(vref=3.3) if not balance_only else None

    # ── PID suivi de ligne ────────────────────────────────────────────────────
    line_pid = PID(
        kp=LINE_KP,
        ki=LINE_KI,
        kd=LINE_KD,
        out_min=-MAX_SPEED_RPM / 2,
        out_max= MAX_SPEED_RPM / 2,
    )

    # ── Moteurs ───────────────────────────────────────────────────────────────
    motors = DualMotorController(
        motor1_params={
            "step": MOTOR1_STEP_PIN,
            "dir":  MOTOR1_DIR_PIN,
            "direction": MOTOR1_DIRECTION,
        },
        motor2_params={
            "step": MOTOR2_STEP_PIN,
            "dir":  MOTOR2_DIR_PIN,
            "direction": MOTOR2_DIRECTION,
        },
    )

    print("Démarrage — tenez le robot droit !")
    if balance_only:
        print("Mode : BALANCE SEULE (sans suivi de ligne)")

    dt_target        = 1.0 / LOOP_HZ
    display_interval = 1.0 / DISPLAY_HZ
    last_time        = time.monotonic()
    last_display     = time.monotonic()
    steer_cmd        = 0.0
    line_err: float | None = None
    loop_count       = 0

    try:
        motors.set_speeds(0, 0)
        motors.start_continuous()

        while _running:
            now = time.monotonic()
            dt  = now - last_time

            # Attend le prochain tick
            if dt < dt_target:
                time.sleep(dt_target - dt)
                continue

            last_time = now

            # ── 1. Équilibre ─────────────────────────────────────────────────
            speed_cmd = bc.update(dt)
            angle     = bc.angle

            # Arrêt d'urgence si le robot tombe
            if abs(angle) > FALL_ANGLE:
                print(f"\n⚠  Chute détectée (angle={angle:.1f}°) — arrêt d'urgence !")
                motors.set_speeds(0, 0)
                bc.reset()
                line_pid.reset()
                steer_cmd = 0.0
                time.sleep(1.5)      # pause avant de réessayer
                last_time = time.monotonic()
                continue

            # ── 2. Suivi de ligne ────────────────────────────────────────────
            if not balance_only and adc is not None:
                line_err, _ = get_line_error(adc, threshold=LINE_THRESHOLD)

                if line_err is not None:
                    # Ligne visible → correction PID
                    steer_cmd = line_pid.compute(error=line_err, dt=dt)
                else:
                    # Ligne perdue → rotation lente sur place pour chercher
                    steer_cmd = SEARCH_SPEED_RPM
                    line_pid.reset()

            # ── 3. Fusion équilibre + direction ──────────────────────────────
            #   speed_cmd  : vitesse base (avant/arrière) issue du PID balance
            #   steer_cmd  : différentiel (gauche/droite) issu du PID ligne
            speed_left  = speed_cmd + steer_cmd
            speed_right = speed_cmd - steer_cmd

            motors.set_speeds(speed_left, speed_right)

            # ── 4. Télémétrie console ─────────────────────────────────────────
            loop_count += 1
            if now - last_display >= display_interval:
                elapsed     = now - last_display
                actual_hz   = loop_count / elapsed if elapsed > 0 else 0.0
                loop_count  = 0
                last_display = now
                _print_telemetry(
                    angle=angle,
                    speed_cmd=speed_cmd,
                    steer_cmd=steer_cmd,
                    speed_left=speed_left,
                    speed_right=speed_right,
                    line_err=line_err,
                    actual_hz=actual_hz,
                    mode="BAL+LINE" if not balance_only else "BAL SEULE",
                    deadband=DEADBAND_DEG,
                )

    finally:
        motors.stop_all()
        bc.close()
        if adc is not None:
            adc.close()
        GPIO.cleanup()
        print("\nArrêt propre effectué.")


# ══════════════════════════════════════════════════════════════════════════════
# Calibration de l'offset d'angle
# ══════════════════════════════════════════════════════════════════════════════

def calibrate() -> None:
    """Mesure l'offset vertical de l'IMU et affiche la valeur à saisir dans motor_config.py."""
    print("Calibration — posez le robot parfaitement droit sur une surface plane.")
    print("Appuyez sur Entrée quand il est immobile…")
    input()

    bc = BalanceController(
        angle_offset=0.0,
        axis=IMU_AXIS,
        alpha=ALPHA,
        output_beta=0.0,
    )

    print("Mesure en cours (2 secondes)…")
    samples = 100
    total   = 0.0
    last_t  = time.monotonic()

    for _ in range(samples):
        now = time.monotonic()
        bc.update(now - last_t)
        last_t = now
        total += bc.angle
        time.sleep(0.02)

    bc.close()
    offset = total / samples
    print(f"\nOffset mesuré : {offset:.3f}°")
    print(f"→ Dans motor/motor_config.py, mettez :  ANGLE_OFFSET = {offset:.3f}")


# ══════════════════════════════════════════════════════════════════════════════
# Télémétrie
# ══════════════════════════════════════════════════════════════════════════════

def _print_telemetry(
    angle: float,
    speed_cmd: float,
    steer_cmd: float,
    speed_left: float,
    speed_right: float,
    line_err: float | None,
    actual_hz: float,
    mode: str,
    deadband: float,
) -> None:
    db_flag = "*" if abs(angle) < deadband else " "
    err_str = f"{line_err:+.2f}" if line_err is not None else "  ––  "
    print(
        f"\r[{mode}] "
        f"Ang={angle:+6.2f}°{db_flag} │ "
        f"Base={speed_cmd:+5.1f} │ "
        f"Steer={steer_cmd:+5.1f} │ "
        f"G={speed_left:+5.1f} D={speed_right:+5.1f} │ "
        f"Ligne={err_str} │ "
        f"Hz={actual_hz:.0f}   ",
        end="",
        flush=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# Point d'entrée
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Robot Segway suiveur de ligne — contrôleur principal"
    )
    parser.add_argument(
        "--balance",
        action="store_true",
        help="Mode équilibre seul (suivi de ligne désactivé)",
    )
    parser.add_argument(
        "--calibrate",
        action="store_true",
        help="Calibrer l'offset vertical de l'IMU",
    )
    args = parser.parse_args()

    if args.calibrate:
        calibrate()
    else:
        run(balance_only=args.balance)


if __name__ == "__main__":
    main()
