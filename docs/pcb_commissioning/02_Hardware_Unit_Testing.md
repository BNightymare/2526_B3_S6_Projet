# Tests Unitaires des Fonctions Matérielles / Hardware Unit Testing

## 1. Introduction

Ce document décrit les procédures de tests unitaires pour valider les fonctions matérielles du PCB.

This document describes unit testing procedures to validate the PCB hardware functions.

## 2. Préparation des tests / Test Preparation

### 2.1 Équipement requis / Required Equipment

- [ ] Multimètre digital / Digital multimeter
- [ ] Oscilloscope (min. 2 canaux / channels)
- [ ] Alimentation de laboratoire réglable / Adjustable lab power supply
- [ ] Câbles et sondes de test / Test cables and probes
- [ ] Ordinateur avec logiciel de test / Computer with testing software

### 2.2 Conditions de test / Test Conditions

- Température ambiante : 20-25°C / Room temperature: 20-25°C
- Humidité relative : < 70% / Relative humidity: < 70%
- PCB à température ambiante / PCB at room temperature

## 3. Tests d'alimentation / Power Supply Tests

### 3.1 Test de la tension d'alimentation / Supply Voltage Test

#### Objectif / Objective
Vérifier que le circuit d'alimentation fournit les tensions correctes.
Verify that the power supply circuit provides correct voltages.

#### Procédure / Procedure

```
1. Connecter l'alimentation de laboratoire (sans allumer le PCB)
   Connect lab power supply (without powering the PCB)
   - Régler à 12V (ou tension nominale)
   - Set to 12V (or nominal voltage)
   - Limiter le courant à 500mA initialement
   - Limit current to 500mA initially

2. Mesurer les tensions à vide (sans charge)
   Measure no-load voltages
   - V_in = ___ V (attendu/expected: 12V ± 0.5V)
   - V_5V = ___ V (attendu/expected: 5.0V ± 0.25V)
   - V_3.3V = ___ V (attendu/expected: 3.3V ± 0.165V)

3. Allumer le PCB et mesurer sous charge nominale
   Power on PCB and measure under nominal load
   - V_5V = ___ V
   - V_3.3V = ___ V
   - I_total = ___ mA

4. Mesurer l'ondulation (ripple) avec oscilloscope
   Measure ripple with oscilloscope
   - Ripple_5V = ___ mV_pp (max: 100mV)
   - Ripple_3.3V = ___ mV_pp (max: 100mV)
```

#### Critères de validation / Validation Criteria

| Rail | Tension nominale / Nominal | Tolérance / Tolerance | Ondulation max / Max Ripple |
|------|---------------------------|----------------------|----------------------------|
| V_in | 12V | ± 0.5V | N/A |
| 5V | 5.0V | ± 5% (± 0.25V) | < 100mV pp |
| 3.3V | 3.3V | ± 5% (± 0.165V) | < 100mV pp |

### 3.2 Test de protection contre les surintensités / Overcurrent Protection Test

```
1. Augmenter progressivement la charge sur le rail 5V
   Gradually increase load on 5V rail
2. Observer le comportement du circuit
   Observe circuit behavior
3. Vérifier que la protection s'active correctement
   Verify protection activates correctly
4. Documenter le seuil de déclenchement
   Document trigger threshold
   I_limit = ___ mA (attendu/expected: ~1000mA)
```

## 4. Tests de communication / Communication Tests

### 4.1 Test UART

#### Configuration / Setup
- Baudrate: 115200
- Data bits: 8
- Parity: None
- Stop bits: 1

#### Procédure / Procedure

```
1. Connecter un adaptateur USB-UART
   Connect USB-UART adapter
2. Configurer le terminal série
   Configure serial terminal
3. Envoyer une commande de test
   Send test command: "AT\r\n"
4. Vérifier la réponse
   Verify response: "OK\r\n"
```

#### Résultats / Results
- [ ] Communication établie / Communication established
- [ ] Pas d'erreurs de trame / No frame errors
- [ ] Données reçues correctement / Data received correctly

### 4.2 Test I2C

#### Procédure / Procedure

```python
# Exemple de code Python pour tester I2C
# Python example code to test I2C

import smbus
import time

bus = smbus.SMBus(1)  # I2C bus number

# Scanner les adresses I2C / Scan I2C addresses
def scan_i2c():
    devices = []
    for address in range(0x03, 0x78):
        try:
            bus.read_byte(address)
            devices.append(hex(address))
            print(f"Périphérique trouvé à / Device found at: {hex(address)}")
        except:
            pass
    return devices

# Tester la lecture d'un registre / Test reading a register
def test_read(address, register):
    try:
        data = bus.read_byte_data(address, register)
        print(f"Données lues / Data read: {hex(data)}")
        return True
    except Exception as e:
        print(f"Erreur / Error: {e}")
        return False

# Exécuter les tests / Run tests
print("Scanning I2C bus...")
devices = scan_i2c()
print(f"Périphériques détectés / Devices detected: {devices}")
```

#### Résultats / Results
- Adresses I2C détectées / I2C addresses detected: _______________
- [ ] IMU détectée (0x68 ou 0x69) / IMU detected (0x68 or 0x69)
- [ ] Autres périphériques / Other devices: _______________

### 4.3 Test SPI

#### Configuration / Setup
- Mode: 0 (CPOL=0, CPHA=0)
- Vitesse: 1 MHz (initial)
- Bits par mot / Bits per word: 8

#### Procédure / Procedure

