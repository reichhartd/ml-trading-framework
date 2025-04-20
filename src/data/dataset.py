"""
This module provides functions to manage the complete dataset workflow.
"""

from src.utils.logger import setup_logger
from .download_dataset import download_dataset
from .process_dataset import process_dataset


logger = setup_logger(__name__)


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:
        logger.info("Downloading dataset")
        download_dataset()

        logger.info("Processing dataset")
        process_dataset()

        logger.info("Dataset preparation completed successfully")
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
