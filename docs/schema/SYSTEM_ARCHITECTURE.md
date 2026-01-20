# Schéma d'Architecture du Système
# System Architecture Schema

## Vue d'ensemble / Overview

Ce document décrit l'architecture complète du système 2526_B3_S6_Projet, incluant les composants matériels, logiciels et leurs interactions.

This document describes the complete architecture of the 2526_B3_S6_Projet system, including hardware components, software components, and their interactions.

## Architecture Globale / Global Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Système 2526_B3_S6_Projet                        │
│                  2526_B3_S6_Projet System                           │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                        COUCHE MATÉRIELLE                             │
│                        HARDWARE LAYER                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐     │
│  │     PCB      │─────▶│   Capteurs   │─────▶│  Moteurs/    │     │
│  │   Circuit    │      │   Sensors    │      │  Actuateurs  │     │
│  │   Imprimé    │      │              │      │  Motors/     │     │
│  └──────────────┘      └──────────────┘      │  Actuators   │     │
│         │                     │               └──────────────┘     │
│         │                     │                      ▲              │
│         ▼                     ▼                      │              │
│  ┌──────────────────────────────────────────────────┘              │
│  │         Interface Électronique / Electronic Interface           │
│  └─────────────────────────────────────────────────────────────────┤
│                                                                      │
└──────────────────────────────────────────┬───────────────────────────┘
                                           │
                                           │ Signal analogique/numérique
                                           │ Analog/Digital signals
                                           │
┌──────────────────────────────────────────▼───────────────────────────┐
│                    COUCHE TRAITEMENT DU SIGNAL                       │
│                    SIGNAL PROCESSING LAYER                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Acquisition ──▶ Filtrage ──▶ Transmission ──▶ Traitement          │
│  Acquisition    Filtering     Transmission     Processing            │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Module Filtrage (filtrage/)                                │   │
│  │  • Filtre passe-bas  / Low-pass filter                      │   │
│  │  • Filtre passe-haut / High-pass filter                     │   │
│  │  • Filtre passe-bande / Band-pass filter                    │   │
│  │  • Moyenne mobile / Moving average                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
└──────────────────────────────────────────┬───────────────────────────┘
                                           │
                                           │ Signal filtré
                                           │ Filtered signal
                                           │
┌──────────────────────────────────────────▼───────────────────────────┐
│                     COUCHE CONTRÔLE / CONTROL LAYER                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Module Asservissement (asservi/)                           │   │
│  │  • Contrôleur PID / PID Controller                          │   │
│  │  • Interface moteur / Motor interface                       │   │
│  │  • Gestion des consignes / Setpoint management             │   │
│  │  • Boucle de rétroaction / Feedback loop                   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                          │                                           │
│                          ▼                                           │
│            Commandes moteur / Motor commands                        │
│                                                                      │
└──────────────────────────────────────────┬───────────────────────────┘
                                           │
                                           │ Commandes de contrôle
                                           │ Control commands
                                           │
┌──────────────────────────────────────────▼───────────────────────────┐
│                   COUCHE APPLICATION / APPLICATION LAYER             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Application Python (src/)                                   │   │
│  │  • Interface utilisateur / User interface                    │   │
│  │  • Gestion des configurations / Configuration management    │   │
│  │  • Logging et monitoring / Logging and monitoring           │   │
│  │  • Orchestration des modules / Module orchestration         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Flux de Données / Data Flow

```
┌──────────┐
│ Capteur  │ Mesure physique (température, position, etc.)
│ Sensor   │ Physical measurement (temperature, position, etc.)
└────┬─────┘
     │
     ▼
┌──────────────────┐
│ Acquisition ADC  │ Conversion analogique → numérique
│ ADC Acquisition  │ Analog → digital conversion
└────┬─────────────┘
     │ Signal brut / Raw signal
     ▼
┌──────────────────┐
│ Filtrage         │ Élimination du bruit, extraction de bande
│ Filtering        │ Noise removal, band extraction
└────┬─────────────┘
     │ Signal filtré / Filtered signal
     ▼
┌──────────────────┐
│ Transmission     │ Communication vers le contrôleur
│ Transmission     │ Communication to controller
└────┬─────────────┘
     │ Signal transmis / Transmitted signal
     ▼
┌──────────────────┐
│ Asservissement   │ Calcul de la commande (PID)
│ Servo Control    │ Command calculation (PID)
└────┬─────────────┘
     │ Commande / Command
     ▼
┌──────────────────┐
│ Actionneur       │ Exécution de l'action
│ Actuator         │ Action execution
└──────────────────┘
```

## Composants Détaillés / Detailed Components

### 1. Hardware (Matériel)

