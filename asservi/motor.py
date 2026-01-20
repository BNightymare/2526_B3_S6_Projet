"""
Interface pour le contrôle de moteurs avec asservissement.

Fournit une abstraction pour contrôler des moteurs avec retour d'information
(encodeur, capteur de position, etc.) et asservissement PID.
"""

from .pid_controller import PIDController


class Motor:
    """
    Classe représentant un moteur avec asservissement.
    
    Attributes:
        name (str): Nom du moteur
        pid (PIDController): Contrôleur PID associé
    """
    
    def __init__(self, name="Motor", kp=1.0, ki=0.0, kd=0.0):
        """
        Initialise un moteur avec son contrôleur PID.
        
        Args:
            name (str): Nom du moteur (défaut: "Motor")
            kp (float): Gain proportionnel du PID (défaut: 1.0)
            ki (float): Gain intégral du PID (défaut: 0.0)
            kd (float): Gain dérivé du PID (défaut: 0.0)
        """
        self.name = name
        self.pid = PIDController(kp, ki, kd)
        
        self._current_position = 0.0
        self._target_position = 0.0
        self._current_speed = 0.0
        self._power = 0.0
        
        self.pid.set_output_limits(-100.0, 100.0)
    
    def set_target(self, position):
        """
        Définit la position cible du moteur.
        
        Args:
            position (float): Position cible à atteindre
        """
        self._target_position = position
        self.pid.set_setpoint(position)
    
    def update_position(self, position):
        """
        Met à jour la position actuelle du moteur (mesure du capteur).
        
        Args:
            position (float): Position actuelle mesurée
        """
        self._current_position = position
    
    def compute_power(self, dt=None):
        """
        Calcule la puissance à appliquer au moteur via le PID.
        
        Args:
            dt (float, optional): Pas de temps depuis la dernière mise à jour
        
        Returns:
            float: Puissance à appliquer (entre -100 et 100 par défaut)
        """
        self._power = self.pid.update(self._current_position, dt)
        return self._power
    
    def set_pid_gains(self, kp=None, ki=None, kd=None):
        """
        Modifie les gains du contrôleur PID du moteur.
        
        Args:
            kp (float, optional): Nouveau gain proportionnel
            ki (float, optional): Nouveau gain intégral
            kd (float, optional): Nouveau gain dérivé
        """
        self.pid.set_gains(kp, ki, kd)
    
    def set_power_limits(self, min_power, max_power):
        """
        Définit les limites de puissance du moteur.
        
        Args:
            min_power (float): Puissance minimale
            max_power (float): Puissance maximale
        """
        self.pid.set_output_limits(min_power, max_power)
    
    def get_position(self):
        """
        Retourne la position actuelle du moteur.
        
        Returns:
            float: Position actuelle
        """
        return self._current_position
    
    def get_target(self):
        """
        Retourne la position cible du moteur.
        
        Returns:
            float: Position cible
        """
        return self._target_position
    
    def get_error(self):
        """
        Retourne l'erreur actuelle (différence entre cible et position).
        
        Returns:
            float: Erreur de position
        """
        return self._target_position - self._current_position
    
    def get_power(self):
        """
        Retourne la puissance actuelle appliquée au moteur.
        
        Returns:
            float: Puissance actuelle
        """
        return self._power
    
    def reset(self):
        """
        Réinitialise le moteur et son contrôleur PID.
        """
        self.pid.reset()
        self._power = 0.0
    
    def __str__(self):
        """
        Représentation textuelle du moteur.
        
        Returns:
            str: Description de l'état du moteur
        """
        return (f"Motor({self.name}): pos={self._current_position:.2f}, "
                f"target={self._target_position:.2f}, "
                f"error={self.get_error():.2f}, power={self._power:.2f}")
