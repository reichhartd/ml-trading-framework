"""
This module provides functions to manage the complete dataset workflow.
"""

from .create_dataframe import create_dataframe
from .download_dataset import download_dataset
from .plot_missing_values import plot_missing_values
from .process_dataset import process_dataset
from . import data_logger as logger


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:
        logger.info("Downloading dataset")
        download_dataset()

        logger.info("Processing dataset")
        process_dataset()

        logger.info("Creating dataframe")
        df = create_dataframe()

        logger.info("Plotting missing values")
        plot_missing_values(df)

        logger.info("Dataset preparation completed successfully")
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
