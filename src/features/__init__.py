"""
Feature module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central feature module logger
feature_logger = setup_logger("src.features")


# Import and expose submodules
from .features import prepare_features

# Export public API
__all__ = ["prepare_features", "feature_logger"]
