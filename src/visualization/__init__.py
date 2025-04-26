"""
Visualization module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central visualization module logger
visualization_logger = setup_logger("src.visualization")


# Import and expose submodules
from .plot_line import plot_line
from .plot_target_correlation import plot_target_correlation

# Export public API
__all__ = ["plot_line", "plot_target_correlation"]
