"""Contrôleur d'équilibre : IMU + filtre complémentaire + PID."""

from __future__ import annotations

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "imu"))

from drv_lsm6dsow import drv_lsm6dsow
from setting import SF_2G, SF_200DPS
from control.pid import PID


class BalanceController:
    """IMU + filtre complémentaire + PID d'équilibre en un seul objet."""

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
    ):
        self._imu = drv_lsm6dsow(bus=1)
        self._pid = PID(kp=kp, ki=ki, kd=kd, out_min=-max_speed, out_max=max_speed)

        self.angle_offset = angle_offset
        self.alpha        = alpha
        self.output_beta  = output_beta
        self.axis         = axis.lower()
        self.deadband     = deadband
        self.kg           = kg

        self.angle: float          = 0.0
        self._filtered_angle: float = 0.0
        self._last_output: float   = 0.0
        self._initialized: bool    = False

    def update(self, dt: float) -> float:
        """Lit l'IMU, filtre l'angle, retourne la commande de vitesse."""
        x_a, y_a, z_a = self._imu.read_accel()
        x_g, y_g, z_g = self._imu.read_gyro()

        if self.axis == "x":
            accel_angle = math.degrees(math.atan2(y_a * SF_2G, z_a * SF_2G))
            gyro_rate   = x_g * SF_200DPS
        else:
            accel_angle = math.degrees(math.atan2(x_a * SF_2G, z_a * SF_2G))
            gyro_rate   = y_g * SF_200DPS

        if not self._initialized:
            self._filtered_angle = accel_angle
            self._initialized = True

        # Filtre complémentaire : 98% gyro + 2% accéléromètre
        self._filtered_angle = (
            self.alpha * (self._filtered_angle + gyro_rate * dt)
            + (1.0 - self.alpha) * accel_angle * self.kg
        )
        self.angle = self._filtered_angle - self.angle_offset

        # Zone morte
        if abs(self.angle) < self.deadband:
            self._pid.reset()
            return 0.0

        output = self._pid.compute(error=self.angle, dt=dt)

        if self.output_beta > 0:
            output = self.output_beta * self._last_output + (1 - self.output_beta) * output
        self._last_output = output

        return output

    def reset(self) -> None:
        self._pid.reset()
        self._initialized = False
        self._last_output = 0.0

    def close(self) -> None:
        if hasattr(self._imu, "bus"):
            self._imu.bus.close()
