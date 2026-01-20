# 2526_B3_S6_Projet

**Projet Intégré B3 - Semestre 6 (2025-2026)**

Projet de système embarqué intégrant hardware (PCB) et software (contrôle, filtrage, traitement de signal).

## 📋 Description

Ce projet combine plusieurs composants pour créer un système embarqué complet :
- **Hardware** : Conception de circuits PCB
- **Software** : Modules Python pour le contrôle et le traitement de signal
- **Asservissement** : Contrôle PID pour moteurs
- **Filtrage** : Traitement numérique du signal

## 🗂️ Structure du Projet

```
2526_B3_S6_Projet/
├── hardware/                 # Composants hardware
│   └── pcb/                 # Conception PCB
│       ├── schematic/       # Schémas électriques
│       ├── layout/          # Layout PCB
│       ├── gerbers/         # Fichiers de fabrication
│       └── bom/             # Liste des composants
│
├── asservi/                 # Module d'asservissement (PID)
│   ├── pid_controller.py   # Contrôleur PID
│   ├── motor.py            # Interface moteur
│   ├── example_pid.py      # Exemples PID
│   ├── example_motor.py    # Exemples moteur
│   └── README.md           # Documentation
│
├── filtrage/                # Module de filtrage de signal
│   ├── filters.py          # Filtres numériques
│   ├── example.py          # Exemples d'utilisation
│   ├── test_filters.py     # Tests
│   └── README.md           # Documentation
│
├── src/                     # Code source principal
│   ├── main.py             # Point d'entrée
│   └── __init__.py
│
├── tests/                   # Tests unitaires
│   ├── test_main.py
│   └── __init__.py
│
├── docs/                    # Documentation
│   └── PCB_DESIGN_GUIDELINES.md
│
├── requirements.txt         # Dépendances Python
├── setup.py                # Configuration du package
└── README.md               # Ce fichier
```

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur
- Git

### Installation du projet

1. Cloner le dépôt :
```bash
git clone https://github.com/BNightymare/2526_B3_S6_Projet.git
cd 2526_B3_S6_Projet
```

2. Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

3. Installer le package en mode développement (optionnel) :
```bash
pip install -e .
```

## 📖 Utilisation

### Application Principale

Exécuter le script principal :
```bash
python src/main.py
```

### Module Asservi (Servo Control)

Module pour l'asservissement PID de moteurs avec retour d'information.

**Exemple basique :**
```python
from asservi import PIDController, Motor

# Créer un contrôleur PID
pid = PIDController(kp=1.0, ki=0.1, kd=0.05, setpoint=100)
pid.set_output_limits(-100, 100)

# Créer un moteur
motor = Motor(name="Moteur Principal", kp=1.5, ki=0.2, kd=0.1)
motor.set_target(1000)
```

**Documentation complète :** [asservi/README.md](asservi/README.md)

**Exemples :**
```bash
python asservi/example_pid.py
python asservi/example_motor.py
```

### Module Filtrage (Signal Filtering)

Module de filtrage numérique pour le traitement de signaux.

**Filtres disponibles :**
- `MovingAverageFilter` - Moyenne mobile
- `LowPassFilter` - Passe-bas
- `HighPassFilter` - Passe-haut
- `BandPassFilter` - Passe-bande

**Exemple :**
```python
from filtrage import LowPassFilter

lpf = LowPassFilter(alpha=0.3)
filtered_value = lpf.filter(sensor_reading)
```

**Documentation complète :** [filtrage/README.md](filtrage/README.md)

**Exemples et tests :**
```bash
python filtrage/example.py
python filtrage/test_filters.py
```

### Hardware PCB

Fichiers de conception PCB et documentation pour la partie hardware du projet.

**Répertoires :**
- `hardware/pcb/schematic/` - Schémas électriques
- `hardware/pcb/layout/` - Layout du PCB
- `hardware/pcb/gerbers/` - Fichiers Gerber pour fabrication
- `hardware/pcb/bom/` - Bill of Materials

**Documentation :** [hardware/pcb/README.md](hardware/pcb/README.md)

## 🧪 Tests

Exécuter les tests :

```bash
# Tests du module principal
python tests/test_main.py

# Tests du module filtrage
python filtrage/test_filters.py
```

## 📚 Documentation

- [PCB Design Guidelines](docs/PCB_DESIGN_GUIDELINES.md) - Règles de conception PCB
- [Asservi Module](asservi/README.md) - Documentation du module d'asservissement
- [Filtrage Module](filtrage/README.md) - Documentation du module de filtrage
- [PCB Hardware](hardware/pcb/README.md) - Documentation hardware

## 🏗️ Développement

### Structure des modules

Chaque module (asservi, filtrage) est autonome et peut être utilisé indépendamment :

```python
# Import depuis le module asservi
from asservi import PIDController, Motor

# Import depuis le module filtrage
from filtrage import LowPassFilter, HighPassFilter
```

### Ajouter de nouveaux modules

1. Créer un nouveau répertoire pour votre module
2. Ajouter un fichier `__init__.py`
3. Ajouter un fichier `README.md` avec la documentation
4. Mettre à jour ce README principal

## 👥 Contributeurs

- **BNightymare** - Chef de projet
- **Samirtaza** - Développement
- **Lucie913** - Développement

Pour contribuer au projet, consultez [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Licence

Projet académique B3 S6 (2025-2026) - Licence MIT

Voir [LICENSE](LICENSE) pour plus de détails.

## 🎓 Contexte Académique

Projet réalisé dans le cadre du cours de systèmes embarqués du semestre 6 de Bachelor 3.

**Objectifs du projet :**
- Conception de circuits PCB
- Implémentation d'algorithmes de contrôle (PID)
- Traitement numérique du signal
- Intégration hardware/software
- Documentation technique complète