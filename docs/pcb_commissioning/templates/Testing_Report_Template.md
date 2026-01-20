# Rapport de Test PCB / PCB Test Report

**Date du test / Test Date:** _______________  
**Opérateur / Operator:** _______________  
**PCB S/N:** _______________  
**Version PCB / PCB Version:** _______________  

---

## 1. Informations générales / General Information

**Type de test / Test Type:**
- [ ] Réception / Reception
- [ ] Soudure / Soldering
- [ ] Tests unitaires / Unit Testing
- [ ] Validation composants / Component Validation

**Conditions de test / Test Conditions:**
- Température / Temperature: _____ °C
- Humidité / Humidity: _____ %
- Alimentation utilisée / Power Supply Used: _______________

---

## 2. Tests d'alimentation / Power Tests

### 2.1 Tensions / Voltages

| Rail | Tension nominale / Nominal | Mesurée / Measured | Ondulation / Ripple | Statut / Status |
|------|---------------------------|-------------------|---------------------|-----------------|
| V_in | 12.0V | _____ V | _____ mV_pp | ☐ PASS ☐ FAIL |
| 5V   | 5.0V  | _____ V | _____ mV_pp | ☐ PASS ☐ FAIL |
| 3.3V | 3.3V  | _____ V | _____ mV_pp | ☐ PASS ☐ FAIL |

### 2.2 Courants / Currents

| Condition | Courant / Current | Limite / Limit | Statut / Status |
|-----------|------------------|----------------|-----------------|
| Repos / Idle | _____ mA | < 100 mA | ☐ PASS ☐ FAIL |
| Nominal | _____ mA | < 500 mA | ☐ PASS ☐ FAIL |
| Max | _____ mA | < 1000 mA | ☐ PASS ☐ FAIL |

**Commentaires / Comments:**
_______________________________________________________

---

## 3. Tests de communication / Communication Tests

### 3.1 UART

- [ ] Communication établie / Communication established
- Baud rate: _______________
- Erreurs de trame / Frame errors: _____
- **Statut / Status:** ☐ PASS ☐ FAIL

### 3.2 I2C

- [ ] Bus I2C fonctionnel / I2C bus functional
- Adresses détectées / Addresses detected: _______________
- Fréquence / Frequency: _______________
- **Statut / Status:** ☐ PASS ☐ FAIL

### 3.3 SPI

- [ ] Communication SPI fonctionnelle / SPI communication functional
- Vitesse / Speed: _______________
- Mode: _____
- **Statut / Status:** ☐ PASS ☐ FAIL

**Commentaires / Comments:**
_______________________________________________________

---

## 4. Tests des composants / Component Tests

### 4.1 IMU

| Test | Résultat / Result | Statut / Status |
|------|------------------|-----------------|
| Détection / Detection | WHO_AM_I: 0x___ | ☐ PASS ☐ FAIL |
| Initialisation / Initialization | | ☐ PASS ☐ FAIL |
| Accéléromètre / Accelerometer | X:___ Y:___ Z:___ | ☐ PASS ☐ FAIL |
| Gyroscope | X:___ Y:___ Z:___ | ☐ PASS ☐ FAIL |
| Température / Temperature | _____ °C | ☐ PASS ☐ FAIL |
| Test gravité / Gravity test | | ☐ PASS ☐ FAIL |
| Test rotation / Rotation test | | ☐ PASS ☐ FAIL |

### 4.2 Moteurs / Motors

| Moteur / Motor | Direction avant / Forward | Direction arrière / Backward | Contrôle vitesse / Speed Control | Statut / Status |
|---------------|--------------------------|----------------------------|--------------------------------|-----------------|
| Moteur 1 | ☐ OK | ☐ OK | ☐ OK | ☐ PASS ☐ FAIL |
| Moteur 2 | ☐ OK | ☐ OK | ☐ OK | ☐ PASS ☐ FAIL |

