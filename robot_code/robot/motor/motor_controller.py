"""Contrôleur double moteur avec boucle de pas continue en arrière-plan."""

from __future__ import annotations

import threading
import time

from .motor_driver import TMC2225
from .motor_config import (
    DEFAULT_SPEED_RPM, DEFAULT_STEPS_PER_REV, DEFAULT_MICROSTEP,
    DIRECTION_FORWARD, DIRECTION_BACKWARD,
)

_STEP_HZ = 200  # fréquence interne du thread de pas


class DualMotorController:

    def __init__(self, motor1_params: dict, motor2_params: dict):
        self.motor1 = TMC2225(
            step_pin=motor1_params["step"],
            dir_pin=motor1_params["dir"],
            speed_rpm=motor1_params.get("speed_rpm", DEFAULT_SPEED_RPM),
            direction=motor1_params.get("direction", DIRECTION_FORWARD),
            steps_per_rev=motor1_params.get("steps_per_rev", DEFAULT_STEPS_PER_REV),
            microstep=motor1_params.get("microstep", DEFAULT_MICROSTEP),
        )
        self.motor2 = TMC2225(
            step_pin=motor2_params["step"],
            dir_pin=motor2_params["dir"],
            speed_rpm=motor2_params.get("speed_rpm", DEFAULT_SPEED_RPM),
            direction=motor2_params.get("direction", DIRECTION_BACKWARD),
            steps_per_rev=motor2_params.get("steps_per_rev", DEFAULT_STEPS_PER_REV),
            microstep=motor2_params.get("microstep", DEFAULT_MICROSTEP),
        )

        self._speed1: float = 0.0
        self._speed2: float = 0.0
        self._lock = threading.Lock()
        self._running = False
        self._thread: threading.Thread | None = None

    # ── API publique ───────────────────────────────────────────────────────────

    def set_speeds(self, speed1: float, speed2: float) -> None:
        """Met à jour les consignes de vitesse (non bloquant).

        speed1, speed2 : RPM signés. Positif = avant, négatif = arrière.
        """
        with self._lock:
            self._speed1 = speed1
            self._speed2 = speed2
            self._apply_speed(self.motor1, speed1)
            self._apply_speed(self.motor2, -speed2)   # moteur 2 monté en miroir

    def start_continuous(self) -> None:
        """Démarre le thread de pas en arrière-plan."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._step_loop, daemon=True)
        self._thread.start()

    def stop_all(self) -> None:
        """Arrête le thread et nettoie les GPIO."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
        self.motor1.cleanup()
        self.motor2.cleanup()

    def info(self) -> None:
        print("\n=== INFOS MOTEURS ===")
        self.motor1.info()
        self.motor2.info()
        print("=====================\n")

    # ── Boucle interne ─────────────────────────────────────────────────────────

    def _step_loop(self) -> None:
        interval = 1.0 / _STEP_HZ
        while self._running:
            start = time.monotonic()
            with self._lock:
                s1 = abs(self._speed1)
                s2 = abs(self._speed2)
            if s1 > 0:
                self.motor1.step(1)
            if s2 > 0:
                self.motor2.step(1)
            elapsed = time.monotonic() - start
            sleep = interval - elapsed
            if sleep > 0:
                time.sleep(sleep)

    # ── Helpers ────────────────────────────────────────────────────────────────

    @staticmethod
    def _apply_speed(motor: TMC2225, speed: float) -> None:
        if abs(speed) < 0.5:
            motor.set_speed(0.5)
            return
        motor.set_direction(DIRECTION_FORWARD if speed >= 0 else DIRECTION_BACKWARD)
        motor.set_speed(abs(speed))
