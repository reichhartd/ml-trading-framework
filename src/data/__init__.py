"""
Data module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central data module logger
data_logger = setup_logger("src.data")

# Import and expose submodules
from .main import prepare_dataset
from .config import PROCESSED_PATH

# Export public API
__all__ = ["prepare_dataset", "PROCESSED_PATH", "data_logger"]
