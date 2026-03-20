"""Configuration globale des moteurs et du robot."""

# ── Direction ──────────────────────────────────────────────────────────────────
DEGREES_PER_CIRCLE = 360
DIRECTION_FORWARD  = 1
DIRECTION_BACKWARD = 0

# ── Pins (numérotation physique BOARD) ────────────────────────────────────────
MOTOR1_STEP_PIN  = 32
MOTOR1_DIR_PIN   = 36
MOTOR1_DIRECTION = DIRECTION_FORWARD

MOTOR2_STEP_PIN  = 33
MOTOR2_DIR_PIN   = 31
MOTOR2_DIRECTION = DIRECTION_BACKWARD

# ── Paramètres moteur ──────────────────────────────────────────────────────────
DEFAULT_STEPS_PER_REV = 200
DEFAULT_MICROSTEP     = 16
DEFAULT_SPEED_RPM     = 9.375   # 500 Hz à 16 microsteps
MAX_SPEED_RPM         = 60.0

MOTOR1_SPEED_RPM = 9.375
MOTOR2_SPEED_RPM = 9.375

# ── PID équilibre ──────────────────────────────────────────────────────────────
BALANCE_KP = 30.0
BALANCE_KI = 0.5
BALANCE_KD = 1.2
BALANCE_KG = 1.0

# ── PID suivi de ligne ─────────────────────────────────────────────────────────
LINE_KP = 8.0
LINE_KI = 0.0
LINE_KD = 0.5

# ── Paramètres IMU / filtre complémentaire ─────────────────────────────────────
ALPHA        = 0.98    # 98% gyro, 2% accéléromètre
OUTPUT_BETA  = 0.0     # lissage sortie PID (0 = désactivé)
IMU_AXIS     = "x"     # axe de penchement avant/arrière
ANGLE_OFFSET = 0.0     # à calibrer avec : python3 main_imu.py --calibrate
DEADBAND_DEG = 2.0     # zone morte en degrés (évite les tremblements)

# ── Suivi de ligne ─────────────────────────────────────────────────────────────
LINE_THRESHOLD   = 1.5  # seuil de détection IR en volts
SEARCH_SPEED_RPM = 3.0  # vitesse de rotation quand la ligne est perdue

# ── Sécurité ───────────────────────────────────────────────────────────────────
FALL_ANGLE = 45.0       # angle (°) au-delà duquel on coupe les moteurs
