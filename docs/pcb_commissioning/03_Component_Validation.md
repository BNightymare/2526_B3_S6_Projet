# Validation IMU, Moteurs et MCP3208 / IMU, Motors and MCP3208 Validation

## 1. Introduction

Ce document décrit les procédures de validation pour les composants spécifiques du PCB.

This document describes validation procedures for specific PCB components.

## 2. Validation de l'IMU (Inertial Measurement Unit)

### 2.1 Identification du composant / Component Identification

IMUs couramment utilisés / Commonly used IMUs:
- MPU6050 (6-axis: gyroscope + accelerometer)
- MPU9250 (9-axis: gyroscope + accelerometer + magnetometer)
- LSM6DS3 (6-axis)
- BMI160 (6-axis)

### 2.2 Test de communication / Communication Test

#### Procédure / Procedure

```python
import smbus
import time

# Configuration I2C
I2C_BUS = 1
IMU_ADDR = 0x68  # ou 0x69 / or 0x69

bus = smbus.SMBus(I2C_BUS)

def test_imu_connection():
    """Tester la connexion avec l'IMU / Test connection with IMU"""
    try:
        # Lire le registre WHO_AM_I / Read WHO_AM_I register
        who_am_i = bus.read_byte_data(IMU_ADDR, 0x75)
        print(f"WHO_AM_I: 0x{who_am_i:02X}")
        
        # Valeurs attendues / Expected values:
        # MPU6050: 0x68
        # MPU9250: 0x71
        # Vérifier avec la datasheet / Verify with datasheet
        
        return True
    except Exception as e:
        print(f"Erreur de communication / Communication error: {e}")
        return False

# Exécuter le test / Run test
if test_imu_connection():
    print("✓ IMU détectée / IMU detected")
else:
    print("✗ IMU non détectée / IMU not detected")
```

### 2.3 Initialisation et configuration / Initialization and Configuration

```python
def initialize_imu():
    """Initialiser l'IMU / Initialize IMU"""
    try:
        # Reset de l'IMU / Reset IMU
        bus.write_byte_data(IMU_ADDR, 0x6B, 0x80)
        time.sleep(0.1)
        
        # Sortir du mode sleep / Exit sleep mode
        bus.write_byte_data(IMU_ADDR, 0x6B, 0x00)
        time.sleep(0.1)
        
        # Configurer le gyroscope / Configure gyroscope
        # ±250 degrés/seconde / ±250 degrees/second
        bus.write_byte_data(IMU_ADDR, 0x1B, 0x00)
        
        # Configurer l'accéléromètre / Configure accelerometer
        # ±2g
        bus.write_byte_data(IMU_ADDR, 0x1C, 0x00)
        
        # Activer le filtre passe-bas / Enable low-pass filter
        bus.write_byte_data(IMU_ADDR, 0x1A, 0x03)
        
        print("✓ IMU initialisée / IMU initialized")
        return True
    except Exception as e:
        print(f"Erreur d'initialisation / Initialization error: {e}")
        return False
```

### 2.4 Test de lecture des données / Data Reading Test

```python
def read_imu_data():
    """Lire les données de l'IMU / Read IMU data"""
    try:
        # Lire 14 octets à partir du registre 0x3B
        # Read 14 bytes from register 0x3B
        data = bus.read_i2c_block_data(IMU_ADDR, 0x3B, 14)
        
        # Accéléromètre / Accelerometer
        accel_x = (data[0] << 8) | data[1]
        accel_y = (data[2] << 8) | data[3]
        accel_z = (data[4] << 8) | data[5]
        
        # Convertir en valeurs signées / Convert to signed values
        if accel_x > 32767:
            accel_x -= 65536
        if accel_y > 32767:
            accel_y -= 65536
        if accel_z > 32767:
            accel_z -= 65536
        
        # Température / Temperature
        temp_raw = (data[6] << 8) | data[7]
        if temp_raw > 32767:
            temp_raw -= 65536
        temp = (temp_raw / 340.0) + 36.53
        
        # Gyroscope
        gyro_x = (data[8] << 8) | data[9]
        gyro_y = (data[10] << 8) | data[11]
        gyro_z = (data[12] << 8) | data[13]
        
        # Convertir en valeurs signées / Convert to signed values
        if gyro_x > 32767:
            gyro_x -= 65536
        if gyro_y > 32767:
            gyro_y -= 65536
        if gyro_z > 32767:
            gyro_z -= 65536
        
        return {
            'accel': (accel_x, accel_y, accel_z),
            'gyro': (gyro_x, gyro_y, gyro_z),
            'temp': temp
        }
    except Exception as e:
        print(f"Erreur de lecture / Reading error: {e}")
        return None

# Test de lecture continue / Continuous reading test
print("Test de lecture de l'IMU (10 échantillons) / IMU reading test (10 samples)")
for i in range(10):
    data = read_imu_data()
    if data:
        print(f"Sample {i+1}:")
        print(f"  Accel (x,y,z): {data['accel']}")
        print(f"  Gyro  (x,y,z): {data['gyro']}")
        print(f"  Temp: {data['temp']:.2f}°C")
    time.sleep(0.1)
```

