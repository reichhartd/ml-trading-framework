"""
Models module for the ML trading framework.
"""

from src.utils.logger import setup_logger

# Create central models module logger
models_logger = setup_logger("src.models")


# Import and expose submodules


# Export public API
__all__ = ["models_logger"]
