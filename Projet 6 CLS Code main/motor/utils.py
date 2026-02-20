"""Utilitaires pour les moteurs"""

def calculate_steps(angle, steps_per_rev, microstep):
    """Calcule le nombre de pas nécessaires pour un angle donné"""
    return int((angle / 360) * (steps_per_rev * microstep))

def rpm_to_hz(rpm, steps_per_rev, microstep):
    """Convertit RPM en fréquence Hz"""
    return (rpm * steps_per_rev * microstep) / 60