### 2.5 Tests de validation / Validation Tests

#### Test 1: Gravité statique / Static Gravity Test
```
1. Placer le PCB à plat / Place PCB flat
2. Lire l'accéléromètre / Read accelerometer
3. Vérifier que l'axe Z ≈ 1g (±16384 pour ±2g config)
   Verify Z-axis ≈ 1g (±16384 for ±2g config)
4. Vérifier que X et Y ≈ 0
   Verify X and Y ≈ 0

Résultats / Results:
Accel X: _____ (attendu/expected: 0 ± 2000)
Accel Y: _____ (attendu/expected: 0 ± 2000)
Accel Z: _____ (attendu/expected: 16384 ± 2000)
```

#### Test 2: Rotation / Rotation Test
```
1. Faire pivoter lentement le PCB autour de l'axe Z
   Slowly rotate PCB around Z-axis
2. Observer le gyroscope Z
   Observe gyroscope Z
3. Vérifier une valeur non nulle pendant la rotation
   Verify non-zero value during rotation
4. Vérifier retour à ~0 à l'arrêt
   Verify return to ~0 when stopped

☐ PASS  ☐ FAIL  Gyroscope répond à la rotation / Gyroscope responds to rotation
```

#### Test 3: Température / Temperature Test
```
1. Lire la température / Read temperature
2. Vérifier qu'elle est dans une plage raisonnable
   Verify it's in reasonable range

Température mesurée / Measured temperature: _____ °C
Attendu / Expected: 20-30°C (température ambiante / room temperature)

☐ PASS  ☐ FAIL  Température cohérente / Temperature coherent
```

## 3. Validation des Moteurs / Motor Validation

### 3.1 Configuration matérielle / Hardware Configuration

- Type de moteur / Motor type: DC brushed / Stepper / Servo
- Tension nominale / Nominal voltage: _____ V
- Courant nominal / Nominal current: _____ mA
- Driver de moteur / Motor driver: L298N / DRV8833 / autre

### 3.2 Test du driver de moteur / Motor Driver Test

#### Test de contrôle directionnel / Directional Control Test

```python
import RPi.GPIO as GPIO
import time

# Configuration des GPIO / GPIO setup
MOTOR_IN1 = 17  # Adapter selon votre configuration / Adjust to your setup
MOTOR_IN2 = 27
MOTOR_ENA = 22  # PWM enable

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_IN1, GPIO.OUT)
GPIO.setup(MOTOR_IN2, GPIO.OUT)
GPIO.setup(MOTOR_ENA, GPIO.OUT)

# Créer un objet PWM / Create PWM object
pwm = GPIO.PWM(MOTOR_ENA, 1000)  # 1kHz
pwm.start(0)

def motor_forward(speed):
    """Moteur en avant / Motor forward"""
    GPIO.output(MOTOR_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)
    
def motor_backward(speed):
    """Moteur en arrière / Motor backward"""
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)
    
def motor_stop():
    """Arrêter le moteur / Stop motor"""
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

# Séquence de test / Test sequence
print("Test moteur en avant / Forward motor test")
motor_forward(50)  # 50% de vitesse / 50% speed
time.sleep(2)

print("Test moteur en arrière / Backward motor test")
motor_backward(50)
time.sleep(2)

motor_stop()
print("Test terminé / Test completed")

GPIO.cleanup()
```

#### Tests de validation / Validation Tests

```
Test 1: Direction
☐ PASS  ☐ FAIL  Moteur tourne en avant / Motor rotates forward
☐ PASS  ☐ FAIL  Moteur tourne en arrière / Motor rotates backward
☐ PASS  ☐ FAIL  Moteur s'arrête proprement / Motor stops cleanly

Test 2: Contrôle de vitesse / Speed Control
Tester à différentes vitesses / Test at different speeds:
☐ PASS  ☐ FAIL  25% duty cycle
☐ PASS  ☐ FAIL  50% duty cycle
☐ PASS  ☐ FAIL  75% duty cycle
☐ PASS  ☐ FAIL  100% duty cycle

Test 3: Charge / Load Test
☐ PASS  ☐ FAIL  Moteur fonctionne sous charge normale
                  Motor operates under normal load
☐ PASS  ☐ FAIL  Courant mesuré: _____ mA (< courant max / < max current)
☐ PASS  ☐ FAIL  Température driver: _____ °C (< 70°C)
```

