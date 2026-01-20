# PCB Testing Scripts / Scripts de Test PCB

Ce répertoire contient les scripts Python pour tester les composants du PCB.

This directory contains Python scripts to test PCB components.

## Installation / Installation

### Dépendances / Dependencies

```bash
# Installer les bibliothèques nécessaires / Install required libraries
pip install smbus-cffi spidev RPi.GPIO
```

## Scripts disponibles / Available Scripts

### test_imu.py

Script de test et validation de l'IMU (Inertial Measurement Unit).

IMU testing and validation script.

**Composants testés / Components tested:**
- MPU6050, MPU9250, LSM6DS3, BMI160 ou similaires / or similar
- Communication I2C
- Accéléromètre / Accelerometer
- Gyroscope
- Capteur de température / Temperature sensor

**Tests effectués / Tests performed:**
1. Détection et identification / Detection and identification
2. Initialisation / Initialization
3. Lecture de données / Data reading
4. Test de gravité statique / Static gravity test
5. Test de rotation / Rotation test
6. Test de température / Temperature test

**Utilisation / Usage:**

```bash
# Exécuter tous les tests / Run all tests
python3 test_imu.py

# ou avec sudo si nécessaire pour I2C / or with sudo if needed for I2C
sudo python3 test_imu.py
```

**Configuration / Configuration:**

Le script détecte automatiquement l'adresse I2C de l'IMU (0x68 ou 0x69).

The script automatically detects the IMU I2C address (0x68 or 0x69).

---

### test_mcp3208.py

Script de test et validation du MCP3208 (ADC 12-bit, 8 canaux).

MCP3208 testing and validation script (12-bit ADC, 8 channels).

**Composants testés / Components tested:**
- MCP3208 ADC
- Communication SPI
- 8 canaux analogiques / 8 analog channels

**Tests effectués / Tests performed:**
1. Communication SPI / SPI communication
2. Lecture de tous les canaux / All channels reading
3. Test de référence (GND/VCC) / Reference test (GND/VCC) [manuel/manual]
4. Test de linéarité / Linearity test [manuel/manual]
5. Test de bruit / Noise test [manuel/manual]

**Utilisation / Usage:**

```bash
# Exécuter les tests / Run tests
python3 test_mcp3208.py

# ou avec sudo si nécessaire pour SPI / or with sudo if needed for SPI
sudo python3 test_mcp3208.py
```

**Note:** Les tests détaillés nécessitent l'application manuelle de tensions connues aux entrées de l'ADC.

**Note:** Detailed tests require manual application of known voltages to ADC inputs.

---

## Configuration matérielle / Hardware Configuration

### Connexions I2C (IMU)

| Signal | Pin Raspberry Pi | Pin IMU |
|--------|-----------------|---------|
| SDA    | GPIO 2 (Pin 3)  | SDA     |
| SCL    | GPIO 3 (Pin 5)  | SCL     |
| VCC    | 3.3V            | VCC     |
| GND    | GND             | GND     |

### Connexions SPI (MCP3208)

| Signal | Pin Raspberry Pi | Pin MCP3208 |
|--------|-----------------|-------------|
| MOSI   | GPIO 10 (Pin 19)| DIN (11)    |
| MISO   | GPIO 9 (Pin 21) | DOUT (12)   |
| SCK    | GPIO 11 (Pin 23)| CLK (13)    |
| CE0    | GPIO 8 (Pin 24) | CS (10)     |
| VCC    | 3.3V            | VDD (16), VREF (15) |
| GND    | GND             | GND (9), AGND (14)  |

## Activation des interfaces / Enable Interfaces

### Activer I2C / Enable I2C

```bash
# Raspberry Pi
sudo raspi-config
# Interface Options -> I2C -> Yes

# Vérifier / Verify
i2cdetect -y 1
```

### Activer SPI / Enable SPI

```bash
# Raspberry Pi
sudo raspi-config
# Interface Options -> SPI -> Yes

# Vérifier / Verify
ls /dev/spi*
```

## Dépannage / Troubleshooting

### I2C ne détecte pas l'IMU / I2C doesn't detect IMU

1. Vérifier les connexions / Check connections
2. Vérifier l'alimentation 3.3V / Check 3.3V power supply
3. Essayer l'autre adresse (0x68 ou 0x69) / Try other address
4. Vérifier que I2C est activé / Verify I2C is enabled

```bash
# Scanner le bus I2C / Scan I2C bus
i2cdetect -y 1
```

### SPI ne communique pas / SPI doesn't communicate

1. Vérifier les connexions / Check connections
2. Vérifier l'alimentation / Check power supply
3. Vérifier que SPI est activé / Verify SPI is enabled
4. Vérifier la vitesse SPI (réduire si nécessaire) / Check SPI speed (reduce if needed)

```bash
# Tester SPI / Test SPI
ls -l /dev/spi*
```

### Erreurs de permission / Permission errors

```bash
# Ajouter l'utilisateur aux groupes nécessaires / Add user to necessary groups
sudo usermod -a -G i2c,spi,gpio $USER
# Déconnecter et reconnecter / Logout and login
```

## Références / References

- [MCP3208 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/21298e.pdf)
- [MPU6050 Datasheet](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf)
- [Raspberry Pi SPI](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md)
- [Raspberry Pi I2C](https://www.raspberrypi.org/documentation/hardware/raspberrypi/i2c/README.md)
