"""
Models module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central models module logger
models_logger = setup_logger("src.models")


# Import and expose submodules
from .main import prepare_models

# Export public API
__all__ = ["prepare_models", "models_logger"]
