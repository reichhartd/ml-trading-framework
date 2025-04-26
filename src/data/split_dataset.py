import os
import pandas as pd
from . import data_logger as logger
from ..config import TRAIN_DATA_FILE, VALIDATION_DATA_FILE, TEST_DATA_FILE


def split_dataset(df=None):
    # Check if split files already exist
    if (
        os.path.exists(TRAIN_DATA_FILE)
        and os.path.exists(VALIDATION_DATA_FILE)
        and os.path.exists(TEST_DATA_FILE)
    ):
        logger.info("Split datasets already exist, loading from files")

        train_data = pd.read_csv(TRAIN_DATA_FILE)
        train_data.set_index("Timestamp", inplace=True)

        valid_data = pd.read_csv(VALIDATION_DATA_FILE)
        valid_data.set_index("Timestamp", inplace=True)

        test_data = pd.read_csv(TEST_DATA_FILE)
        test_data.set_index("Timestamp", inplace=True)

        return train_data, valid_data, test_data

    logger.info("Splitting dataset")

    # Chronological split with 60/20/20
    train_size = int(0.6 * len(df))
    valid_size = int(0.2 * len(df))

    # Split in chronological order
    train_data = df.iloc[:train_size]
    valid_data = df.iloc[train_size : train_size + valid_size]
    test_data = df.iloc[train_size + valid_size :]

    logger.info(f"Training set: {len(train_data)} entries")
    logger.info(f"Validation set: {len(valid_data)} entries")
    logger.info(f"Test set: {len(test_data)} entries")

    # Check time ranges
    logger.info(f"Training set: {train_data.index.min()} to {train_data.index.max() }")
    logger.info(f"Validation set: {valid_data.index.min()} to {valid_data.index.max()}")
    logger.info(f"Test set: {test_data.index.min()} to {test_data.index.max()}")

    # Saving the split data records
    train_data.to_csv(TRAIN_DATA_FILE)
    valid_data.to_csv(VALIDATION_DATA_FILE)
    test_data.to_csv(TEST_DATA_FILE)

    return train_data, valid_data, test_data
