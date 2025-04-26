"""
Data module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central data module logger
data_logger = setup_logger("src.data")

# Import and expose submodules
from .main import prepare_dataset

# Export public API
__all__ = [
    "prepare_dataset",
    "data_logger",
]
