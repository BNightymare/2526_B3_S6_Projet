# 2526_B3_S6_Projet

Projet académique de conception et mise en service de PCB avec capteurs IMU, moteurs et ADC.

Academic project for PCB design and commissioning with IMU sensors, motors and ADC.

## Structure du projet / Project Structure

```
2526_B3_S6_Projet/
├── docs/
│   └── pcb_commissioning/      # Documentation de mise en service PCB
│       ├── README.md            # Vue d'ensemble du processus
│       ├── 01_PCB_Reception_Soldering.md  # Procédures de réception et soudure
│       ├── 02_Hardware_Unit_Testing.md    # Tests unitaires matériels
│       ├── 03_Component_Validation.md     # Validation IMU, moteurs, MCP3208
│       ├── checklists/          # Listes de contrôle
│       └── templates/           # Modèles de rapports
│
└── hardware/
    └── pcb_testing/             # Scripts de test
        ├── test_imu.py          # Test de l'IMU
        └── test_mcp3208.py      # Test du MCP3208 ADC
```

## Mise en service du PCB / PCB Commissioning

La mise en service du PCB comprend plusieurs étapes critiques :

PCB commissioning includes several critical stages:

1. **Réception et soudure** / **Reception and Soldering**
   - Inspection visuelle / Visual inspection
   - Vérification dimensionnelle / Dimensional verification
   - Soudure des composants / Component soldering

2. **Tests unitaires matériels** / **Hardware Unit Testing**
   - Tests d'alimentation / Power supply tests
   - Tests de communication (UART, I2C, SPI)
   - Tests des interfaces I/O

3. **Validation des composants** / **Component Validation**
   - IMU (gyroscope + accéléromètre)
   - Moteurs (contrôle directionnel et vitesse)
   - MCP3208 (ADC 8 canaux, 12-bit)

### Documentation

Documentation complète disponible dans [`docs/pcb_commissioning/`](docs/pcb_commissioning/)

Complete documentation available in [`docs/pcb_commissioning/`](docs/pcb_commissioning/)

### Scripts de test / Testing Scripts

```bash
# Test IMU
python3 hardware/pcb_testing/test_imu.py

# Test MCP3208 ADC
python3 hardware/pcb_testing/test_mcp3208.py
```

### Dépendances / Dependencies

```bash
# Installation des bibliothèques Python nécessaires
# Install required Python libraries
pip install smbus-cffi spidev
```

## Composants principaux / Main Components

- **IMU**: MPU6050 ou équivalent (gyroscope + accéléromètre 6-axis)
- **ADC**: MCP3208 (8-channel, 12-bit)
- **Moteurs** / **Motors**: DC avec drivers (L298N, DRV8833, etc.)
- **Communication**: UART, I2C, SPI

## Support

Pour toute question ou problème :
For any questions or issues:

- Créer une issue sur GitHub / Create a GitHub issue
- Consulter la documentation / Refer to documentation