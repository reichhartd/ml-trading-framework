"""
Feature module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central data module logger
data_logger = setup_logger("src.features")


# Export public API
__all__ = ["data_logger"]
