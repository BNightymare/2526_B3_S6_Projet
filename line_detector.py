"""Contrôleur PID générique avec anti-windup et saturation de sortie."""

from __future__ import annotations


class PID:
    """Contrôleur PID discret.

    Paramètres
    ----------
    kp, ki, kd : gains proportionnel, intégral, dérivé
    out_min, out_max : saturation de la sortie (anti-windup intégré)
    """

    def __init__(
        self,
        kp: float = 1.0,
        ki: float = 0.0,
        kd: float = 0.0,
        out_min: float = -100.0,
        out_max: float = 100.0,
    ) -> None:
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.out_min = out_min
        self.out_max = out_max

        self._integral: float = 0.0
        self._prev_error: float = 0.0
        self._first: bool = True

    # ── API publique ───────────────────────────────────────────────────────────

    def compute(self, error: float, dt: float) -> float:
        """Calcule la sortie PID pour l'erreur et l'intervalle de temps donnés.

        Parameters
        ----------
        error : erreur courante (consigne − mesure)
        dt    : temps écoulé depuis le dernier appel (secondes)
        """
        if dt <= 0.0:
            return 0.0

        # Terme proportionnel
        p = self.kp * error

        # Terme intégral avec anti-windup (clamping)
        self._integral += error * dt
        i = self.ki * self._integral

        # Terme dérivé (différence finie, ignoré au 1er appel)
        if self._first:
            d = 0.0
            self._first = False
        else:
            d = self.kd * (error - self._prev_error) / dt

        self._prev_error = error

        # Sortie non saturée
        output = p + i + d

        # Anti-windup : si la sortie sature, on gèle l'intégrale
        if output > self.out_max:
            self._integral -= error * dt   # annule l'accumulation
            output = self.out_max
        elif output < self.out_min:
            self._integral -= error * dt
            output = self.out_min

        return output

    def reset(self) -> None:
        """Remet à zéro l'intégrateur et la mémoire dérivée."""
        self._integral = 0.0
        self._prev_error = 0.0
        self._first = True

    def set_gains(self, kp: float, ki: float, kd: float) -> None:
        """Met à jour les gains à chaud."""
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def __repr__(self) -> str:
        return (
            f"PID(kp={self.kp}, ki={self.ki}, kd={self.kd}, "
            f"out=[{self.out_min}, {self.out_max}])"
        )
