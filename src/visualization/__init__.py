"""
Visualization module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central visualization module logger
visualization_logger = setup_logger("src.visualization")


# Import and expose submodules
from .plot_missing_values import plot_missing_values
from .plot_time_series import plot_time_series
from .plot_target_correlation import plot_target_correlation

# Export public API
__all__ = ["plot_missing_values", "plot_time_series", "plot_target_correlation"]
