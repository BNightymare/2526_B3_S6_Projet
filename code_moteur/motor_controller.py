from .motor_driver import TMC2225
import threading
import time
from .motor_config import (DEFAULT_SPEED_RPM, DEFAULT_STEPS_PER_REV, DEFAULT_MICROSTEP,
                     DIRECTION_FORWARD, DIRECTION_BACKWARD)

class DualMotorController:
    
    
    def __init__(self, motor1_params, motor2_params):
      

        self.motor1 = TMC2225(
            step_pin=motor1_params["step"],
            dir_pin=motor1_params["dir"],
            speed_rpm=motor1_params.get("speed_rpm", DEFAULT_SPEED_RPM),
            direction=motor1_params.get("direction", DIRECTION_FORWARD),
            steps_per_rev=motor1_params.get("steps_per_rev", DEFAULT_STEPS_PER_REV),
            microstep=motor1_params.get("microstep", DEFAULT_MICROSTEP)
        )

        self.motor2 = TMC2225(
            step_pin=motor2_params["step"],
            dir_pin=motor2_params["dir"],
            speed_rpm=motor2_params.get("speed_rpm", DEFAULT_SPEED_RPM),
            direction=motor2_params.get("direction", DIRECTION_BACKWARD), # 0 par défaut
            steps_per_rev=motor2_params.get("steps_per_rev", DEFAULT_STEPS_PER_REV),
            microstep=motor2_params.get("microstep", DEFAULT_MICROSTEP)
        )

    def rotate_both(self, angle1, angle2):
        """Fait tourner les deux moteurs avec des angles potentiellement différents."""
        print(f"Rotation motor1={angle1}° | motor2={angle2}°")
        thread1 = threading.Thread(target=self.motor1.rotate, args=(angle1,))
        thread2 = threading.Thread(target=self.motor2.rotate, args=(angle2,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

 
    def rotate_sync(self, angle, inverse=False):
        """
        Fait tourner les deux moteurs ensemble du même angle.
        Si inverse=True, le deuxième tourne en sens inverse.
        """
        print(f"Rotation synchrone {angle}° (inverse={inverse})")
        original_direction = self.motor2.direction
        if inverse:
            # Calcule la direction opposée (ex: 1+0 - 1 = 0; 1+0 - 0 = 1)
            opposite_direction = (DIRECTION_FORWARD + DIRECTION_BACKWARD) - original_direction
            self.motor2.set_direction(opposite_direction)

        thread1 = threading.Thread(target=self.motor1.rotate, args=(angle,))
        thread2 = threading.Thread(target=self.motor2.rotate, args=(angle,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        
        if inverse:
            # Remet la direction d'origine
            self.motor2.set_direction(original_direction)

    def stop_all(self):
        """Nettoie les deux moteurs."""
        self.motor1.cleanup()
        self.motor2.cleanup()

    def info(self):
        """Affiche les infos des deux moteurs."""
        print("\n=== INFOS MOTEURS ===")
        self.motor1.info()
        self.motor2.info()
        print("=====================\n")
