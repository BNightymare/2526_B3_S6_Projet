"""
Digital Signal Filters
Implements various digital filters for signal processing.
"""

import math
from typing import List, Optional


class MovingAverageFilter:
    """
    Simple moving average filter.
    Smooths signal by averaging over a window of samples.
    """
    
    def __init__(self, window_size: int = 5):
        """
        Initialize moving average filter.
        
        Args:
            window_size: Number of samples to average (default: 5)
        """
        if window_size < 1:
            raise ValueError("Window size must be at least 1")
        self.window_size = window_size
        self.buffer: List[float] = []
    
    def filter(self, value: float) -> float:
        """
        Apply filter to a single value.
        
        Args:
            value: Input value
            
        Returns:
            Filtered value
        """
        self.buffer.append(value)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)
        return sum(self.buffer) / len(self.buffer)
    
    def reset(self):
        """Reset filter state."""
        self.buffer.clear()


class LowPassFilter:
    """
    First-order low-pass filter (exponential smoothing).
    Attenuates high-frequency components of the signal.
    """
    
    def __init__(self, alpha: float = 0.5):
        """
        Initialize low-pass filter.
        
        Args:
            alpha: Smoothing factor (0 < alpha <= 1)
                  Lower values = more smoothing
                  Higher values = less smoothing, more responsive
        """
        if not 0 < alpha <= 1:
            raise ValueError("Alpha must be in range (0, 1]")
        self.alpha = alpha
        self.previous_output: Optional[float] = None
    
    def filter(self, value: float) -> float:
        """
        Apply low-pass filter to a single value.
        
        Args:
            value: Input value
            
        Returns:
            Filtered value
        """
        if self.previous_output is None:
            self.previous_output = value
            return value
        
        output = self.alpha * value + (1 - self.alpha) * self.previous_output
        self.previous_output = output
        return output
    
    def reset(self):
        """Reset filter state."""
        self.previous_output = None


class HighPassFilter:
    """
    First-order high-pass filter.
    Attenuates low-frequency components and passes high-frequency components.
    """
    
    def __init__(self, alpha: float = 0.5):
        """
        Initialize high-pass filter.
        
        Args:
            alpha: Filter coefficient (0 < alpha <= 1)
                  Lower values = more attenuation of low frequencies
                  Higher values = less attenuation
        """
        if not 0 < alpha <= 1:
            raise ValueError("Alpha must be in range (0, 1]")
        self.alpha = alpha
        self.previous_input: Optional[float] = None
        self.previous_output: Optional[float] = None
    
    def filter(self, value: float) -> float:
        """
        Apply high-pass filter to a single value.
        
        Args:
            value: Input value
            
        Returns:
            Filtered value
        """
        if self.previous_input is None:
            self.previous_input = value
            self.previous_output = 0.0
            return 0.0
        
        output = self.alpha * (self.previous_output + value - self.previous_input)
        self.previous_input = value
        self.previous_output = output
        return output
    
    def reset(self):
        """Reset filter state."""
        self.previous_input = None
        self.previous_output = None


class BandPassFilter:
    """
    Band-pass filter combining low-pass and high-pass filters.
    Passes frequencies within a certain range.
    """
    
    def __init__(self, low_alpha: float = 0.3, high_alpha: float = 0.7):
        """
        Initialize band-pass filter.
        
        Args:
            low_alpha: Low-pass filter coefficient
            high_alpha: High-pass filter coefficient
        """
        self.low_pass = LowPassFilter(low_alpha)
        self.high_pass = HighPassFilter(high_alpha)
    
    def filter(self, value: float) -> float:
        """
        Apply band-pass filter to a single value.
        
        Args:
            value: Input value
            
        Returns:
            Filtered value
        """
        # First apply low-pass to remove high frequencies
        low_passed = self.low_pass.filter(value)
        # Then apply high-pass to remove low frequencies
        return self.high_pass.filter(low_passed)
    
    def reset(self):
        """Reset filter state."""
        self.low_pass.reset()
        self.high_pass.reset()


def apply_filter_to_signal(signal: List[float], filter_obj) -> List[float]:
    """
    Apply a filter to an entire signal.
    
    Args:
        signal: List of signal values
        filter_obj: Filter object with a filter() method
        
    Returns:
        Filtered signal
    """
    filter_obj.reset()
    return [filter_obj.filter(value) for value in signal]
