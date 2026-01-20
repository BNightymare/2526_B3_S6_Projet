# 2526_B3_S6_Projet

Projet de troisième année - Semestre 6 (2025-2026)

## Modules

### Asservi (Servo Control)

Module d'asservissement pour le contrôle de moteurs et systèmes avec retour d'information.

- Contrôleur PID complet avec anti-windup
- Interface de contrôle de moteurs
- Exemples d'utilisation
- Documentation détaillée

Voir [asservi/README.md](asservi/README.md) pour plus de détails.

## Structure du Projet

```
.
├── asservi/              # Module d'asservissement (PID, contrôle moteur)
│   ├── __init__.py
│   ├── pid_controller.py
│   ├── motor.py
│   ├── config.ini
│   ├── example_pid.py
│   ├── example_motor.py
│   └── README.md
└── README.md
```

## Installation

Le projet nécessite Python 3.6 ou supérieur.

```bash
# Cloner le dépôt
git clone https://github.com/BNightymare/2526_B3_S6_Projet.git
cd 2526_B3_S6_Projet

# Tester le module asservi
python3 asservi/example_pid.py
python3 asservi/example_motor.py
```

## Auteurs

- BNightymare
- Samirtaza
- Lucie913