#### PCB (hardware/pcb/)
- **Schématique**: Conception du circuit électronique
- **Layout**: Disposition des composants
- **Gerbers**: Fichiers de fabrication
- **BOM**: Liste des composants

**Rôle**: Infrastructure électronique pour connecter capteurs, microcontrôleur et actionneurs.

### 2. Signal Processing (Traitement du Signal)

#### Module Filtrage (filtrage/)
```python
filtrage/
├── __init__.py
├── filters.py          # Implémentation des filtres
├── test_filters.py     # Tests unitaires
└── example.py          # Exemples d'utilisation
```

**Fonctionnalités**:
- Filtre passe-bas: Élimine les hautes fréquences (bruit)
- Filtre passe-haut: Élimine les basses fréquences (dérive)
- Filtre passe-bande: Extrait une bande de fréquences
- Moyenne mobile: Lissage du signal

**Application**: Nettoyer les signaux des capteurs avant traitement.

### 3. Control (Contrôle)

#### Module Asservissement (asservi/)
```python
asservi/
├── __init__.py
├── pid_controller.py   # Contrôleur PID
├── motor.py            # Interface moteur
├── config.ini          # Configuration
└── examples/           # Exemples d'utilisation
```

**Fonctionnalités**:
- Contrôleur PID avec anti-windup
- Interface moteur abstraite
- Gestion des consignes (setpoints)
- Boucle de rétroaction

**Application**: Maintenir une position, vitesse ou température à une valeur cible.

### 4. Application Software (Logiciel d'Application)

#### Application Python (src/)
```python
src/
├── __init__.py
├── main.py            # Point d'entrée
└── modules/           # Modules additionnels
```

**Rôle**: Coordonner tous les modules, gérer l'interface utilisateur et la configuration système.

## Cas d'Usage / Use Cases

### Cas 1: Contrôle de Position
```
1. Capteur de position → mesure → signal analogique
2. ADC → conversion → signal numérique
3. Filtrage → élimination bruit → signal propre
4. PID → calcul erreur → commande moteur
5. Moteur → ajustement position
6. Boucle de retour vers étape 1
```

### Cas 2: Traitement de Signal Audio/Vibration
```
1. Capteur (micro/accéléromètre) → signal brut
2. Filtrage passe-bande → extraction fréquence d'intérêt
3. Analyse → détection d'anomalies
4. Action → alerte ou compensation
```

## Configuration et Intégration / Configuration and Integration

### 1. Configuration Matérielle / Hardware Configuration
- Connexions PCB selon schématique
- Calibration des capteurs
- Test des interfaces

### 2. Configuration Logicielle / Software Configuration
- Installation des dépendances Python (`requirements.txt`)
- Configuration des paramètres PID (`asservi/config.ini`)
- Configuration des filtres (fréquences de coupure)

### 3. Intégration / Integration
```python
# Exemple d'intégration complète
from filtrage.filters import LowPassFilter
from asservi.pid_controller import PIDController
from asservi.motor import Motor

# Configuration
lpf = LowPassFilter(cutoff_freq=10, sample_rate=100)
pid = PIDController(kp=1.0, ki=0.1, kd=0.05)
motor = Motor(pid_controller=pid)

# Boucle de contrôle
while True:
    raw_signal = read_sensor()
    filtered_signal = lpf.filter(raw_signal)
    motor.update(filtered_signal)
```

## Spécifications Techniques / Technical Specifications

### Hardware
- Tension d'alimentation: 5V-12V (à définir selon PCB)
- Interfaces: I2C, SPI, UART
- Fréquence d'échantillonnage: 100-1000 Hz

### Software
- Langage: Python 3.7+
- Fréquence de boucle de contrôle: 10-100 Hz
- Filtres: Ordre 1-2, configurables

### Performance
- Latence: < 10ms
- Précision de contrôle: ±1% (selon calibration)
- Stabilité: Temps de réponse < 1s

## Évolutions Futures / Future Developments

1. **Routage** (Issue #15): Optimisation du routage des signaux sur PCB
2. **Rendu Final** (Issue #11): Interface de visualisation et reporting
3. **Transmission du Signal** (Issue #7): Protocoles de communication robustes
4. **Monitoring**: Dashboard temps réel
5. **Calibration automatique**: Auto-tuning du PID
6. **Machine Learning**: Prédiction et optimisation adaptative

## Références / References

- Documentation PCB: `docs/PCB_DESIGN_GUIDELINES.md`
- Module Filtrage: `filtrage/README.md`
- Module Asservissement: `asservi/README.md`
- Application Python: `src/`

## Contact et Support

Pour questions ou contributions, consulter le README principal du projet.
