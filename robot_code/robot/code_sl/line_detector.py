"""Détection de la ligne via les 8 capteurs IR du MCP3208."""

from __future__ import annotations

from .MCP3208 import MCP3208

# Pondération : canal 0 = extrême gauche (-3), canal 7 = extrême droite (+3)
_WEIGHTS = [-3.0, -2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 3.0]


def get_line_error(ifr: MCP3208, threshold: float = 1.5) -> tuple[float | None, list[float]]:
    """Retourne une erreur normalisée entre -1.0 (gauche) et +1.0 (droite),
    ou None si aucune ligne n'est détectée.
    """
    readings = ifr.read_all_channels()
    detected = [w for v, w in zip(readings, _WEIGHTS) if v < threshold]

    if not detected:
        return None, readings

    raw = sum(detected) / len(detected)
    return max(-1.0, min(1.0, raw / 3.0)), readings


def detect_line(ifr: MCP3208, threshold: float = 1.5, verbose: bool = False) -> str:
    """Version string conservée pour main_line.py. Retourne 'left','center','right','none'."""
    error, readings = get_line_error(ifr, threshold)

    if verbose:
        labels = ["L2", "L1", "L ", "C1", "C ", "R ", "R1", "R2"]
        parts = " | ".join(f"{l}:{v:.2f}V" for l, v in zip(labels, readings))
        print(parts, end=" --> ")

    if error is None:
        position = "none"
    elif error < -0.15:
        position = "left"
    elif error > 0.15:
        position = "right"
    else:
        position = "center"

    if verbose:
        print(position)

    return position
