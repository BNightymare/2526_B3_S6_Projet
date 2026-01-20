"""
Test module for main functionality

This module contains basic tests for the main module.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


def test_main():
    """Test the main function executes without errors"""
    main()


if __name__ == "__main__":
    test_main()
    print("All tests passed!")
