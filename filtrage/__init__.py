"""
Filtrage - Signal Filtering Module
Provides digital signal filtering implementations for signal processing.
"""

from .filters import LowPassFilter, HighPassFilter, BandPassFilter, MovingAverageFilter

__all__ = ['LowPassFilter', 'HighPassFilter', 'BandPassFilter', 'MovingAverageFilter']
__version__ = '0.1.0'