### 3.3 Test de performance / Performance Test

```python
def test_motor_performance():
    """Test de performance du moteur / Motor performance test"""
    
    # Test d'accélération / Acceleration test
    print("Test d'accélération / Acceleration test")
    for speed in range(0, 101, 10):
        motor_forward(speed)
        time.sleep(0.5)
    
    # Test de décélération / Deceleration test
    print("Test de décélération / Deceleration test")
    for speed in range(100, -1, -10):
        motor_forward(speed)
        time.sleep(0.5)
    
    motor_stop()
```

## 4. Validation du MCP3208 (ADC)

### 4.1 Configuration SPI / SPI Configuration

```python
import spidev

# Initialiser SPI / Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, Device 0
spi.max_speed_hz = 1000000  # 1MHz
spi.mode = 0

def read_mcp3208(channel):
    """Lire un canal du MCP3208 / Read MCP3208 channel"""
    if channel < 0 or channel > 7:
        raise ValueError("Canal invalide / Invalid channel")
    
    # Commande de lecture single-ended / Single-ended read command
    # Bit de démarrage (1), SGL/DIFF (1), Canal (3 bits)
    cmd = 0x06 | ((channel & 0x07) >> 2)
    cmd2 = (channel & 0x03) << 6
    
    # Envoyer la commande / Send command
    response = spi.xfer2([cmd, cmd2, 0x00])
    
    # Extraire les 12 bits de données / Extract 12-bit data
    value = ((response[0] & 0x01) << 11) | (response[1] << 3) | (response[2] >> 5)
    
    return value

def adc_to_voltage(value, vref=3.3):
    """Convertir valeur ADC en tension / Convert ADC value to voltage"""
    return (value / 4095.0) * vref
```

### 4.2 Tests de validation / Validation Tests

#### Test 1: Référence de tension / Voltage Reference Test
```python
print("Test de référence de tension / Voltage reference test")

# Mesurer sur chaque canal / Measure on each channel
for channel in range(8):
    # Court-circuiter le canal à GND / Short channel to GND
    input("Connecter canal {} à GND, puis appuyer sur Enter".format(channel))
    value = read_mcp3208(channel)
    voltage = adc_to_voltage(value)
    print(f"Canal {channel} (GND): {value} (0x{value:03X}), {voltage:.4f}V")
    assert value < 50, f"Valeur GND trop élevée / GND value too high: {value}"
    
    # Connecter le canal à VCC / Connect channel to VCC
    input("Connecter canal {} à 3.3V, puis appuyer sur Enter".format(channel))
    value = read_mcp3208(channel)
    voltage = adc_to_voltage(value)
    print(f"Canal {channel} (VCC): {value} (0x{value:03X}), {voltage:.4f}V")
    assert value > 4000, f"Valeur VCC trop faible / VCC value too low: {value}"

print("✓ Test de référence terminé / Reference test completed")
```

#### Test 2: Linéarité / Linearity Test
```python
def test_adc_linearity(channel):
    """Tester la linéarité de l'ADC / Test ADC linearity"""
    print(f"Test de linéarité canal {channel} / Linearity test channel {channel}")
    
    # Appliquer différentes tensions et mesurer
    # Apply different voltages and measure
    test_voltages = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    
    for v in test_voltages:
        input(f"Appliquer {v}V au canal {channel}, puis appuyer sur Enter")
        input(f"Apply {v}V to channel {channel}, then press Enter")
        
        # Lire plusieurs fois pour moyenner / Read multiple times to average
        readings = [read_mcp3208(channel) for _ in range(10)]
        avg_value = sum(readings) / len(readings)
        measured_v = adc_to_voltage(avg_value)
        
        error = abs(measured_v - v)
        print(f"Tension attendue / Expected: {v}V, Mesurée / Measured: {measured_v:.4f}V, Erreur / Error: {error:.4f}V")
        
        # Tolérance de ±50mV / Tolerance ±50mV
        assert error < 0.05, f"Erreur trop importante / Error too large: {error}V"
    
    print("✓ Test de linéarité réussi / Linearity test passed")
```

