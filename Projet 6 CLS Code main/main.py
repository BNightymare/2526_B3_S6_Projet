# Programme principal du robot suiveur de ligne
# Intègre les capteurs infrarouges, l'IMU et les moteurs


from sensors.MCP3208 import MCP3208
from sensors.line_detector import detect_line
from motor.controller import DualMotorController
from motor.config import (
    MOTOR1_STEP_PIN, MOTOR1_DIR_PIN, MOTOR1_SPEED_RPM, MOTOR1_DIRECTION,
    MOTOR2_STEP_PIN, MOTOR2_DIR_PIN, MOTOR2_SPEED_RPM, MOTOR2_DIRECTION,
    DIRECTION_FORWARD, DIRECTION_BACKWARD
)
import config
import time

# Import optionnel de l'IMU
if config.USE_IMU:
    try:
        from imu.drv_lsm6dsow import drv_lsm6dsow
        IMU_AVAILABLE = True
    except ImportError:
        print("⚠ Module IMU non disponible, fonctionnement sans IMU")
        IMU_AVAILABLE = False
else:
    IMU_AVAILABLE = False


class LineFollowerRobot:
    """Classe principale du robot suiveur de ligne"""
    
    def __init__(self):
        """Initialise tous les composants du robot"""
        print("=" * 60)
        print("INITIALISATION DU ROBOT SUIVEUR DE LIGNE")
        print("=" * 60)
        
        # Initialisation du capteur de ligne
        print("\n[1/3] Initialisation du capteur de ligne...")
        try:
            self.line_sensor = MCP3208(
                spi_bus=config.LINE_SENSOR_SPI_BUS,
                spi_device=config.LINE_SENSOR_SPI_DEVICE,
                clock_speed=config.LINE_SENSOR_CLOCK_SPEED,
                vref=config.LINE_SENSOR_VREF
            )
            print("      ✓ Capteur de ligne MCP3208 initialisé")
        except Exception as e:
            print(f"      ✗ Erreur capteur de ligne: {e}")
            raise
        
        # Initialisation des moteurs
        print("\n[2/3] Initialisation des moteurs...")
        try:
            motor1_params = {
                "step": MOTOR1_STEP_PIN,
                "dir": MOTOR1_DIR_PIN,
                "speed_rpm": MOTOR1_SPEED_RPM,
                "direction": MOTOR1_DIRECTION
            }
            
            motor2_params = {
                "step": MOTOR2_STEP_PIN,
                "dir": MOTOR2_DIR_PIN,
                "speed_rpm": MOTOR2_SPEED_RPM,
                "direction": MOTOR2_DIRECTION
            }
            
            self.motor_controller = DualMotorController(motor1_params, motor2_params)
            print("      ✓ Moteurs TMC2225 initialisés")
        except Exception as e:
            print(f"      ✗ Erreur moteurs: {e}")
            self.line_sensor.close()
            raise
        
        # Initialisation optionnelle de l'IMU
        print("\n[3/3] Initialisation de l'IMU...")
        if config.USE_IMU and IMU_AVAILABLE:
            try:
                self.imu = drv_lsm6dsow(
                    bus=config.IMU_I2C_BUS,
                    adresse=config.IMU_I2C_ADDRESS
                )
                self.use_imu = True
                print("      ✓ IMU LSM6DSOX initialisé")
            except Exception as e:
                print(f"      ⚠ IMU non disponible: {e}")
                self.use_imu = False
        else:
            self.use_imu = False
            print("      ⊗ IMU désactivé dans la configuration")
        
        print("\n" + "=" * 60)
        print("✓ ROBOT PRÊT À DÉMARRER")
        print("=" * 60 + "\n")
    
    def move_forward(self):
        """Fait avancer le robot en ligne droite"""
        if config.DEBUG_MODE:
            print("  → Avancer tout droit")
        self.motor_controller.rotate_sync(
            angle=config.FORWARD_ANGLE,
            inverse=False
        )
    
    def turn_left(self, angle):
        """Tourne le robot vers la gauche"""
        if config.DEBUG_MODE:
            print(f"  ← Virage gauche ({angle}°)")
        # Pour tourner à gauche : moteur droit avance plus que le gauche
        self.motor_controller.motor2.rotate(angle)
        # On peut ajuster le moteur 1 si nécessaire
    
    def turn_right(self, angle):
        """Tourne le robot vers la droite"""
        if config.DEBUG_MODE:
            print(f"  → Virage droite ({angle}°)")
        # Pour tourner à droite : moteur gauche avance plus que le droit
        self.motor_controller.motor1.rotate(angle)
        # On peut ajuster le moteur 2 si nécessaire
    
    def correct_trajectory(self, position):
        """
        Corrige la trajectoire du robot en fonction de la position de la ligne
        
        Args:
            position (str): Position détectée ('Line on the left', 'Line in the center', 
                          'Line on the right', 'No line detected')
        """
        if position == "Line in the center":
            # La ligne est au centre, avancer tout droit
            self.move_forward()
            
        elif position == "Line on the left":
            # La ligne est à gauche, tourner à gauche
            self.turn_left(config.ROTATION_ANGLE_MEDIUM)
            
        elif position == "Line on the right":
            # La ligne est à droite, tourner à droite
            self.turn_right(config.ROTATION_ANGLE_MEDIUM)
            
        else:  # "No line detected"
            # Aucune ligne détectée, arrêter ou chercher
            print("  ⚠ LIGNE PERDUE - Recherche...")
            # Stratégie de recherche : tourner légèrement à gauche puis à droite
            time.sleep(0.5)
    
    def read_imu_data(self):
        """Lit les données de l'IMU si disponible"""
        if self.use_imu:
            try:
                x_a, y_a, z_a = self.imu.read_accel()
                x_g, y_g, z_g = self.imu.read_gyro()
                if config.DEBUG_MODE:
                    print(f"  IMU - Accel: ({x_a}, {y_a}, {z_a}) | Gyro: ({x_g}, {y_g}, {z_g})")
                return {"accel": (x_a, y_a, z_a), "gyro": (x_g, y_g, z_g)}
            except Exception as e:
                print(f"  ⚠ Erreur lecture IMU: {e}")
                return None
        return None
    
    def run(self):
        """Boucle principale du robot"""
        try:
            print("\n" + "=" * 60)
            print("DÉMARRAGE DU SUIVI DE LIGNE")
            print("=" * 60)
            print("Appuyez sur Ctrl+C pour arrêter le robot\n")
            
            # Afficher les infos des moteurs
            if config.DEBUG_MODE:
                self.motor_controller.info()
            
            iteration = 0
            
            while True:
                iteration += 1
                if config.DEBUG_MODE:
                    print(f"\n--- Itération {iteration} ---")
                
                # Lire la position de la ligne
                position = detect_line(
                    self.line_sensor, 
                    threshold=config.LINE_THRESHOLD
                )
                
                # Corriger la trajectoire
                self.correct_trajectory(position)
                
                # Lire l'IMU pour stabilisation (optionnel)
                if self.use_imu:
                    self.read_imu_data()
                
                # Délai avant la prochaine itération
                time.sleep(config.LOOP_DELAY)
                
        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("ARRÊT DEMANDÉ PAR L'UTILISATEUR")
            print("=" * 60)
            self.shutdown()
            
        except Exception as e:
            print(f"\n\n⚠ ERREUR CRITIQUE: {e}")
            import traceback
            traceback.print_exc()
            self.shutdown()
    
    def shutdown(self):
        """Arrêt propre du robot"""
        print("\nArrêt des composants...")
        
        # Arrêt du capteur de ligne
        try:
            self.line_sensor.close()
            print("  ✓ Capteur de ligne fermé")
        except Exception as e:
            print(f"  ✗ Erreur fermeture capteur: {e}")
        
        # Arrêt des moteurs
        try:
            self.motor_controller.stop_all()
            print("  ✓ Moteurs arrêtés")
        except Exception as e:
            print(f"  ✗ Erreur arrêt moteurs: {e}")
        
        # Arrêt de l'IMU
        if self.use_imu:
            try:
                self.imu.close()
                print("  ✓ IMU fermé")
            except Exception as e:
                print(f"  ✗ Erreur fermeture IMU: {e}")
        
        print("\n" + "=" * 60)
        print("✓ ROBOT ARRÊTÉ PROPREMENT")
        print("=" * 60 + "\n")


def main():
    """Point d'entrée du programme"""
    try:
        robot = LineFollowerRobot()
        robot.run()
    except Exception as e:
        print(f"\n⚠ Impossible de démarrer le robot: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
