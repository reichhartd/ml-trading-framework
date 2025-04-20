"""
This module provides consistent logging setup across the application.
"""

import logging
import sys
from pathlib import Path


def setup_logger(name, log_level=logging.INFO, log_file=None):
    """Configure and return a logger with consistent formatting.

    Args:
        name: Name of the logger, usually __name__
        log_level: Logging level, default is INFO
        log_file: Optional file path to write logs to

    Returns:
        Configured logger instance
    """
    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False  # Prevent duplicate logging

    # Clear existing handlers to avoid duplicates when reusing
    if logger.handlers:
        logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (optional)
    if log_file:
        # Create directory if it doesn't exist
        log_path = Path(log_file).parent
        log_path.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Global application logger
app_logger = setup_logger("ml_trading_framework")
