"""
Configuration globale du robot suiveur de ligne
"""

# ==================== CONFIGURATION DES CAPTEURS ====================

# Capteur de ligne infrarouge (MCP3208)
LINE_SENSOR_SPI_BUS = 0
LINE_SENSOR_SPI_DEVICE = 0
LINE_SENSOR_CLOCK_SPEED = 1000000
LINE_SENSOR_VREF = 3.3
LINE_THRESHOLD = 1.5  # Seuil de détection de ligne (en volts)

# IMU (LSM6DSOX)
IMU_I2C_BUS = 1
IMU_I2C_ADDRESS = 0x6A
USE_IMU = False  # Mettre à True pour activer l'IMU


# ==================== CONFIGURATION DES MOTEURS ====================

# Moteur 1 (Gauche)
MOTOR1_STEP_PIN = 32
MOTOR1_DIR_PIN = 36
MOTOR1_DIRECTION = 1  # 1 = Forward, 0 = Backward
MOTOR1_SPEED_RPM = 9.375

# Moteur 2 (Droit)
MOTOR2_STEP_PIN = 33
MOTOR2_DIR_PIN = 31
MOTOR2_DIRECTION = 0  # 1 = Forward, 0 = Backward
MOTOR2_SPEED_RPM = 5.625

# Paramètres des moteurs
STEPS_PER_REV = 200
MICROSTEP = 16


# ==================== CONFIGURATION DU COMPORTEMENT ====================

# Angles de rotation pour les corrections
ROTATION_ANGLE_SOFT = 5      # Petite correction
ROTATION_ANGLE_MEDIUM = 10   # Correction moyenne
ROTATION_ANGLE_HARD = 20     # Grande correction

# Vitesse de déplacement
FORWARD_ANGLE = 360          # Angle de rotation pour avancer

# Délai entre les lectures
LOOP_DELAY = 0.05  # En secondes

# Mode debug
DEBUG_MODE = True  # Affiche plus d'informations
