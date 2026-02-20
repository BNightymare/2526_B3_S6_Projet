"""
Script de test pour vérifier individuellement chaque composant du robot
Utiliser ce script avant de lancer le programme principal
"""

import sys
import time

def test_sensors():
    """Test des capteurs infrarouges"""
    print("\n" + "="*60)
    print("TEST DES CAPTEURS INFRAROUGES")
    print("="*60)
    
    try:
        from sensors.MCP3208 import MCP3208
        from sensors.line_detector import detect_line
        import config
        
        print("Initialisation du capteur MCP3208...")
        sensor = MCP3208(
            spi_bus=config.LINE_SENSOR_SPI_BUS,
            spi_device=config.LINE_SENSOR_SPI_DEVICE,
            clock_speed=config.LINE_SENSOR_CLOCK_SPEED,
            vref=config.LINE_SENSOR_VREF
        )
        print("✓ Capteur initialisé\n")
        
        print("Lecture des 8 capteurs pendant 5 secondes...")
        print("(Déplacez une ligne sous les capteurs)\n")
        
        for i in range(10):
            position = detect_line(sensor, threshold=config.LINE_THRESHOLD)
            time.sleep(0.5)
        
        sensor.close()
        print("\n✓ Test des capteurs réussi!")
        return True
        
    except Exception as e:
        print(f"\n✗ Erreur lors du test des capteurs: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_motors():
    """Test des moteurs"""
    print("\n" + "="*60)
    print("TEST DES MOTEURS")
    print("="*60)
    
    try:
        from motor.controller import DualMotorController
        from motor.config import (
            MOTOR1_STEP_PIN, MOTOR1_DIR_PIN, MOTOR1_SPEED_RPM, MOTOR1_DIRECTION,
            MOTOR2_STEP_PIN, MOTOR2_DIR_PIN, MOTOR2_SPEED_RPM, MOTOR2_DIRECTION
        )
        
        print("Initialisation des moteurs...")
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
        
        motors = DualMotorController(motor1_params, motor2_params)
        print("✓ Moteurs initialisés\n")
        
        motors.info()
        
        print("\nTest 1: Rotation synchrone 90° (les deux moteurs)")
        motors.rotate_sync(90, inverse=False)
        time.sleep(1)
        
        print("\nTest 2: Rotation moteur 1 seulement (45°)")
        motors.motor1.rotate(45)
        time.sleep(1)
        
        print("\nTest 3: Rotation moteur 2 seulement (45°)")
        motors.motor2.rotate(45)
        time.sleep(1)
        
        motors.stop_all()
        print("\n✓ Test des moteurs réussi!")
        return True
        
    except Exception as e:
        print(f"\n✗ Erreur lors du test des moteurs: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_imu():
    """Test de l'IMU"""
    print("\n" + "="*60)
    print("TEST DE L'IMU")
    print("="*60)
    
    try:
        from imu.drv_lsm6dsow import drv_lsm6dsow
        import config
        
        print("Initialisation de l'IMU LSM6DSOX...")
        imu = drv_lsm6dsow(
            bus=config.IMU_I2C_BUS,
            adresse=config.IMU_I2C_ADDRESS
        )
        print("✓ IMU initialisé\n")
        
        print("Lecture des données pendant 5 secondes...")
        print("(Bougez le capteur pour voir les valeurs changer)\n")
        
        for i in range(10):
            x_a, y_a, z_a = imu.read_accel()
            x_g, y_g, z_g = imu.read_gyro()
            
            print(f"Accel: X={x_a:6d} Y={y_a:6d} Z={z_a:6d} | "
                  f"Gyro: X={x_g:6d} Y={y_g:6d} Z={z_g:6d}")
            time.sleep(0.5)
        
        imu.close()
        print("\n✓ Test de l'IMU réussi!")
        return True
        
    except Exception as e:
        print(f"\n✗ Erreur lors du test de l'IMU: {e}")
        print("(C'est normal si l'IMU n'est pas connecté)")
        import traceback
        traceback.print_exc()
        return False


def test_all():
    """Lance tous les tests"""
    print("\n" + "="*60)
    print("TESTS DES COMPOSANTS DU ROBOT")
    print("="*60)
    print("\nCe script va tester chaque composant individuellement.")
    print("Assurez-vous que tout est branché correctement.\n")
    
    input("Appuyez sur Entrée pour commencer les tests...")
    
    results = {
        "Capteurs": False,
        "Moteurs": False,
        "IMU": False
    }
    
    # Test des capteurs
    results["Capteurs"] = test_sensors()
    
    # Test des moteurs
    if input("\n\nVoulez-vous tester les moteurs? (o/n): ").lower() == 'o':
        results["Moteurs"] = test_motors()
    else:
        print("Test des moteurs ignoré.")
    
    # Test de l'IMU
    if input("\n\nVoulez-vous tester l'IMU? (o/n): ").lower() == 'o':
        results["IMU"] = test_imu()
    else:
        print("Test de l'IMU ignoré.")
    
    # Résumé
    print("\n\n" + "="*60)
    print("RÉSUMÉ DES TESTS")
    print("="*60)
    
    for component, success in results.items():
        status = "✓ RÉUSSI" if success else "✗ ÉCHOUÉ"
        print(f"{component:.<30} {status}")
    
    print("\n")
    
    if all(results.values()):
        print("✓ Tous les tests ont réussi! Le robot est prêt.")
    else:
        print("⚠ Certains tests ont échoué. Vérifiez les composants.")
    
    print("="*60 + "\n")


def main():
    """Menu principal"""
    print("\n╔════════════════════════════════════════════════════════╗")
    print("║       SCRIPT DE TEST - ROBOT SUIVEUR DE LIGNE         ║")
    print("╚════════════════════════════════════════════════════════╝")
    print("\nChoisissez un test à effectuer:")
    print("  1. Tester les capteurs infrarouges")
    print("  2. Tester les moteurs")
    print("  3. Tester l'IMU")
    print("  4. Tester tous les composants")
    print("  5. Quitter")
    
    choice = input("\nVotre choix (1-5): ")
    
    if choice == '1':
        test_sensors()
    elif choice == '2':
        test_motors()
    elif choice == '3':
        test_imu()
    elif choice == '4':
        test_all()
    elif choice == '5':
        print("Au revoir!")
        sys.exit(0)
    else:
        print("Choix invalide.")
    
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrompu par l'utilisateur.")
        sys.exit(0)
