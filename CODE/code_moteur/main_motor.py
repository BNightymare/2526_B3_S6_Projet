"""Test unitaire des moteurs TMC2225.

Lance :
    python3 main_motor.py
"""

from __future__ import annotations

import time
from importlib import import_module

try:
    GPIO = import_module("RPi.GPIO")
except ModuleNotFoundError:
    class _MockGPIO:
        BOARD = "BOARD"
        @staticmethod
        def setmode(mode): return None
        @staticmethod
        def cleanup(channel=None): return None
    GPIO = _MockGPIO()
    print("[WARN] RPi.GPIO introuvable : mode simulation activé.")

from motor.motor_controller import DualMotorController
from motor.motor_config import (
    MOTOR1_STEP_PIN, MOTOR1_DIR_PIN, MOTOR1_DIRECTION,
    MOTOR2_STEP_PIN, MOTOR2_DIR_PIN, MOTOR2_DIRECTION,
)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)

    motors = DualMotorController(
        motor1_params={"step": MOTOR1_STEP_PIN, "dir": MOTOR1_DIR_PIN, "direction": MOTOR1_DIRECTION},
        motor2_params={"step": MOTOR2_STEP_PIN, "dir": MOTOR2_DIR_PIN, "direction": MOTOR2_DIRECTION},
    )
    motors.info()

    try:
        print("Test : avance 3s...")
        motors.set_speeds(10, 10)
        motors.start_continuous()
        time.sleep(3)

        print("Test : virage gauche 2s...")
        motors.set_speeds(5, 10)
        time.sleep(2)

        print("Test : virage droite 2s...")
        motors.set_speeds(10, 5)
        time.sleep(2)

        print("Test : marche arrière 2s...")
        motors.set_speeds(-10, -10)
        time.sleep(2)

        print("Arrêt.")
    except KeyboardInterrupt:
        print("\nInterrompu.")
    finally:
        motors.stop_all()
        GPIO.cleanup()
