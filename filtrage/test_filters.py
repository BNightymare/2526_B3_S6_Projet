"""
Tests for filtrage module
"""

import sys
import os

# Add parent directory to path to import filtrage
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from filtrage import MovingAverageFilter, LowPassFilter, HighPassFilter, BandPassFilter
from filtrage.filters import apply_filter_to_signal


def test_moving_average_filter():
    """Test MovingAverageFilter"""
    print("Testing MovingAverageFilter...")
    
    maf = MovingAverageFilter(window_size=3)
    
    # Test single values
    assert maf.filter(1.0) == 1.0  # First value
    assert maf.filter(2.0) == 1.5  # (1+2)/2
    assert maf.filter(3.0) == 2.0  # (1+2+3)/3
    assert maf.filter(4.0) == 3.0  # (2+3+4)/3
    
    print("  ✓ MovingAverageFilter passed")


def test_low_pass_filter():
    """Test LowPassFilter"""
    print("Testing LowPassFilter...")
    
    lpf = LowPassFilter(alpha=0.5)
    
    # Test with a step input
    result1 = lpf.filter(0.0)
    result2 = lpf.filter(10.0)
    
    # Should smooth the step
    assert result1 == 0.0
    assert 0 < result2 < 10.0
    
    print(f"  ✓ LowPassFilter passed (smoothed 10.0 to {result2})")


def test_high_pass_filter():
    """Test HighPassFilter"""
    print("Testing HighPassFilter...")
    
    hpf = HighPassFilter(alpha=0.5)
    
    # Test with constant input (should go to zero)
    hpf.filter(5.0)
    hpf.filter(5.0)
    result = hpf.filter(5.0)
    
    # Should attenuate DC component
    assert abs(result) < 5.0
    
    print(f"  ✓ HighPassFilter passed (attenuated DC to {result})")


def test_band_pass_filter():
    """Test BandPassFilter"""
    print("Testing BandPassFilter...")
    
    bpf = BandPassFilter(low_alpha=0.3, high_alpha=0.7)
    
    # Test with a simple signal
    result = bpf.filter(5.0)
    
    # Just check it doesn't crash and returns a value
    assert isinstance(result, float)
    
    print("  ✓ BandPassFilter passed")


def test_apply_filter_to_signal():
    """Test apply_filter_to_signal utility"""
    print("Testing apply_filter_to_signal...")
    
    signal = [1.0, 2.0, 3.0, 4.0, 5.0]
    maf = MovingAverageFilter(window_size=3)
    
    filtered = apply_filter_to_signal(signal, maf)
    
    assert len(filtered) == len(signal)
    assert all(isinstance(v, float) for v in filtered)
    
    print("  ✓ apply_filter_to_signal passed")


def test_filter_reset():
    """Test filter reset functionality"""
    print("Testing filter reset...")
    
    lpf = LowPassFilter(alpha=0.5)
    lpf.filter(10.0)
    lpf.reset()
    
    # After reset, should behave like new filter
    result = lpf.filter(5.0)
    assert result == 5.0
    
    print("  ✓ Filter reset passed")


def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Filtrage Module Tests")
    print("="*50 + "\n")
    
    try:
        test_moving_average_filter()
        test_low_pass_filter()
        test_high_pass_filter()
        test_band_pass_filter()
        test_apply_filter_to_signal()
        test_filter_reset()
        
        print("\n" + "="*50)
        print("✓ All tests passed!")
        print("="*50 + "\n")
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        return 1
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