#### Test 3: Bruit et stabilité / Noise and Stability Test
```python
def test_adc_noise(channel, num_samples=100):
    """Mesurer le bruit de l'ADC / Measure ADC noise"""
    print(f"Test de bruit canal {channel} / Noise test channel {channel}")
    input("Connecter le canal à une tension stable (ex: 1.65V), puis appuyer sur Enter")
    input("Connect channel to stable voltage (e.g., 1.65V), then press Enter")
    
    # Collecter des échantillons / Collect samples
    samples = []
    for _ in range(num_samples):
        value = read_mcp3208(channel)
        samples.append(value)
        time.sleep(0.01)
    
    # Analyser les données / Analyze data
    mean_value = sum(samples) / len(samples)
    variance = sum((x - mean_value)**2 for x in samples) / len(samples)
    std_dev = variance ** 0.5
    
    print(f"Moyenne / Mean: {mean_value:.2f} ({adc_to_voltage(mean_value):.4f}V)")
    print(f"Écart-type / Std dev: {std_dev:.2f} ({adc_to_voltage(std_dev):.4f}V)")
    print(f"Min: {min(samples)}, Max: {max(samples)}, Range: {max(samples) - min(samples)}")
    
    # La déviation standard devrait être faible / Standard deviation should be low
    assert std_dev < 5, f"Bruit trop important / Noise too high: {std_dev}"
    
    print("✓ Test de bruit réussi / Noise test passed")
```

## 5. Documentation des résultats / Results Documentation

### 5.1 Rapport de validation / Validation Report

```
========================================
RAPPORT DE VALIDATION DES COMPOSANTS
COMPONENT VALIDATION REPORT
========================================

Date: _______________
Opérateur / Operator: _______________
PCB S/N: _______________

VALIDATION IMU
--------------
Modèle / Model: _______________
Adresse I2C / I2C Address: 0x___
WHO_AM_I: 0x___

☐ PASS  ☐ FAIL  Communication
☐ PASS  ☐ FAIL  Initialisation
☐ PASS  ☐ FAIL  Lecture accéléromètre / Accelerometer reading
☐ PASS  ☐ FAIL  Lecture gyroscope / Gyroscope reading
☐ PASS  ☐ FAIL  Lecture température / Temperature reading
☐ PASS  ☐ FAIL  Test gravité / Gravity test
☐ PASS  ☐ FAIL  Test rotation / Rotation test

VALIDATION MOTEURS / MOTOR VALIDATION
--------------------------------------
Nombre de moteurs / Number of motors: ___
Type: _______________

Pour chaque moteur / For each motor:
Moteur 1:
☐ PASS  ☐ FAIL  Direction avant / Forward direction
☐ PASS  ☐ FAIL  Direction arrière / Backward direction
☐ PASS  ☐ FAIL  Contrôle vitesse / Speed control
☐ PASS  ☐ FAIL  Test de charge / Load test

Moteur 2:
☐ PASS  ☐ FAIL  Direction avant / Forward direction
☐ PASS  ☐ FAIL  Direction arrière / Backward direction
☐ PASS  ☐ FAIL  Contrôle vitesse / Speed control
☐ PASS  ☐ FAIL  Test de charge / Load test

VALIDATION MCP3208
------------------
☐ PASS  ☐ FAIL  Communication SPI
☐ PASS  ☐ FAIL  Test référence / Reference test
☐ PASS  ☐ FAIL  Test linéarité / Linearity test
☐ PASS  ☐ FAIL  Test bruit / Noise test

Canaux fonctionnels / Functional channels: ___/8

RÉSULTAT GLOBAL / OVERALL RESULT
---------------------------------
☐ TOUS LES COMPOSANTS VALIDÉS / ALL COMPONENTS VALIDATED
☐ ÉCHECS DÉTECTÉS / FAILURES DETECTED

Commentaires / Comments:
________________________
________________________
________________________

Signature: _______________
```

## 6. Prochaines étapes / Next Steps

Si tous les tests de validation passent :
If all validation tests pass:

1. Le PCB est prêt pour l'intégration système
   PCB is ready for system integration
2. Archiver tous les rapports de test
   Archive all test reports
3. Marquer le PCB comme "VALIDÉ" / Mark PCB as "VALIDATED"
4. Procéder aux tests d'intégration
   Proceed to integration tests

Si des tests échouent / If tests fail:
1. Documenter précisément les échecs
   Document failures precisely
2. Analyser les causes racines
   Analyze root causes
3. Effectuer les réparations nécessaires
   Perform necessary repairs
4. Répéter les tests de validation
   Repeat validation tests