```
1. Connecter un analyseur logique aux lignes SPI
   Connect logic analyzer to SPI lines
   - MOSI (Master Out Slave In)
   - MISO (Master In Slave Out)
   - SCK (Serial Clock)
   - CS (Chip Select)

2. Envoyer une commande de lecture au MCP3208
   Send read command to MCP3208
   - Commande: 0x06 pour canal 0 en mode single-ended
   - Command: 0x06 for channel 0 in single-ended mode

3. Vérifier la réponse
   Verify response
   - Format attendu: 12 bits de données
   - Expected format: 12-bit data
```

#### Résultats / Results
- [ ] Communication SPI fonctionnelle / SPI communication functional
- [ ] Signaux propres (pas de bruit) / Clean signals (no noise)
- [ ] Vitesse correcte / Correct speed

## 5. Tests des interfaces I/O / I/O Interface Tests

### 5.1 Test des GPIO

#### Procédure / Procedure

```python
# Test des sorties digitales / Digital output test
def test_gpio_output(pin):
    gpio.setup(pin, gpio.OUT)
    
    # Test HIGH
    gpio.output(pin, gpio.HIGH)
    measured_voltage = float(input(f"Mesurer tension sur GPIO{pin} / Measure voltage on GPIO{pin}: "))
    assert 3.0 < measured_voltage < 3.6, "Tension HIGH incorrecte / HIGH voltage incorrect"
    
    # Test LOW
    gpio.output(pin, gpio.LOW)
    measured_voltage = float(input(f"Mesurer tension sur GPIO{pin} / Measure voltage on GPIO{pin}: "))
    assert measured_voltage < 0.4, "Tension LOW incorrecte / LOW voltage incorrect"
    
    return True

# Test des entrées digitales / Digital input test
def test_gpio_input(pin):
    gpio.setup(pin, gpio.IN)
    # Appliquer 3.3V et GND manuellement et vérifier la lecture
    # Apply 3.3V and GND manually and verify reading
    pass
```

### 5.2 Test des entrées analogiques (MCP3208)

```python
def test_adc_channel(channel):
    # Appliquer une tension connue (ex: 2.5V)
    # Apply known voltage (e.g., 2.5V)
    input_voltage = 2.5
    
    # Lire la valeur ADC
    # Read ADC value
    adc_value = read_mcp3208(channel)
    
    # Convertir en tension (12-bit ADC, Vref = 3.3V)
    # Convert to voltage (12-bit ADC, Vref = 3.3V)
    measured_voltage = (adc_value / 4095.0) * 3.3
    
    # Vérifier la précision (±50mV)
    # Verify accuracy (±50mV)
    error = abs(measured_voltage - input_voltage)
    assert error < 0.05, f"Erreur trop importante / Error too large: {error}V"
    
    return measured_voltage
```

## 6. Tests fonctionnels / Functional Tests

### 6.1 Test de charge / Load Test

```
1. Faire fonctionner le système pendant 30 minutes
   Run system for 30 minutes
2. Surveiller la température des composants
   Monitor component temperatures
   - Régulateurs / Regulators: ___ °C (max: 80°C)
   - Microcontrôleur / Microcontroller: ___ °C (max: 70°C)
   - Autres composants / Other components: ___ °C

3. Vérifier la stabilité des tensions
   Verify voltage stability
   - Dérive maximale / Maximum drift: ___ mV (max: 100mV)
```

### 6.2 Test de reset / Reset Test

```
1. Appuyer sur le bouton reset
   Press reset button
2. Vérifier que le système redémarre correctement
   Verify system restarts correctly
3. Vérifier l'état des GPIO après reset
   Verify GPIO states after reset
```

## 7. Documentation des résultats / Results Documentation

### 7.1 Formulaire de rapport de test / Test Report Form

```
========================================
RAPPORT DE TEST MATÉRIEL / HARDWARE TEST REPORT
========================================

Date: _______________
Opérateur / Operator: _______________
PCB S/N: _______________

TESTS D'ALIMENTATION / POWER TESTS
------------------------------------
☐ PASS  ☐ FAIL  Test de tension / Voltage test
☐ PASS  ☐ FAIL  Test d'ondulation / Ripple test
☐ PASS  ☐ FAIL  Test de protection / Protection test

TESTS DE COMMUNICATION / COMMUNICATION TESTS
--------------------------------------------
☐ PASS  ☐ FAIL  UART
☐ PASS  ☐ FAIL  I2C
☐ PASS  ☐ FAIL  SPI

TESTS I/O / I/O TESTS
---------------------
☐ PASS  ☐ FAIL  GPIO
☐ PASS  ☐ FAIL  ADC

TESTS FONCTIONNELS / FUNCTIONAL TESTS
-------------------------------------
☐ PASS  ☐ FAIL  Test de charge / Load test
☐ PASS  ☐ FAIL  Test de reset / Reset test

RÉSULTAT GLOBAL / OVERALL RESULT
---------------------------------
☐ TOUS LES TESTS RÉUSSIS / ALL TESTS PASSED
☐ ÉCHECS DÉTECTÉS / FAILURES DETECTED

Commentaires / Comments:
________________________
________________________
________________________

Signature: _______________
```

### 7.2 Capture de données / Data Capture

- [ ] Screenshots de l'oscilloscope / Oscilloscope screenshots
- [ ] Logs de test / Test logs
- [ ] Photos des mesures / Measurement photos
- [ ] Fichiers de données brutes / Raw data files

## 8. Prochaines étapes / Next Steps

Si tous les tests unitaires passent :
If all unit tests pass:

1. Procéder à la [validation des composants spécifiques](03_Component_Validation.md)
   Proceed to [specific component validation](03_Component_Validation.md)
2. Archiver le rapport de test / Archive test report
3. Mettre à jour le statut du PCB / Update PCB status

Si des tests échouent / If tests fail:
1. Analyser les causes / Analyze causes
2. Effectuer les corrections nécessaires / Make necessary corrections
3. Répéter les tests / Repeat tests
