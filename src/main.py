"""
Main module for 2526_B3_S6_Projet

This is the main entry point for the integrated embedded systems project.
Demonstrates the integration of all modules: asservi (PID control) and filtrage (signal filtering).
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def display_project_info():
    """Display project information"""
    print("=" * 70)
    print("  2526 B3 S6 - Projet de Système Embarqué Intégré")
    print("=" * 70)
    print("\nModules disponibles :")
    print("  1. Asservi (PID Control) - Contrôle de moteurs avec asservissement")
    print("  2. Filtrage (Signal Filtering) - Traitement numérique du signal")
    print("  3. Hardware PCB - Conception de circuits imprimés")
    print("=" * 70)


def demo_asservi():
    """Demonstrate the asservi (servo control) module"""
    try:
        from asservi import PIDController
        
        print("\n🎯 Démonstration du module Asservi (PID Controller)")
        print("-" * 70)
        
        # Create a PID controller
        pid = PIDController(kp=1.0, ki=0.1, kd=0.05, setpoint=100)
        pid.set_output_limits(-50, 50)
        
        print(f"Contrôleur PID créé avec:")
        print(f"  - Kp = 1.0 (Proportionnel)")
        print(f"  - Ki = 0.1 (Intégral)")
        print(f"  - Kd = 0.05 (Dérivé)")
        print(f"  - Consigne = 100")
        print(f"  - Limites de sortie = [-50, 50]")
        
        print("\nSimulation d'asservissement sur 5 étapes:")
        measured_value = 0
        for step in range(5):
            command = pid.update(measured_value)
            measured_value += command * 0.1  # Simulate system response
            print(f"  Étape {step + 1}: Mesure = {measured_value:6.2f}, "
                  f"Commande = {command:6.2f}, Erreur = {100 - measured_value:6.2f}")
        
        print("✅ Module Asservi opérationnel")
        return True
    except Exception as e:
        print(f"❌ Erreur dans le module Asservi: {e}")
        return False


def demo_filtrage():
    """Demonstrate the filtrage (signal filtering) module"""
    try:
        from filtrage import LowPassFilter, MovingAverageFilter
        
        print("\n🔬 Démonstration du module Filtrage")
        print("-" * 70)
        
        # Test signal with noise
        test_signal = [10.0, 15.0, 12.0, 18.0, 14.0, 16.0, 13.0, 17.0, 15.0, 19.0]
        
        # Low-pass filter
        lpf = LowPassFilter(alpha=0.3)
        print("Filtre passe-bas (alpha=0.3):")
        filtered_lpf = []
        for i, value in enumerate(test_signal[:5]):
            filtered = lpf.filter(value)
            filtered_lpf.append(filtered)
            print(f"  Signal[{i}] = {value:5.1f} → Filtré = {filtered:5.2f}")
        
        # Moving average filter
        print("\nFiltre à moyenne mobile (fenêtre=3):")
        maf = MovingAverageFilter(window_size=3)
        filtered_maf = []
        for i, value in enumerate(test_signal[:5]):
            filtered = maf.filter(value)
            filtered_maf.append(filtered)
            print(f"  Signal[{i}] = {value:5.1f} → Filtré = {filtered:5.2f}")
        
        print("✅ Module Filtrage opérationnel")
        return True
    except Exception as e:
        print(f"❌ Erreur dans le module Filtrage: {e}")
        return False


def main():
    """Main function - Entry point for the integrated project"""
    display_project_info()
    
    print("\n📦 Vérification des modules...")
    print("=" * 70)
    
    # Test asservi module
    asservi_ok = demo_asservi()
    
    # Test filtrage module
    filtrage_ok = demo_filtrage()
    
    # Summary
    print("\n" + "=" * 70)
    print("  Résumé de l'intégration")
    print("=" * 70)
    print(f"  Asservi (PID):       {'✅ OK' if asservi_ok else '❌ ERREUR'}")
    print(f"  Filtrage (Signal):   {'✅ OK' if filtrage_ok else '❌ ERREUR'}")
    print(f"  Hardware PCB:        📋 Documentation disponible")
    print("=" * 70)
    
    if asservi_ok and filtrage_ok:
        print("\n🎉 Tous les modules sont opérationnels!")
        print("\nPour plus d'informations, consultez:")
        print("  - README.md (racine)")
        print("  - asservi/README.md (documentation PID)")
        print("  - filtrage/README.md (documentation filtrage)")
        print("  - hardware/pcb/README.md (documentation hardware)")
    else:
        print("\n⚠️  Certains modules présentent des erreurs.")
        sys.exit(1)


if __name__ == "__main__":
    main()
