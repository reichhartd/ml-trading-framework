"""
Config module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central config module logger
data_logger = setup_logger("src.config")

# Import and expose submodules
from .main import (
    TRAIN_DATA_BASELINE_FILE,
    TRAIN_DATA_TECHNICAL_FILE,
    VALIDATION_DATA_BASELINE_FILE,
    VALIDATION_DATA_TECHNICAL_FILE,
    PLOT_DATA,
    PLOT_DATA_POINTS,
    PROCESSED_FOLDER,
)

# Export public API
__all__ = [
    "TRAIN_DATA_BASELINE_FILE",
    "TRAIN_DATA_TECHNICAL_FILE",
    "VALIDATION_DATA_BASELINE_FILE",
    "VALIDATION_DATA_TECHNICAL_FILE",
    "PLOT_DATA",
    "PLOT_DATA_POINTS",
    "PROCESSED_FOLDER",
]
