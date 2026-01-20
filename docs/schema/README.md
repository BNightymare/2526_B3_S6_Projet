# Documentation du Schéma du Système
# System Schema Documentation

## À propos / About

Ce dossier contient la documentation complète de l'architecture du système 2526_B3_S6_Projet, incluant les schémas, diagrammes et spécifications techniques.

This folder contains the complete architecture documentation for the 2526_B3_S6_Projet system, including schemas, diagrams, and technical specifications.

## Documents Disponibles / Available Documents

### 1. [SYSTEM_ARCHITECTURE.md](./SYSTEM_ARCHITECTURE.md)
**Architecture Globale du Système / Global System Architecture**

Contient:
- Vue d'ensemble du système en couches (matériel, traitement signal, contrôle, application)
- Diagrammes ASCII de l'architecture
- Description détaillée de chaque composant
- Flux de données
- Cas d'usage
- Spécifications techniques
- Évolutions futures

Contains:
- Layered system overview (hardware, signal processing, control, application)
- ASCII architecture diagrams
- Detailed component descriptions
- Data flow
- Use cases
- Technical specifications
- Future developments

### 2. [COMPONENT_INTERACTIONS.md](./COMPONENT_INTERACTIONS.md)
**Interactions entre Composants / Component Interactions**

Contient:
- Diagrammes de séquence
- Matrice d'interaction des modules
- Interfaces de communication
- Flux de contrôle détaillé
- Protocoles de communication
- Synchronisation et timing
- Points d'extension

Contains:
- Sequence diagrams
- Module interaction matrix
- Communication interfaces
- Detailed control flow
- Communication protocols
- Synchronization and timing
- Extension points

## Structure du Projet / Project Structure

```
2526_B3_S6_Projet/
│
├── hardware/              # Composants matériels / Hardware components
│   └── pcb/              # Conception PCB / PCB design
│       ├── schematic/    # Schématiques / Schematics
│       ├── layout/       # Layout PCB
│       ├── gerbers/      # Fichiers fabrication / Manufacturing files
│       └── bom/          # Liste composants / Bill of materials
│
├── src/                  # Code source Python / Python source code
│   ├── __init__.py
│   └── main.py           # Point d'entrée / Entry point
│
├── filtrage/             # Module de filtrage / Filtering module
│   ├── filters.py        # Filtres numériques / Digital filters
│   ├── test_filters.py   # Tests unitaires / Unit tests
│   └── example.py        # Exemples / Examples
│
├── asservi/              # Module d'asservissement / Servo control
│   ├── pid_controller.py # Contrôleur PID / PID controller
│   ├── motor.py          # Interface moteur / Motor interface
│   └── config.ini        # Configuration
│
├── docs/                 # Documentation
│   ├── schema/           # Schémas d'architecture / Architecture schemas
│   └── PCB_DESIGN_GUIDELINES.md
│
└── tests/                # Tests / Tests
```

## Guide de Lecture / Reading Guide

### Pour les Développeurs / For Developers
1. Commencer par `SYSTEM_ARCHITECTURE.md` pour comprendre la vue d'ensemble
2. Lire `COMPONENT_INTERACTIONS.md` pour les détails d'implémentation
3. Consulter les README des modules individuels pour l'API

1. Start with `SYSTEM_ARCHITECTURE.md` for the big picture
2. Read `COMPONENT_INTERACTIONS.md` for implementation details
3. Refer to individual module READMEs for API details

### Pour les Concepteurs Hardware / For Hardware Designers
1. Section "Hardware Layer" dans `SYSTEM_ARCHITECTURE.md`
2. Consulter `docs/PCB_DESIGN_GUIDELINES.md`
3. Explorer `hardware/pcb/` pour les fichiers de conception

1. "Hardware Layer" section in `SYSTEM_ARCHITECTURE.md`
2. Refer to `docs/PCB_DESIGN_GUIDELINES.md`
3. Explore `hardware/pcb/` for design files

### Pour les Intégrateurs / For System Integrators
1. "Configuration et Intégration" dans `SYSTEM_ARCHITECTURE.md`
2. "Interfaces de Communication" dans `COMPONENT_INTERACTIONS.md`
3. Exemples de code dans chaque module

1. "Configuration and Integration" in `SYSTEM_ARCHITECTURE.md`
2. "Communication Interfaces" in `COMPONENT_INTERACTIONS.md`
3. Code examples in each module

## Légende des Diagrammes / Diagram Legend

```
┌────┐
│Box │  = Composant / Component
└────┘

  │
  ▼     = Flux de données unidirectionnel / Unidirectional data flow

  ├──▶  = Flux avec branchement / Flow with branching

 ─────  = Connexion / Connection

[text]  = Note ou commentaire / Note or comment
```

## Modules du Système / System Modules

### 1. Hardware / Matériel
- **PCB**: Carte électronique principale
- **Capteurs**: Acquisition de données physiques
- **Actuateurs**: Exécution des actions

### 2. Traitement du Signal / Signal Processing
- **Filtrage**: Nettoyage et extraction de signaux
  - Passe-bas, passe-haut, passe-bande
  - Moyenne mobile

### 3. Contrôle / Control
- **Asservissement**: Boucles de régulation
  - Contrôleur PID
  - Interface moteur

### 4. Application / Application
- **Python**: Logiciel de supervision
  - Interface utilisateur
  - Configuration
  - Monitoring

## Workflow Typique / Typical Workflow

```
[Capteur] → [Filtrage] → [Asservissement] → [Actuateur]
                                ↓
                          [Application]
                          - Configuration
                          - Monitoring
                          - Logging
```

## Considérations de Conception / Design Considerations

### Performance
- Latence totale: < 10ms
- Fréquence d'échantillonnage: 100-1000 Hz
- Stabilité: Temps de réponse < 1s

### Robustesse
- Gestion d'erreurs à tous les niveaux
- Modes de sécurité
- Validation des entrées

### Extensibilité
- Architecture modulaire
- Interfaces standardisées
- Points d'extension documentés

## Contribuer / Contributing

Pour proposer des modifications à l'architecture:
1. Créer une issue décrivant la modification
2. Mettre à jour les documents concernés
3. Soumettre une pull request

To propose architecture changes:
1. Create an issue describing the change
2. Update relevant documents
3. Submit a pull request

## Support et Questions / Support and Questions

Pour toute question sur l'architecture du système, consulter:
- Les documents dans ce dossier
- Les README des modules individuels
- Les issues GitHub du projet

For questions about system architecture, refer to:
- Documents in this folder
- Individual module READMEs
- Project GitHub issues

## Versions / Versions

- v1.0 (2026-01): Architecture initiale / Initial architecture
  - Modules: PCB, Python, Filtrage, Asservissement
  - Documentation complète des interactions
  - Spécifications techniques

## Références / References

### Documentation Externe / External Documentation
- [KiCad PCB Design](https://www.kicad.org/)
- [Python Documentation](https://docs.python.org/3/)
- [PID Control Theory](https://en.wikipedia.org/wiki/PID_controller)
- [Digital Signal Processing](https://en.wikipedia.org/wiki/Digital_signal_processing)

### Normes et Standards / Standards
- IEC 61131-3: Programmable controllers
- ISO 9001: Quality management
- RoHS: Restriction of Hazardous Substances
