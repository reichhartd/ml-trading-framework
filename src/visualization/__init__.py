"""
Visualization module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central visualization module logger
visualization_logger = setup_logger("src.visualization")


# Import and expose submodules
from .plot_correlation_matrix import plot_correlation_matrix
from .plot_missing_data import plot_missing_data
from .plot_time_series import plot_time_series

# Export public API
__all__ = ["plot_missing_data", "plot_time_series", "plot_correlation_matrix"]
