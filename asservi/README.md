# Module Asservi (Servo Control)

Module d'asservissement pour le contrôle de moteurs et systèmes avec retour d'information.

## Description

Ce module fournit des outils pour implémenter l'asservissement de moteurs et autres systèmes. Il inclut :

- **PIDController** : Un contrôleur PID (Proportionnel-Intégral-Dérivé) complet avec anti-windup
- **Motor** : Une abstraction de moteur avec asservissement intégré

## Caractéristiques

- Contrôleur PID configurable avec gains Kp, Ki, Kd
- Support de l'anti-windup pour éviter la saturation de l'intégrale
- Limitation de la sortie configurable
- Interface simple pour le contrôle de moteurs
- Gestion automatique du pas de temps

## Installation

Le module est autonome et ne nécessite que Python 3.6+.

```python
from asservi import PIDController, Motor
```

## Usage

### Exemple 1 : Utilisation basique du PID

```python
from asservi import PIDController

# Créer un contrôleur PID
pid = PIDController(kp=1.0, ki=0.1, kd=0.05, setpoint=100)

# Définir des limites de sortie
pid.set_output_limits(-100, 100)

# Boucle d'asservissement
measured_value = 0
while abs(pid.setpoint - measured_value) > 0.1:
    # Calculer la commande
    command = pid.update(measured_value)
    
    # Simuler le système (à remplacer par votre code)
    measured_value += command * 0.01
    
    print(f"Mesure: {measured_value:.2f}, Commande: {command:.2f}")
```

### Exemple 2 : Contrôle d'un moteur

```python
from asservi import Motor
import time

# Créer un moteur avec gains PID
motor = Motor(name="Moteur Gauche", kp=1.5, ki=0.2, kd=0.1)

# Définir une position cible
motor.set_target(1000)  # Position en encodeur ticks par exemple

# Boucle de contrôle
for i in range(100):
    # Lire la position actuelle du capteur (à adapter)
    current_position = read_encoder()  # Fonction à implémenter
    motor.update_position(current_position)
    
    # Calculer la puissance à appliquer
    power = motor.compute_power()
    
    # Appliquer la puissance au moteur (à adapter)
    apply_motor_power(power)  # Fonction à implémenter
    
    print(motor)
    time.sleep(0.02)  # 50 Hz
```

### Exemple 3 : Ajustement dynamique des gains

```python
from asservi import Motor

motor = Motor(name="Moteur Test")

# Modifier les gains pendant l'exécution
motor.set_pid_gains(kp=2.0, ki=0.3, kd=0.15)

# Changer la cible
motor.set_target(500)

# Obtenir les composantes du PID pour le débogage
components = motor.pid.get_components()
print(f"Erreur: {components['error']}")
print(f"Intégrale: {components['integral']}")
print(f"Terme P: {components['p_term']}")
print(f"Terme I: {components['i_term']}")
```

## Configuration

Un fichier `config.ini` est fourni avec les paramètres par défaut :

- Gains PID par défaut (Kp, Ki, Kd)
- Limites de puissance des moteurs
- Limites de l'intégrale (anti-windup)
- Fréquence de mise à jour recommandée

## Structure du Module

```
asservi/
├── __init__.py           # Point d'entrée du module
├── pid_controller.py     # Implémentation du contrôleur PID
├── motor.py             # Abstraction de moteur avec PID
├── config.ini           # Configuration par défaut
└── README.md           # Cette documentation
```

## Concepts

### Contrôleur PID

Le contrôleur PID calcule une commande basée sur trois termes :

- **P (Proportionnel)** : Réagit à l'erreur actuelle
- **I (Intégral)** : Corrige l'erreur accumulée dans le temps
- **D (Dérivé)** : Anticipe l'évolution de l'erreur

La sortie est calculée comme : `output = Kp*error + Ki*integral + Kd*derivative`

### Anti-Windup

L'anti-windup limite l'accumulation de l'intégrale pour éviter les dépassements importants et améliorer la stabilité du système.

### Réglage des Gains

Pour régler les gains PID :

1. Commencer avec Ki=0 et Kd=0
2. Augmenter Kp jusqu'à obtenir des oscillations
3. Réduire Kp à 50-70% de cette valeur
4. Augmenter Ki pour réduire l'erreur statique
5. Ajouter du Kd si nécessaire pour réduire les oscillations

## Auteurs

Projet B3 S6 - 2526

## Licence

Projet étudiant
