# Diagramme d'Interaction des Composants
# Component Interaction Diagram

## Vue d'ensemble / Overview

Ce document détaille les interactions entre les différents composants du système.

This document details the interactions between the different system components.

## Diagramme de Séquence - Boucle de Contrôle
## Sequence Diagram - Control Loop

```
Capteur    ADC    Filtrage    Asservi    Moteur    
  │         │         │          │         │
  │ Lecture │         │          │         │
  ├────────▶│         │          │         │
  │         │ Signal  │          │         │
  │         ├────────▶│          │         │
  │         │         │ Filtré   │         │
  │         │         ├─────────▶│         │
  │         │         │          │ Calcul  │
  │         │         │          │ PID     │
  │         │         │          ├────────▶│
  │         │         │          │         │ Action
  │         │         │          │◀────────┤
  │         │         │          │ Feedback│
  │         │         │◀─────────┤         │
  │         │◀────────┤          │         │
  │◀────────┤         │          │         │
  │         │         │          │         │
```

## Matrice d'Interaction des Modules
## Module Interaction Matrix

| Module Source     | Module Destination | Type d'Interaction | Données Échangées       |
|-------------------|--------------------|--------------------|-------------------------|
| PCB/Capteurs      | Filtrage           | Signal analogique  | Tension, Courant        |
| Filtrage          | Asservissement     | Signal numérique   | Valeurs filtrées        |
| Asservissement    | PCB/Moteurs        | Commande PWM       | Duty cycle, Direction   |
| Application Python| Tous modules       | Configuration      | Paramètres, Consignes   |
| Tous modules      | Application Python | Monitoring         | État, Métriques         |

## Interfaces de Communication
## Communication Interfaces

### 1. Interface Capteur → Filtrage
```python
class SensorInterface:
    """
    Interface pour la lecture des capteurs
    Interface for sensor reading
    """
    def read_sensor(self) -> float:
        """Lit la valeur du capteur / Reads sensor value"""
        pass
    
    def get_sample_rate(self) -> int:
        """Retourne la fréquence d'échantillonnage / Returns sampling rate"""
        pass
```

### 2. Interface Filtrage → Asservissement
```python
class FilterInterface:
    """
    Interface pour le filtrage des signaux
    Interface for signal filtering
    """
    def filter(self, signal: float) -> float:
        """Filtre un échantillon / Filters a sample"""
        pass
    
    def reset(self) -> None:
        """Réinitialise l'état du filtre / Resets filter state"""
        pass
```

### 3. Interface Asservissement → Actuateur
```python
class ActuatorInterface:
    """
    Interface pour le contrôle des actuateurs
    Interface for actuator control
    """
    def set_command(self, value: float) -> None:
        """Envoie une commande / Sends a command"""
        pass
    
    def get_feedback(self) -> float:
        """Lit le retour d'information / Reads feedback"""
        pass
```

## Flux de Contrôle Détaillé
## Detailed Control Flow

### Initialisation du Système / System Initialization
```
1. Chargement configuration / Load configuration
   ├─▶ Lecture fichiers config / Read config files
   ├─▶ Validation paramètres / Validate parameters
   └─▶ Initialisation modules / Initialize modules

2. Test des interfaces / Interface testing
   ├─▶ Vérification capteurs / Check sensors
   ├─▶ Vérification actuateurs / Check actuators
   └─▶ Test communication / Test communication

3. Calibration / Calibration
   ├─▶ Zéro des capteurs / Zero sensors
   ├─▶ Limites actuateurs / Actuator limits
   └─▶ Ajustement filtres / Adjust filters

4. Démarrage boucle principale / Start main loop
```

### Boucle Principale / Main Loop
```python
def main_control_loop():
    """
    Boucle de contrôle principale
    Main control loop
    """
    # Initialisation
    sensor = initialize_sensor()
    lpf = LowPassFilter(cutoff_freq=10, sample_rate=100)
    pid = PIDController(kp=1.0, ki=0.1, kd=0.05)
    motor = Motor(pid_controller=pid)
    
    # Paramètres
    setpoint = 100.0  # Consigne / Setpoint
    dt = 0.01  # Période d'échantillonnage / Sampling period (10ms)
    
    # Boucle infinie
    while True:
        # 1. Acquisition
        raw_value = sensor.read()
        
        # 2. Filtrage
        filtered_value = lpf.filter(raw_value)
        
        # 3. Calcul erreur
        error = setpoint - filtered_value
        
        # 4. Calcul commande PID
        command = pid.compute(error, dt)
        
        # 5. Application commande
        motor.set_speed(command)
        
        # 6. Logging (optionnel)
        log_data(raw_value, filtered_value, command)
        
        # 7. Attente
        sleep(dt)
```

