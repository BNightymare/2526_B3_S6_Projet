# Robot Suiveur de Ligne Scobolide

Ce projet intègre tous les codes des différents composants (accéléromètre/gyroscope LSM6DSOX, moteur MCP3208, traceur de ligne TMC2225).

## Structure du Projet

```
Projet 6 CLS Code main/
│
├── main.py                    # Programme principal
├── config.py                  # Configuration globale du robot
├── README.md                  # Ce fichier
├── README_integration.md      # Documentation d'intégration (originale)
│
├── sensors/                   # Module des capteurs
│   ├── __init__.py
│   ├── MCP3208.py            # Driver ADC pour capteurs infrarouges
│   └── line_detector.py      # Détection de ligne
│
├── motor/                     # Module des moteurs
│   ├── __init__.py
│   ├── config.py             # Configuration des moteurs
│   ├── driver.py             # Driver TMC2225
│   ├── controller.py         # Contrôleur double moteur
│   └── utils.py              # Utilitaires
│
└── imu/                       # Module IMU (optionnel)
    ├── __init__.py
    ├── setting.py            # Configuration LSM6DSOX
    └── drv_lsm6dsow.py       # Driver IMU
```

## 🔧 Composants Intégrés

### 1. **Capteur de Ligne Infrarouge** 
- **Responsable**: [Nom du membre]
- **Fichiers**: `sensors/MCP3208.py`, `sensors/line_detector.py`
- **Description**: Utilise un ADC MCP3208 pour lire 8 capteurs infrarouges qui détectent la position d'une ligne noire

### 2. **Contrôleur de Moteurs**
- **Responsable**: Raphaël, Quentin, Samir
- **Fichiers**: `motor/driver.py`, `motor/controller.py`, `motor/config.py`
- **Description**: Contrôle deux moteurs pas-à-pas TMC2225 pour le déplacement du robot

### 3. **IMU (Unité de Mesure Inertielle)**
- **Responsable**: [Nom du membre]
- **Fichiers**: `imu/drv_lsm6dsow.py`, `imu/setting.py`
- **Description**: Capteur LSM6DSOX pour mesurer l'accélération et la rotation (optionnel)

### 4. **Intégration Principale**
- **Responsable**: [Nom du membre]
- **Fichiers**: `main.py`, `config.py`
- **Description**: Coordonne tous les composants pour le suivi de ligne

## ⚙️ Configuration

### Modifier les Paramètres

Ouvrez le fichier `config.py` pour ajuster :

```python
# Seuil de détection de ligne
LINE_THRESHOLD = 1.5

# Angles de correction
ROTATION_ANGLE_MEDIUM = 10

# Vitesse de déplacement
FORWARD_ANGLE = 360

# Activer/Désactiver l'IMU
USE_IMU = False

# Mode debug
DEBUG_MODE = True
```

## 🚀 Installation et Utilisation

### Prérequis

```bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev
pip3 install RPi.GPIO spidev smbus2
```

### Activer SPI et I2C

```bash
sudo raspi-config
# Interface Options → SPI → Enable
# Interface Options → I2C → Enable
```

### Lancement du Robot

```bash
cd "c:\Users\clara\OneDrive - ensea\Bureau\Ecole\Bachelor\A3\Projet 6\3. Code\Projet 6 CLS Code main"
python3 main.py
```

### Arrêter le Robot

Appuyez sur `Ctrl+C` pour arrêter le robot proprement.

## 🎯 Fonctionnement

1. **Lecture des Capteurs**: Le robot lit continuellement les 8 capteurs infrarouges
2. **Détection de Position**: Détermine si la ligne est à gauche, au centre, à droite ou absente
3. **Correction de Trajectoire**: 
   - Ligne au centre → Avancer tout droit
   - Ligne à gauche → Tourner à gauche
   - Ligne à droite → Tourner à droite
   - Pas de ligne → Arrêt et recherche
4. **Stabilisation (optionnelle)**: Utilise l'IMU pour améliorer la stabilité

## 🔌 Branchements

### Capteurs Infrarouges (MCP3208)
- **VDD**: 3.3V
- **VREF**: 3.3V
- **AGND**: GND
- **CLK**: GPIO 11 (SCLK)
- **DOUT**: GPIO 9 (MISO)
- **DIN**: GPIO 10 (MOSI)
- **CS/SHDN**: GPIO 8 (CE0)
- **DGND**: GND

### Moteurs (TMC2225)
#### Moteur 1 (Gauche)
- **STEP**: GPIO 32
- **DIR**: GPIO 36

#### Moteur 2 (Droit)
- **STEP**: GPIO 33
- **DIR**: GPIO 31

### IMU (LSM6DSOX) - Optionnel
- **VDD**: 3.3V
- **GND**: GND
- **SDA**: GPIO 2
- **SCL**: GPIO 3

## 🐛 Dépannage

### Le robot ne détecte pas la ligne
- Vérifiez le seuil dans `config.py` (LINE_THRESHOLD)
- Testez les capteurs individuellement avec `sensors/line_detector.py`

### Les moteurs ne bougent pas
- Vérifiez les connexions GPIO
- Vérifiez l'alimentation des moteurs
- Testez avec `motor/controller.py`

### Erreurs d'importation
- Assurez-vous d'être dans le bon répertoire
- Vérifiez que tous les fichiers `__init__.py` sont présents

## 📝 Modifications Futures

- [ ] Améliorer l'algorithme de recherche de ligne
- [ ] Utiliser l'IMU pour la stabilisation
- [ ] Ajouter un mode d'étalonnage automatique
- [ ] Implémenter un PID pour le suivi de ligne
- [ ] Ajouter des logs dans un fichier

## 👥 Équipe

- **Capteurs**: [Nom]
- **Moteurs**: Raphaël, Quentin, Samir
- **IMU**: [Nom]
- **Intégration**: [Nom]

## 📄 Licence

Projet académique - ENSEA Bachelor A3 - 2026
