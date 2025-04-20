"""
Main entry point for the src package.

Run this module with: python -m src
"""

from src.utils.logger import setup_logger
from src.data import prepare_dataset

logger = setup_logger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Starting ML trading framework execution")
        prepare_dataset()
        logger.info("ML trading framework execution completed successfully")
    except Exception as e:
        logger.critical(f"ML trading framework execution failed: {e}", exc_info=True)
        exit(1)
