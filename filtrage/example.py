"""
Example usage of the filtrage module
"""

import sys
import os

# Add parent directory to path to import filtrage
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from filtrage import MovingAverageFilter, LowPassFilter, HighPassFilter, BandPassFilter
from filtrage.filters import apply_filter_to_signal
import math


def generate_noisy_signal(length=100):
    """Generate a noisy sine wave signal"""
    import random
    signal = []
    for i in range(length):
        # Sine wave with noise
        clean = math.sin(2 * math.pi * i / 20)
        noise = random.gauss(0, 0.2)
        signal.append(clean + noise)
    return signal


def main():
    print("\n" + "="*60)
    print("Filtrage Module - Example Usage")
    print("="*60 + "\n")
    
    # Generate a noisy signal
    print("1. Generating noisy sine wave signal...")
    noisy_signal = generate_noisy_signal(50)
    print(f"   Generated {len(noisy_signal)} samples\n")
    
    # Example 1: Moving Average Filter
    print("2. Applying Moving Average Filter (window_size=5)...")
    maf = MovingAverageFilter(window_size=5)
    ma_filtered = apply_filter_to_signal(noisy_signal, maf)
    print(f"   Original signal [0:5]: {[f'{x:.3f}' for x in noisy_signal[:5]]}")
    print(f"   Filtered signal [0:5]: {[f'{x:.3f}' for x in ma_filtered[:5]]}\n")
    
    # Example 2: Low-Pass Filter
    print("3. Applying Low-Pass Filter (alpha=0.2)...")
    lpf = LowPassFilter(alpha=0.2)
    lp_filtered = apply_filter_to_signal(noisy_signal, lpf)
    print(f"   Original signal [0:5]: {[f'{x:.3f}' for x in noisy_signal[:5]]}")
    print(f"   Filtered signal [0:5]: {[f'{x:.3f}' for x in lp_filtered[:5]]}\n")
    
    # Example 3: High-Pass Filter
    print("4. Applying High-Pass Filter (alpha=0.8)...")
    hpf = HighPassFilter(alpha=0.8)
    hp_filtered = apply_filter_to_signal(noisy_signal, hpf)
    print(f"   Original signal [0:5]: {[f'{x:.3f}' for x in noisy_signal[:5]]}")
    print(f"   Filtered signal [0:5]: {[f'{x:.3f}' for x in hp_filtered[:5]]}\n")
    
    # Example 4: Band-Pass Filter
    print("5. Applying Band-Pass Filter...")
    bpf = BandPassFilter(low_alpha=0.3, high_alpha=0.7)
    bp_filtered = apply_filter_to_signal(noisy_signal, bpf)
    print(f"   Original signal [0:5]: {[f'{x:.3f}' for x in noisy_signal[:5]]}")
    print(f"   Filtered signal [0:5]: {[f'{x:.3f}' for x in bp_filtered[:5]]}\n")
    
    # Example 5: Real-time filtering
    print("6. Real-time filtering example (processing values one by one)...")
    lpf_realtime = LowPassFilter(alpha=0.3)
    print("   Processing 10 values:")
    for i, value in enumerate(noisy_signal[:10]):
        filtered = lpf_realtime.filter(value)
        print(f"      Sample {i}: {value:.3f} → {filtered:.3f}")
    
    print("\n" + "="*60)
    print("Examples completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
