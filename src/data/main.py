"""
This module provides functions to manage the complete dataset workflow.
"""

from .exploring_dataframe import exploring_dataframe
from .download_dataset import download_dataset
from .process_dataset import process_dataset
from . import data_logger as logger
from .split_dataset import split_dataset
import pandas as pd
from ..config import (
    PLOT_DATA,
    RAW_FILE,
    PROCESSED_PATH,
    TRAIN_DATA_FILE,
    VALIDATION_DATA_FILE,
    TEST_DATA_FILE,
)
from ..visualization import plot_missing_data
import os


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:
        if (
            os.path.exists(RAW_FILE)
            and os.path.exists(PROCESSED_PATH)
            and os.path.exists(TRAIN_DATA_FILE)
            and os.path.exists(VALIDATION_DATA_FILE)
            and os.path.exists(TEST_DATA_FILE)
        ):
            logger.info("Data files already exist, loading directly")

            train_data = pd.read_csv(TRAIN_DATA_FILE)
            train_data.set_index("Timestamp", inplace=True)

            valid_data = pd.read_csv(VALIDATION_DATA_FILE)
            valid_data.set_index("Timestamp", inplace=True)

            test_data = pd.read_csv(TEST_DATA_FILE)
            test_data.set_index("Timestamp", inplace=True)

            return train_data, valid_data, test_data

        logger.info("Data files don't exist, generating features")

        download_dataset()
        df = process_dataset()

        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
        df.set_index("Timestamp", inplace=True)
        df.drop(columns=["datetime"], inplace=True)

        if PLOT_DATA:
            exploring_dataframe(df)
            plot_missing_data(df)
        train_data, valid_data, test_data = split_dataset(df)

        logger.info("Dataset preparation completed successfully")
        return train_data, valid_data, test_data
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
