"""Contrôleur d'équilibre : IMU LSM6DSOX + filtre complémentaire + PID.

Fournit un angle filtré en degrés et une commande de vitesse moteur (RPM).
"""

from __future__ import annotations

import math

from imu.drv_lsm6dsow import drv_lsm6dsow
from imu.setting import SF_2G, SF_200DPS
from control.pid import PID


class BalanceController:
    """IMU + filtre complémentaire + PID d'équilibre en un seul objet.

    Paramètres
    ----------
    kp, ki, kd : gains PID pour l'équilibre
    kg         : gain appliqué sur l'angle accéléromètre dans le filtre
    max_speed  : vitesse maximale en sortie (RPM)
    angle_offset : offset de calibration (angle lu quand le robot est droit)
    alpha      : poids du gyroscope dans le filtre complémentaire (0.95–0.99)
    output_beta : lissage exponentiel de la sortie (0 = désactivé)
    axis       : 'x' ou 'y' selon l'orientation de l'IMU sur le PCB
    deadband   : zone morte en degrés (supprime les micro-oscillations)
    """

    def __init__(
        self,
        kp: float = 30.0,
        ki: float = 0.5,
        kd: float = 1.2,
        kg: float = 1.0,
        max_speed: float = 60.0,
        angle_offset: float = 0.0,
        alpha: float = 0.98,
        output_beta: float = 0.0,
        axis: str = "x",
        deadband: float = 2.0,
    ) -> None:
        # Matériel
        self._imu = drv_lsm6dsow(bus=1)

        # PID équilibre
        self._pid = PID(
            kp=kp, ki=ki, kd=kd,
            out_min=-max_speed,
            out_max= max_speed,
        )

        # Paramètres filtre
        self.angle_offset = angle_offset
        self.alpha        = alpha          # poids gyro
        self.output_beta  = output_beta    # lissage sortie
        self.axis         = axis.lower()
        self.deadband     = deadband
        self.kg           = kg

        # État interne
        self.angle: float           = 0.0   # angle filtré courant (degrés)
        self._filtered_angle: float = 0.0
        self._last_output: float    = 0.0
        self._initialized: bool     = False

    # ── Boucle de contrôle ─────────────────────────────────────────────────────

    def update(self, dt: float) -> float:
        """Lit l'IMU, met à jour le filtre complémentaire et calcule la commande.

        Parameters
        ----------
        dt : temps écoulé depuis le dernier appel (secondes)

        Returns
        -------
        float : consigne de vitesse en RPM (positive = avant, négative = arrière)
        """
        # 1. Lecture IMU
        x_a, y_a, z_a = self._imu.read_accel()
        x_g, y_g, z_g = self._imu.read_gyro()

        # 2. Calcul de l'angle accéléromètre et du taux gyroscope
        if self.axis == "x":
            # Penchement avant/arrière autour de l'axe X
            accel_angle = math.degrees(math.atan2(y_a * SF_2G, z_a * SF_2G))
            gyro_rate   = x_g * SF_200DPS   # °/s
        else:
            # Penchement avant/arrière autour de l'axe Y
            accel_angle = math.degrees(math.atan2(x_a * SF_2G, z_a * SF_2G))
            gyro_rate   = y_g * SF_200DPS

        # 3. Initialisation au premier appel
        if not self._initialized:
            self._filtered_angle = accel_angle
            self._initialized = True

        # 4. Filtre complémentaire
        #    α × (θ_précédent + ω_gyro × dt) + (1−α) × θ_accél
        self._filtered_angle = (
            self.alpha * (self._filtered_angle + gyro_rate * dt)
            + (1.0 - self.alpha) * accel_angle * self.kg
        )

        # 5. Soustraction de l'offset de calibration
        self.angle = self._filtered_angle - self.angle_offset

        # 6. Zone morte : le robot est suffisamment droit → pas de commande
        if abs(self.angle) < self.deadband:
            self._pid.reset()
            self._last_output = 0.0
            return 0.0

        # 7. PID — l'erreur est l'angle lui-même (consigne = 0°)
        output = self._pid.compute(error=self.angle, dt=dt)

        # 8. Lissage exponentiel optionnel de la sortie
        if self.output_beta > 0.0:
            output = (
                self.output_beta * self._last_output
                + (1.0 - self.output_beta) * output
            )
        self._last_output = output

        return output

    # ── Utilitaires ────────────────────────────────────────────────────────────

    def reset(self) -> None:
        """Remet à zéro le PID et réinitialise le filtre au prochain appel."""
        self._pid.reset()
        self._initialized = False
        self._last_output = 0.0

    def set_gains(self, kp: float, ki: float, kd: float) -> None:
        """Met à jour les gains PID à chaud."""
        self._pid.set_gains(kp, ki, kd)

    def close(self) -> None:
        """Libère le bus I²C."""
        if hasattr(self._imu, "bus"):
            try:
                self._imu.bus.close()
            except Exception:
                pass
