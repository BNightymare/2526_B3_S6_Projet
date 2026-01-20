# 2526_B3_S6_Projet

## Description

Projet de Bachelor 3, Semestre 6 - Système embarqué de contrôle et traitement du signal.

Bachelor Year 3, Semester 6 Project - Embedded control and signal processing system.

## Architecture du Système / System Architecture

📋 **[Voir la documentation complète de l'architecture](docs/schema/README.md)** / **[See complete architecture documentation](docs/schema/README.md)**

Le système est composé de quatre couches principales :

The system consists of four main layers:

1. **Couche Matérielle** / **Hardware Layer**: PCB, capteurs, actuateurs
2. **Traitement du Signal** / **Signal Processing**: Filtrage numérique
3. **Contrôle** / **Control**: Asservissement PID
4. **Application** / **Application**: Logiciel Python de supervision

```
[Capteurs] → [Filtrage] → [Asservissement PID] → [Actuateurs]
                                  ↓
                          [Application Python]
```

## Modules du Projet / Project Modules

### Hardware / Matériel
- **PCB**: Conception de la carte électronique principale
  - Voir `hardware/pcb/` pour les fichiers de conception
  - Documentation: `docs/PCB_DESIGN_GUIDELINES.md`

### Software / Logiciel

#### Module Filtrage (Signal Processing)
- **Emplacement**: `filtrage/`
- **Fonctionnalités**:
  - Filtres passe-bas, passe-haut, passe-bande
  - Moyenne mobile
  - Tests et exemples inclus

#### Module Asservissement (Servo Control)
- **Emplacement**: `asservi/`
- **Fonctionnalités**:
  - Contrôleur PID avec anti-windup
  - Interface moteur abstraite
  - Configuration paramétrable

#### Application Python
- **Emplacement**: `src/`
- **Rôle**: Coordination des modules, interface utilisateur, monitoring

## Installation / Setup

### Prérequis / Prerequisites
- Python 3.7+
- Git

### Installation des dépendances / Dependency Installation
```bash
pip install -r requirements.txt
```

## Utilisation / Usage

### Lancement de l'application / Starting the Application
```bash
python src/main.py
```

### Exemples / Examples

#### Exemple de Filtrage / Filtering Example
```bash
python filtrage/example.py
```

#### Exemple d'Asservissement / Servo Control Example
```bash
python asservi/example_pid.py
python asservi/example_motor.py
```

## Documentation

- 📐 **[Architecture Système](docs/schema/SYSTEM_ARCHITECTURE.md)**: Vue d'ensemble complète
- 🔗 **[Interactions Composants](docs/schema/COMPONENT_INTERACTIONS.md)**: Détails d'implémentation
- 🔧 **[Guidelines PCB](docs/PCB_DESIGN_GUIDELINES.md)**: Conception hardware
- 📦 **[README Filtrage](filtrage/README.md)**: Module de filtrage
- ⚙️ **[README Asservissement](asservi/README.md)**: Module de contrôle

## Structure du Projet / Project Structure

```
2526_B3_S6_Projet/
├── hardware/pcb/         # Conception PCB / PCB design
├── src/                  # Application Python / Python application
├── filtrage/             # Module filtrage / Filtering module
├── asservi/              # Module asservissement / Servo control module
├── docs/                 # Documentation
│   └── schema/           # Schémas d'architecture / Architecture schemas
├── tests/                # Tests
├── requirements.txt      # Dépendances Python / Python dependencies
└── README.md             # Ce fichier / This file
```

## Développement / Development

### Tests
```bash
# Tests du module de filtrage
python -m pytest filtrage/test_filters.py

# Tests de l'application
python -m pytest tests/
```

### Contribution
Les contributions sont les bienvenues ! Veuillez :
1. Créer une issue pour discuter des modifications
2. Fork le projet
3. Créer une branche pour vos modifications
4. Soumettre une pull request

Contributions are welcome! Please:
1. Create an issue to discuss changes
2. Fork the project
3. Create a branch for your changes
4. Submit a pull request

## Issues et Tâches / Issues and Tasks

Voir le [tracker d'issues GitHub](https://github.com/BNightymare/2526_B3_S6_Projet/issues) pour :
- PCB (Issue #1)
- Python (Issue #3)
- Asservissement (Issue #5)
- Transmission du signal (Issue #7)
- Filtrage (Issue #8)
- Schéma (Issue #13) - ✅ Complété
- Routage (Issue #15)

## Licence / License

Projet académique - B3 S6 / Academic project - B3 S6

## Contact

Pour toute question, consulter les issues GitHub ou la documentation du projet.

For any questions, refer to GitHub issues or project documentation.