#!/usr/bin/env python3
"""
Exemple d'utilisation basique du contrôleur PID.

Cet exemple montre comment utiliser le PIDController pour asservir
un système simple simulé.
"""

import sys
import time
sys.path.insert(0, '/home/runner/work/2526_B3_S6_Projet/2526_B3_S6_Projet')

from asservi import PIDController


def simulate_system(command, current_value, dt=0.02):
    """
    Simule un système simple (premier ordre).
    
    Args:
        command: Commande d'entrée
        current_value: Valeur actuelle du système
        dt: Pas de temps
    
    Returns:
        Nouvelle valeur du système
    """
    # Système simple avec inertie
    tau = 0.5  # Constante de temps
    new_value = current_value + (command - current_value) * dt / tau
    return new_value


def main():
    """Exemple d'asservissement avec PID."""
    print("=== Exemple d'asservissement PID ===\n")
    
    # Créer le contrôleur PID
    pid = PIDController(kp=2.0, ki=0.5, kd=0.1, setpoint=100.0)
    pid.set_output_limits(-50, 50)
    pid.set_integral_limits(-100, 100)
    
    print(f"Consigne: {pid.setpoint}")
    print(f"Gains: Kp={pid.kp}, Ki={pid.ki}, Kd={pid.kd}")
    print("\nDébut de l'asservissement...\n")
    
    # Simulation
    measured_value = 0.0
    dt = 0.02  # 50 Hz
    max_iterations = 200
    
    for i in range(max_iterations):
        # Calculer la commande PID
        command = pid.update(measured_value, dt)
        
        # Simuler le système
        measured_value = simulate_system(command, measured_value, dt)
        
        # Afficher l'état tous les 10 itérations
        if i % 10 == 0:
            error = pid.setpoint - measured_value
            components = pid.get_components()
            print(f"t={i*dt:.2f}s | Mesure: {measured_value:6.2f} | "
                  f"Erreur: {error:6.2f} | Commande: {command:6.2f} | "
                  f"P: {components['p_term']:6.2f} | "
                  f"I: {components['i_term']:6.2f}")
        
        # Arrêter si la consigne est atteinte
        if abs(pid.setpoint - measured_value) < 0.5 and i > 50:
            print(f"\nConsigne atteinte après {i*dt:.2f}s")
            print(f"Valeur finale: {measured_value:.2f}")
            break
        
        time.sleep(dt)
    
    print("\n=== Fin de l'exemple ===")


if __name__ == "__main__":
    main()
