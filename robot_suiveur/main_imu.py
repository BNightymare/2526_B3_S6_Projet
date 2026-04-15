"""
Robot suiveur - Équilibrage PID Complet
"""

from __future__ import annotations
import time
import sys
import os
import math

# --- IMPORTS SYSTÈME ET IMU (TRÈS IMPORTANT) ---
# Ajout du dossier 'imu' au chemin pour pouvoir importer drv_lsm6dsow et setting tels quels
sys.path.append(os.path.join(os.path.dirname(__file__), "imu"))

try:
    from drv_lsm6dsow import *
    from setting import *
except ImportError as e:
    print(f"Erreur d'import IMU : {e}")
    sys.exit(1)

# Import des modules moteurs
from motor.controller import DualMotorController
from motor.config import (
    MOTOR1_STEP_PIN, MOTOR1_DIR_PIN, MOTOR1_DIRECTION,
    MOTOR2_STEP_PIN, MOTOR2_DIR_PIN, MOTOR2_DIRECTION,
)

# --- RÉGLAGES PID BOOSTÉS POUR L'ÉQUILIBRE ---
KP = 15.0              # Réaction immédiate (Proportionnel)
KI = 0.8               # Correction de l'inclinaison résiduelle (Intégral)
KD = 1.2               # Amortissement des secousses (Dérivé)

TARGET_ANGLE = -90.0   # Verticale parfaite
DEADBAND = 0.5         # Zone morte réduite pour plus de précision
ALPHA = 0.98           # Filtre complémentaire
LOOP_DELAY = 0.01      # 100Hz
MAX_SPEED = 180.0      # Vitesse max augmentée pour rattraper les chutes rapides

def main() -> None:
    print("Initialisation de l'IMU...")
    try:
        driver = drv_lsm6dsow(bus=1)
    except Exception as e:
        print(f"Erreur IMU : {e}")
        return

    # Initialisation des moteurs
    motors = DualMotorController(
        motor1_params={"step": MOTOR1_STEP_PIN, "dir": MOTOR1_DIR_PIN, "direction": MOTOR1_DIRECTION},
        motor2_params={"step": MOTOR2_STEP_PIN, "dir": MOTOR2_DIR_PIN, "direction": MOTOR2_DIRECTION},
    )

    try:
        print("Démarrage... Tenez le robot bien droit à -90° !")
        motors.set_speeds(0, 0)
        motors.start_continuous()
        time.sleep(1)

        # Variables PID
        filtered_angle_x = -90.0
        integral = 0.0
        last_time = time.time()
        print_counter = 0

        while True:
            current_time = time.time()
            dt = current_time - last_time
            if dt <= 0: dt = 0.001
            last_time = current_time

            # Lecture IMU
            x_a, y_a, z_a = driver.read_accel()
            x_g, y_g, z_g = driver.read_gyro()
            
            # Calcul angle (Accéléromètre)
            angle_x = math.degrees(math.atan2(y_a * SF_2G, z_a * SF_2G))
            gyro_x_dps = x_g * SF_200DPS # Ajuster INVERT_GYRO si besoin

            # Filtre Complémentaire
            filtered_angle_x = ALPHA * (filtered_angle_x + gyro_x_dps * dt) + (1.0 - ALPHA) * angle_x
            
            # --- CALCUL DU PID ---
            error = TARGET_ANGLE - filtered_angle_x
            
            if abs(error) < DEADBAND:
                error = 0
            
            # Calcul de l'intégrale avec protection (anti-windup)
            integral += error * dt
            integral = max(min(integral, 40), -40) # Limite l'accumulation pour éviter l'emballement
            
            # Formule PID : 
            # On utilise le gyro_x_dps directement pour le terme Dérivé (D)
            correction_speed = (error * KP) + (integral * KI) - (gyro_x_dps * KD)
            
            # Limitation de la vitesse
            correction_speed = max(min(correction_speed, MAX_SPEED), -MAX_SPEED)
                
            # Application aux moteurs (Inverser le signe si le robot "aide" sa chute au lieu de contrer)
            motors.set_speeds(correction_speed, -correction_speed)
            
            # Affichage
            print_counter += 1
            if print_counter >= 15:
                print(f"Angle: {filtered_angle_x:.2f}° | Vitesse: {correction_speed:.1f} RPM")
                print_counter = 0

            # Timing
            time_spent = time.time() - current_time
            sleep_time = LOOP_DELAY - time_spent
            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nArrêt.")
    finally:
        motors.stop_all()

if __name__ == "__main__":
    main()
