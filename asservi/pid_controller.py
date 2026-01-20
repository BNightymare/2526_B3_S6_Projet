"""
Contrôleur PID (Proportionnel-Intégral-Dérivé) pour l'asservissement.

Le contrôleur PID permet d'atteindre et maintenir une consigne en calculant
une commande basée sur l'erreur entre la mesure actuelle et la consigne.
"""

import time


class PIDController:
    """
    Contrôleur PID pour l'asservissement de systèmes.
    
    Attributes:
        kp (float): Gain proportionnel
        ki (float): Gain intégral
        kd (float): Gain dérivé
        setpoint (float): Consigne à atteindre
    """
    
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=0.0):
        """
        Initialise le contrôleur PID.
        
        Args:
            kp (float): Gain proportionnel (défaut: 1.0)
            ki (float): Gain intégral (défaut: 0.0)
            kd (float): Gain dérivé (défaut: 0.0)
            setpoint (float): Consigne initiale (défaut: 0.0)
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        
        self._integral = 0.0
        self._last_error = 0.0
        self._last_time = None
        
        self._output_limits = (None, None)
        self._integral_limits = (None, None)
    
    def set_gains(self, kp=None, ki=None, kd=None):
        """
        Modifie les gains du contrôleur PID.
        
        Args:
            kp (float, optional): Nouveau gain proportionnel
            ki (float, optional): Nouveau gain intégral
            kd (float, optional): Nouveau gain dérivé
        """
        if kp is not None:
            self.kp = kp
        if ki is not None:
            self.ki = ki
        if kd is not None:
            self.kd = kd
    
    def set_setpoint(self, setpoint):
        """
        Définit une nouvelle consigne.
        
        Args:
            setpoint (float): Nouvelle consigne à atteindre
        """
        self.setpoint = setpoint
    
    def set_output_limits(self, min_output=None, max_output=None):
        """
        Définit les limites de la sortie du contrôleur.
        
        Args:
            min_output (float, optional): Limite minimale de sortie
            max_output (float, optional): Limite maximale de sortie
        """
        self._output_limits = (min_output, max_output)
    
    def set_integral_limits(self, min_integral=None, max_integral=None):
        """
        Définit les limites de l'intégrale (anti-windup).
        
        Args:
            min_integral (float, optional): Limite minimale de l'intégrale
            max_integral (float, optional): Limite maximale de l'intégrale
        """
        self._integral_limits = (min_integral, max_integral)
    
    def reset(self):
        """
        Réinitialise le contrôleur (intégrale, erreur précédente, etc.).
        """
        self._integral = 0.0
        self._last_error = 0.0
        self._last_time = None
    
    def update(self, measured_value, dt=None):
        """
        Calcule la sortie du contrôleur PID.
        
        Args:
            measured_value (float): Valeur mesurée actuelle
            dt (float, optional): Pas de temps depuis la dernière mise à jour.
                                 Si None, calcule automatiquement.
        
        Returns:
            float: Commande de sortie du contrôleur
        """
        current_time = time.time()
        
        if dt is None:
            if self._last_time is None:
                dt = 0.0
            else:
                dt = current_time - self._last_time
        
        self._last_time = current_time
        
        error = self.setpoint - measured_value
        
        # Terme proportionnel
        p_term = self.kp * error
        
        # Terme intégral
        if dt > 0:
            self._integral += error * dt
            
            # Anti-windup: limiter l'intégrale
            min_int, max_int = self._integral_limits
            if min_int is not None and self._integral < min_int:
                self._integral = min_int
            if max_int is not None and self._integral > max_int:
                self._integral = max_int
        
        i_term = self.ki * self._integral
        
        # Terme dérivé
        if dt > 0:
            derivative = (error - self._last_error) / dt
        else:
            derivative = 0.0
        
        d_term = self.kd * derivative
        
        self._last_error = error
        
        # Calcul de la sortie
        output = p_term + i_term + d_term
        
        # Limiter la sortie
        min_out, max_out = self._output_limits
        if min_out is not None and output < min_out:
            output = min_out
        if max_out is not None and output > max_out:
            output = max_out
        
        return output
    
    def get_components(self):
        """
        Retourne les composantes actuelles du PID pour le débogage.
        
        Returns:
            dict: Dictionnaire contenant les valeurs P, I, D et l'erreur
        """
        return {
            'error': self._last_error,
            'integral': self._integral,
            'p_term': self.kp * self._last_error,
            'i_term': self.ki * self._integral,
        }