### Gestion des Erreurs / Error Handling
```
Détection Erreur / Error Detection
├─▶ Capteur hors limites / Sensor out of range
│   └─▶ Mode sécurité / Safety mode
├─▶ Timeout communication / Communication timeout
│   └─▶ Arrêt actuateurs / Stop actuators
├─▶ Erreur calcul / Computation error
│   └─▶ Valeur par défaut / Default value
└─▶ Limite atteinte / Limit reached
    └─▶ Saturation / Saturation
```

## Dépendances entre Modules
## Module Dependencies

```
Application Python
    │
    ├─▶ Module Asservissement
    │   ├─▶ PID Controller
    │   └─▶ Motor Interface
    │
    ├─▶ Module Filtrage
    │   ├─▶ Low-pass Filter
    │   ├─▶ High-pass Filter
    │   ├─▶ Band-pass Filter
    │   └─▶ Moving Average
    │
    └─▶ Hardware PCB
        ├─▶ Capteurs / Sensors
        └─▶ Actuateurs / Actuators
```

## Protocoles de Communication
## Communication Protocols

### I2C (Inter-Integrated Circuit)
- **Usage**: Communication avec capteurs
- **Vitesse**: 100-400 kHz
- **Configuration**: Mode Master

### SPI (Serial Peripheral Interface)
- **Usage**: Communication haute vitesse
- **Vitesse**: 1-10 MHz
- **Configuration**: Mode Master, CPOL=0, CPHA=0

### UART (Universal Asynchronous Receiver-Transmitter)
- **Usage**: Debug et monitoring
- **Vitesse**: 115200 baud
- **Configuration**: 8N1 (8 bits, No parity, 1 stop bit)

### PWM (Pulse Width Modulation)
- **Usage**: Contrôle moteurs
- **Fréquence**: 1-20 kHz
- **Résolution**: 8-10 bits

## Synchronisation et Timing
## Synchronization and Timing

### Fréquences d'Échantillonnage / Sampling Frequencies
```
Capteur rapide (position):     1000 Hz
Capteur lent (température):     10 Hz
Filtrage:                      100 Hz
Boucle PID:                    100 Hz
Logging:                        10 Hz
Interface utilisateur:          1 Hz
```

### Latences Typiques / Typical Latencies
```
Lecture capteur:              < 1 ms
Filtrage:                     < 0.1 ms
Calcul PID:                   < 0.5 ms
Commande actuateur:           < 1 ms
───────────────────────────────────────
Latence totale:               < 3 ms
```

## Diagramme de Déploiement
## Deployment Diagram

```
┌─────────────────────────────────────────┐
│         Microcontrôleur / MCU            │
│  ┌──────────────────────────────────┐   │
│  │  Firmware embarqué / Embedded FW │   │
│  │  • Acquisition ADC               │   │
│  │  • PWM Control                   │   │
│  │  • Communication                 │   │
│  └──────────────────────────────────┘   │
│                 │                        │
└─────────────────┼────────────────────────┘
                  │ USB/UART
                  │
┌─────────────────▼────────────────────────┐
│      Ordinateur / Computer               │
│  ┌──────────────────────────────────┐   │
│  │  Application Python              │   │
│  │  • Filtrage avancé               │   │
│  │  • Contrôle PID                  │   │
│  │  • Interface utilisateur         │   │
│  │  • Logging et analyse            │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

## Points d'Extension / Extension Points

### 1. Ajout d'un Nouveau Capteur / Adding a New Sensor
```python
from sensor_interface import SensorInterface

class NewSensor(SensorInterface):
    def __init__(self, config):
        # Configuration spécifique
        pass
    
    def read_sensor(self):
        # Implémentation de lecture
        pass
```

### 2. Ajout d'un Nouveau Filtre / Adding a New Filter
```python
from filtrage.base import FilterBase

class NewFilter(FilterBase):
    def __init__(self, params):
        # Paramètres du filtre
        pass
    
    def filter(self, signal):
        # Algorithme de filtrage
        pass
```

### 3. Ajout d'un Contrôleur Personnalisé / Adding a Custom Controller
```python
from asservi.controller_base import ControllerBase

class CustomController(ControllerBase):
    def compute(self, error, dt):
        # Algorithme de contrôle
        pass
```

## Considérations de Performance
## Performance Considerations

### Optimisations Recommandées / Recommended Optimizations
1. **Bufferisation**: Utiliser des buffers circulaires pour les filtres
2. **Pré-calcul**: Calculer les coefficients de filtres une fois
3. **Entiers fixes**: Utiliser des entiers pour calculs temps réel sur MCU
4. **Batch processing**: Traiter plusieurs échantillons à la fois si possible

### Métriques de Performance / Performance Metrics
- **CPU Usage**: < 50% du temps disponible
- **Memory Usage**: < 80% de la RAM disponible
- **Jitter**: < 1ms pour la boucle de contrôle
- **Throughput**: Capacité de traiter 1000 échantillons/seconde

## Références / References
- SYSTEM_ARCHITECTURE.md - Architecture globale
- Spécifications des modules individuels dans leurs README respectifs
