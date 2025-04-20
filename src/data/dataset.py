"""
This module provides functions to manage the complete dataset workflow.
"""

import os
from .create_dataframe import create_dataframe
from .download_dataset import download_dataset
from .plot_missing_values import plot_missing_values
from .process_dataset import process_dataset
from . import data_logger as logger
from .split_dataset import split_dataset
from .config import TRAIN_DATA_FILE, VALIDATION_DATA_FILE, TEST_DATA_FILE


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:

        if (
            os.path.exists(TRAIN_DATA_FILE)
            and os.path.exists(VALIDATION_DATA_FILE)
            and os.path.exists(TEST_DATA_FILE)
        ):
            logger.info("Dataset files already exist, skipping preparation")
            return split_dataset()

        download_dataset()
        process_dataset()
        df = create_dataframe()
        plot_missing_values(df)
        train_data, valid_data, test_data = split_dataset(df)

        logger.info("Dataset preparation completed successfully")
        return train_data, valid_data, test_data
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
