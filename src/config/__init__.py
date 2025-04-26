"""
Config module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central config module logger
data_logger = setup_logger("src.config")

# Import and expose submodules
from .main import (
    ZIP_PATH,
    RAW_PATH,
    ZIP_FILE,
    RAW_FILE,
    PROCESSED_FILE,
    PROCESSED_PATH,
    TRAIN_DATA_FILE,
    VALIDATION_DATA_FILE,
    TEST_DATA_FILE,
    TRAIN_DATA_WITH_FEATURES_FILE,
    VALIDATION_DATA_WITH_FEATURES_FILE,
    PLOT_DATA_POINTS,
)

# Export public API
__all__ = [
    "ZIP_PATH",
    "RAW_PATH",
    "ZIP_FILE",
    "RAW_FILE",
    "PROCESSED_FILE",
    "PROCESSED_PATH",
    "TRAIN_DATA_FILE",
    "VALIDATION_DATA_FILE",
    "TEST_DATA_FILE",
    "TRAIN_DATA_WITH_FEATURES_FILE",
    "VALIDATION_DATA_WITH_FEATURES_FILE",
    "PLOT_DATA_POINTS",
]
