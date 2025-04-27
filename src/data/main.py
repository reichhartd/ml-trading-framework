"""
This module provides functions to manage the complete dataset workflow.
"""

from .dataset import Dataset
from . import data_logger as logger


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:
        train_data, valid_data, test_data = Dataset.split_dataset()
        logger.info("Dataset preparation completed successfully")
        return train_data, valid_data, test_data
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
