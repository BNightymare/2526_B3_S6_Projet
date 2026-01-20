# Mise en Service du PCB / PCB Commissioning

Ce document décrit les procédures de mise en service du PCB pour le projet 2526_B3_S6.

This document describes the PCB commissioning procedures for the 2526_B3_S6 project.

## Vue d'ensemble / Overview

La mise en service du PCB est un processus critique qui garantit que la carte électronique fonctionne correctement avant son intégration dans le système final. Ce processus comprend plusieurs étapes clés :

The PCB commissioning is a critical process that ensures the electronic board functions correctly before integration into the final system. This process includes several key stages:

### Étapes de mise en service / Commissioning Stages

1. **Réception et inspection du PCB** / **PCB Reception and Inspection**
   - Inspection visuelle / Visual inspection
   - Vérification des dimensions / Dimension verification
   - Contrôle qualité / Quality control

2. **Soudure des composants** / **Component Soldering**
   - Préparation des composants / Component preparation
   - Procédures de soudure / Soldering procedures
   - Inspection post-soudure / Post-soldering inspection

3. **Tests unitaires des fonctions matérielles** / **Hardware Unit Testing**
   - Tests d'alimentation / Power supply tests
   - Tests de communication / Communication tests
   - Tests des interfaces I/O / I/O interface tests

4. **Validation des composants spécifiques** / **Specific Component Validation**
   - Validation IMU / IMU validation
   - Validation des moteurs / Motor validation
   - Validation MCP3208 (ADC) / MCP3208 (ADC) validation

## Documentation

### Documents de procédure / Procedure Documents

- [01_PCB_Reception_Soldering.md](01_PCB_Reception_Soldering.md) - Procédures de réception et soudure
- [02_Hardware_Unit_Testing.md](02_Hardware_Unit_Testing.md) - Tests unitaires matériels
- [03_Component_Validation.md](03_Component_Validation.md) - Validation des composants

### Formulaires et checklists / Forms and Checklists

- [Reception_Checklist.md](checklists/Reception_Checklist.md) - Checklist de réception
- [Soldering_Checklist.md](checklists/Soldering_Checklist.md) - Checklist de soudure
- [Testing_Report_Template.md](templates/Testing_Report_Template.md) - Modèle de rapport de test

## Scripts de test / Testing Scripts

Les scripts de test sont disponibles dans le répertoire `hardware/pcb_testing/` :

Testing scripts are available in the `hardware/pcb_testing/` directory:

- `test_power.py` - Tests d'alimentation
- `test_imu.py` - Tests de l'IMU
- `test_motors.py` - Tests des moteurs
- `test_mcp3208.py` - Tests du MCP3208

## Équipement requis / Required Equipment

### Outils de mesure / Measurement Tools
- Multimètre digital / Digital multimeter
- Oscilloscope
- Analyseur logique (optionnel) / Logic analyzer (optional)

### Outils de soudure / Soldering Tools
- Station de soudure avec contrôle de température / Temperature-controlled soldering station
- Fer à souder avec panne fine / Soldering iron with fine tip
- Pompe à dessouder / Desoldering pump
- Flux et fil de soudure / Flux and solder wire

### Équipement de programmation / Programming Equipment
- Programmateur/Debugger (ST-Link, J-Link, etc.)
- Câbles de connexion / Connection cables
- Alimentation de laboratoire / Lab power supply

## Normes de sécurité / Safety Standards

⚠️ **IMPORTANT** : Respecter les normes de sécurité suivantes / Follow these safety standards:

1. Porter des lunettes de protection / Wear safety glasses
2. Travailler dans un environnement ESD-safe / Work in an ESD-safe environment
3. Vérifier les tensions avant de connecter l'alimentation / Verify voltages before connecting power
4. Ne jamais toucher les composants sous tension / Never touch powered components
5. Débrancher l'alimentation avant toute modification / Disconnect power before any modification

## Résolution des problèmes / Troubleshooting

En cas de problème pendant la mise en service, consulter :
In case of problems during commissioning, refer to:

1. [Troubleshooting Guide](Troubleshooting_Guide.md)
2. Documentation des composants / Component datasheets
3. Schémas électriques / Electrical schematics

## Support

Pour toute question ou problème, contacter l'équipe technique :
For any questions or issues, contact the technical team:

- Email: [project.support@example.com]
- Issue tracker: GitHub Issues
