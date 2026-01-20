"""
Module d'asservissement (servo control) pour le projet.

Ce module fournit des outils pour l'asservissement de moteurs et autres systèmes,
incluant un contrôleur PID et des interfaces pour gérer les moteurs.
"""

from .pid_controller import PIDController
from .motor import Motor

__all__ = ['PIDController', 'Motor']
__version__ = '1.0.0'