**Courant maximal mesuré / Max measured current:** _____ mA

### 4.3 MCP3208 (ADC)

| Canal / Channel | GND (bits) | VCC (bits) | Statut / Status |
|----------------|-----------|-----------|-----------------|
| 0 | _____ | _____ | ☐ PASS ☐ FAIL |
| 1 | _____ | _____ | ☐ PASS ☐ FAIL |
| 2 | _____ | _____ | ☐ PASS ☐ FAIL |
| 3 | _____ | _____ | ☐ PASS ☐ FAIL |
| 4 | _____ | _____ | ☐ PASS ☐ FAIL |
| 5 | _____ | _____ | ☐ PASS ☐ FAIL |
| 6 | _____ | _____ | ☐ PASS ☐ FAIL |
| 7 | _____ | _____ | ☐ PASS ☐ FAIL |

**Bruit mesuré / Measured noise:** _____ bits RMS

**Commentaires / Comments:**
_______________________________________________________

---

## 5. Tests fonctionnels / Functional Tests

### 5.1 Test de charge / Load Test

- Durée / Duration: _____ minutes
- Température max composants / Max component temperature: _____ °C
- Dérive tension / Voltage drift: _____ mV
- **Statut / Status:** ☐ PASS ☐ FAIL

### 5.2 Test de reset / Reset Test

- [ ] Système redémarre correctement / System restarts correctly
- [ ] États GPIO corrects après reset / GPIO states correct after reset
- **Statut / Status:** ☐ PASS ☐ FAIL

---

## 6. Problèmes identifiés / Identified Issues

| # | Description | Sévérité / Severity | Action requise / Required Action |
|---|-------------|---------------------|--------------------------------|
| 1 | | ☐ Majeur ☐ Mineur / Major Minor | |
| 2 | | ☐ Majeur ☐ Mineur / Major Minor | |
| 3 | | ☐ Majeur ☐ Mineur / Major Minor | |

---

## 7. Résumé / Summary

### 7.1 Résultat global / Overall Result

- [ ] **TOUS LES TESTS RÉUSSIS** / **ALL TESTS PASSED**
  - PCB validé pour mise en service / PCB validated for commissioning
  
- [ ] **TESTS RÉUSSIS AVEC REMARQUES** / **TESTS PASSED WITH NOTES**
  - Problèmes mineurs identifiés / Minor issues identified
  - PCB utilisable avec précautions / PCB usable with precautions
  
- [ ] **ÉCHECS DÉTECTÉS** / **FAILURES DETECTED**
  - Réparations nécessaires / Repairs needed
  - Tests à répéter / Tests to be repeated

### 7.2 Statistiques / Statistics

- Tests effectués / Tests performed: _____
- Tests réussis / Tests passed: _____
- Tests échoués / Tests failed: _____
- Taux de réussite / Success rate: _____ %

---

## 8. Actions de suivi / Follow-up Actions

- [ ] Aucune action nécessaire / No action needed
- [ ] Réparations à effectuer / Repairs to perform
- [ ] Tests supplémentaires requis / Additional tests required
- [ ] Documentation à mettre à jour / Documentation to update
- [ ] Autre / Other: _______________________________

**Détails / Details:**
_______________________________________________________
_______________________________________________________

---

## 9. Pièces jointes / Attachments

- [ ] Photos du PCB / PCB photos
- [ ] Captures oscilloscope / Oscilloscope screenshots
- [ ] Logs de test / Test logs
- [ ] Fichiers de données / Data files

**Liste des fichiers / File list:**
_______________________________________________________

---

## 10. Signatures / Signatures

**Testeur / Tester:** _______________  **Date:** _______________

**Vérificateur / Reviewer:** _______________  **Date:** _______________

**Responsable technique / Technical Manager:** _______________  **Date:** _______________

---

## 11. Notes additionnelles / Additional Notes

_______________________________________________________
_______________________________________________________
_______________________________________________________
_______________________________________________________
