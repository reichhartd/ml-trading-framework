"""
This module provides functions to manage the complete dataset workflow.
"""

from .exploring_dataframe import exploring_dataframe
from .download_dataset import download_dataset
from .process_dataset import process_dataset
from . import data_logger as logger
from .split_dataset import split_dataset
import pandas as pd
from ..visualization import plot_missing_data


def prepare_dataset():
    """Prepare the dataset by downloading and processing it."""
    logger.info("Starting dataset preparation")

    try:
        download_dataset()
        df, created_from_scratch = process_dataset()

        df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
        df.set_index("Timestamp", inplace=True)
        df.drop(columns=["datetime"], inplace=True)

        if created_from_scratch:
            exploring_dataframe(df)
            plot_missing_data(df)
        train_data, valid_data, test_data = split_dataset(df)

        logger.info("Dataset preparation completed successfully")
        return train_data, valid_data, test_data
    except Exception as e:
        logger.error(f"Error preparing dataset: {e}", exc_info=True)
        raise
