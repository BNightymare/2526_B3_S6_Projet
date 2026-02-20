#!/bin/bash
# Script de démarrage rapide pour le robot suiveur de ligne
# Usage: ./start_robot.sh

echo "╔════════════════════════════════════════════════════════╗"
echo "║       ROBOT SUIVEUR DE LIGNE - DÉMARRAGE              ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Vérifier si on est sur Raspberry Pi
if [ ! -f /proc/device-tree/model ] || ! grep -q "Raspberry Pi" /proc/device-tree/model; then
    echo "⚠ Attention: Ce script doit être exécuté sur un Raspberry Pi"
    echo "  Continuer quand même? (o/n)"
    read -r response
    if [ "$response" != "o" ]; then
        exit 1
    fi
fi

# Vérifier les dépendances
echo "[1/3] Vérification des dépendances Python..."
python3 -c "import RPi.GPIO, spidev, smbus2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠ Dépendances manquantes. Installation..."
    pip3 install -r requirements.txt
else
    echo "✓ Dépendances OK"
fi

# Vérifier SPI
echo ""
echo "[2/3] Vérification de SPI..."
if [ -e /dev/spidev0.0 ]; then
    echo "✓ SPI activé"
else
    echo "✗ SPI non activé. Activez-le avec: sudo raspi-config"
    echo "  Interface Options → SPI → Enable"
    exit 1
fi

# Vérifier I2C
echo ""
echo "[3/3] Vérification de I2C..."
if [ -e /dev/i2c-1 ]; then
    echo "✓ I2C activé"
else
    echo "⚠ I2C non activé (nécessaire uniquement pour l'IMU)"
fi

echo ""
echo "════════════════════════════════════════════════════════"
echo "✓ Prêt à démarrer!"
echo "════════════════════════════════════════════════════════"
echo ""
echo "Lancement du robot dans 3 secondes..."
echo "(Appuyez sur Ctrl+C pour annuler)"
sleep 3

# Lancer le programme principal
python3 main.py
