#!/usr/bin/env python3
"""
Exemple d'utilisation de la classe Motor avec asservissement.

Cet exemple montre comment utiliser la classe Motor pour contrôler
un moteur avec retour d'encodeur.
"""

import sys
import time
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from asservi import Motor


class SimulatedMotor:
    """Simule un moteur avec encodeur pour les tests."""
    
    def __init__(self):
        self.position = 0.0
        self.velocity = 0.0
        self.power = 0.0
    
    def apply_power(self, power):
        """Applique une puissance au moteur."""
        self.power = power
    
    def update(self, dt):
        """Met à jour la position du moteur."""
        # Modèle simple : accélération proportionnelle à la puissance
        acceleration = self.power * 0.5
        self.velocity += acceleration * dt
        self.velocity *= 0.95  # Friction
        self.position += self.velocity * dt
        return self.position


def main():
    """Exemple de contrôle de moteur avec asservissement."""
    print("=== Exemple de contrôle de moteur ===\n")
    
    # Créer le moteur avec contrôleur PID
    motor = Motor(name="Moteur Droit", kp=3.0, ki=0.8, kd=0.2)
    motor.set_power_limits(-100, 100)
    motor.pid.set_integral_limits(-50, 50)
    
    # Simulateur de moteur
    sim_motor = SimulatedMotor()
    
    # Définir une position cible
    target_position = 500.0
    motor.set_target(target_position)
    
    print(f"Position cible: {target_position}")
    print(f"Gains PID: Kp={motor.pid.kp}, Ki={motor.pid.ki}, Kd={motor.pid.kd}")
    print("\nDébut du mouvement...\n")
    
    # Boucle de contrôle
    dt = 0.02  # 50 Hz
    max_iterations = 300
    
    for i in range(max_iterations):
        # Lire la position actuelle (du simulateur)
        current_position = sim_motor.position
        motor.update_position(current_position)
        
        # Calculer la puissance à appliquer
        power = motor.compute_power(dt)
        
        # Appliquer au moteur simulé
        sim_motor.apply_power(power)
        sim_motor.update(dt)
        
        # Afficher l'état tous les 10 itérations
        if i % 10 == 0:
            print(motor)
        
        # Arrêter si la position est atteinte
        if abs(motor.get_error()) < 1.0 and i > 100:
            print(f"\nPosition atteinte après {i*dt:.2f}s")
            print(f"Position finale: {current_position:.2f}")
            print(f"Erreur résiduelle: {motor.get_error():.2f}")
            break
        
        time.sleep(dt)
    
    print("\n=== Changement de consigne ===\n")
    
    # Changer la consigne
    new_target = 200.0
    motor.set_target(new_target)
    print(f"Nouvelle position cible: {new_target}")
    
    # Continuer l'asservissement
    for i in range(150):
        current_position = sim_motor.position
        motor.update_position(current_position)
        
        power = motor.compute_power(dt)
        sim_motor.apply_power(power)
        sim_motor.update(dt)
        
        if i % 10 == 0:
            print(motor)
        
        if abs(motor.get_error()) < 1.0 and i > 50:
            print(f"\nNouvelle position atteinte après {i*dt:.2f}s")
            print(f"Position finale: {current_position:.2f}")
            break
        
        time.sleep(dt)
    
    print("\n=== Fin de l'exemple ===")


if __name__ == "__main__":
    main()
