# Guide de Démarrage

## Installation en 3 étapes

### 1️⃣ Activer SPI et I2C

```bash
sudo raspi-config
```

- Aller dans **Interface Options** → **SPI** → **Enable**
- Aller dans **Interface Options** → **I2C** → **Enable**
- Redémarrer: `sudo reboot`

### 2️⃣ Installer les dépendances

```bash
cd "Projet 6 CLS Code main"
pip3 install -r requirements.txt
```

### 3️⃣ Lancer le robot

**Option A - Script automatique (Linux/Mac):**
```bash
chmod +x start_robot.sh
./start_robot.sh
```

**Option B - Commande directe:**
```bash
python3 main.py
```

**Option C - Tests individuels:**
```bash
python3 test_components.py
```

## ⚙️ Configuration Rapide

Modifiez `config.py` pour ajuster:

```python
# Seuil de détection (ajuster selon vos capteurs)
LINE_THRESHOLD = 1.5

# Vitesse du robot
FORWARD_ANGLE = 360
MOTOR1_SPEED_RPM = 9.375
MOTOR2_SPEED_RPM = 5.625

# Activer/Désactiver l'IMU
USE_IMU = False

# Mode verbeux
DEBUG_MODE = True
```

## 🔧 Dépannage Express

| Problème | Solution |
|----------|----------|
| `ImportError: No module named 'RPi.GPIO'` | `pip3 install RPi.GPIO` |
| `FileNotFoundError: [Errno 2] No such file or directory: '/dev/spidev0.0'` | Activer SPI dans raspi-config |
| Les moteurs ne bougent pas | Vérifier alimentation et branchements GPIO |
| Capteurs détectent mal | Ajuster `LINE_THRESHOLD` dans config.py |

## 📦 Structure des Fichiers

```
Projet 6 CLS Code main/
├── main.py              ← Programme principal (LANCER CE FICHIER)
├── config.py            ← Configuration (MODIFIER ICI)
├── test_components.py   ← Tests individuels
├── start_robot.sh       ← Script de démarrage automatique
├── requirements.txt     ← Dépendances Python
├── README.md            ← Documentation complète
└── QUICKSTART.md        ← Ce fichier
```

## 🎮 Utilisation

1. Placer le robot sur un circuit avec une ligne noire
2. Lancer `python3 main.py`
3. Le robot suit automatiquement la ligne
4. Appuyer sur **Ctrl+C** pour arrêter

## 🐛 En cas de problème

1. Tester chaque composant: `python3 test_components.py`
2. Vérifier les branchements (voir README.md)
3. Consulter les logs d'erreur
4. Ajuster les paramètres dans `config.py`

## 📞 Support

- Documentation complète: `README.md`
- Tests: `python3 test_components.py`
- Configuration: `config.py`

---

**Prêt en 5 minutes! 🎉**
