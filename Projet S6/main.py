import board
import busio
import adafruit_mcp3208
from adafruit_lsm6ds.lsm6dox import LSM6DOX
import PWMio
import time

# Initialiser la communication SPI pour MCP3208
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = board.D8
mcp = adafruit_mcp3208.MCP3208(spi, cs)

# Initialiser I2C pour LSM6DOX
i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DOX(i2c)

# Configuration moteurs
motor_left_pwm = PWMio.PWMOut(board.D9, frequency=1000)
motor_right_pwm = PWMio.PWMOut(board.D10, frequency=1000)
motor_left_dir = board.D11
motor_right_dir = board.D12

def set_motor_speed(left_speed, right_speed):
    """Contrôler la vitesse des moteurs (-1 à 1)"""
    motor_left_pwm.duty_cycle = int(abs(left_speed) * 65535)
    motor_right_pwm.duty_cycle = int(abs(right_speed) * 65535)

def read_line_sensor():
    """Lire la position de la ligne (canal 0 du MCP3208)"""
    return mcp.channel[0].value

def read_accelerometer():
    """Lire l'accélération pour éviter les chutes"""
    return sensor.acceleration

def stabilize_balance(accel_z, threshold=8.0):
    """Vérifier si le robot ne tombe pas"""
    return accel_z > threshold

def main():
    print("Démarrage du robot suiveur de ligne")
    
    while True:
        # Lire capteur de ligne
        line_position = read_line_sensor()
        
        # Lire accéléromètre
        accel_x, accel_y, accel_z = read_accelerometer()
        
        # Vérifier l'équilibre
        if not stabilize_balance(accel_z):
            print("Attention: Chute détectée!")
            set_motor_speed(0, 0)
            continue
        
        # Calculer correction pour suivre la ligne
        error = line_position - 2048  # Centrer autour de 2048
        correction = error / 2048.0
        
        # Limiter correction
        correction = max(-1, min(1, correction))
        
        # Appliquer commandes moteurs
        base_speed = 0.6
        left_speed = base_speed - correction
        right_speed = base_speed + correction
        
        set_motor_speed(left_speed, right_speed)
        
        time.sleep(0.05)

if __name__ == "__main__":
    main()