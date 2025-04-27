from os import path, makedirs, remove
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import pandas as pd
from . import data_logger as logger
from pytz import UTC
from datetime import datetime
from shutil import copy2

from .exploring_dataframe import exploring_dataframe
from ..config import PLOT_DATA
from ..visualization import plot_missing_data


class Dataset:
    # Folder
    __ZIP_FOLDER = "data/zip/"
    __RAW_FOLDER = "data/raw/"
    __PROCESSED_FOLDER = "data/processed/"

    # Files
    __ZIP_FILE = path.join(__ZIP_FOLDER, "bitcoin-historical-data.zip")
    __RAW_FILE = path.join(__RAW_FOLDER, "btcusd_1-min_data.csv")
    __PROCESSED_FILE = path.join(__PROCESSED_FOLDER, "btcusd_1-min_data_processed.csv")

    # Splits
    __TRAIN_DATA_FILE = path.join(__PROCESSED_FOLDER, "train_data.csv")
    __VALIDATION_DATA_FILE = path.join(__PROCESSED_FOLDER, "validation_data.csv")
    __TEST_DATA_FILE = path.join(__PROCESSED_FOLDER, "test_data.csv")

    @staticmethod
    def __ensure_folders_exist():
        makedirs(Dataset.__ZIP_FOLDER, exist_ok=True)
        makedirs(Dataset.__RAW_FOLDER, exist_ok=True)
        makedirs(Dataset.__PROCESSED_FOLDER, exist_ok=True)

    @staticmethod
    def __read_csv(filepath, set_index=True):
        df = pd.read_csv(filepath, low_memory=False)
        if set_index:
            df.set_index("Timestamp", inplace=True)
        return df

    @staticmethod
    def __download_dataset():
        """
        Dataset
        CSV file for the bitcoin price for the time period of 01.01.2012 10:01 until 26.04.2025 00:43.
        :return:
        """
        logger.info("Downloading dataset")

        # Ensure folders exist
        Dataset.__ensure_folders_exist()

        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(
            "mczielinski/bitcoin-historical-data", path=Dataset.__ZIP_FOLDER
        )

        # Extract zip
        zip_file = ZipFile(Dataset.__ZIP_FILE)
        zip_file.extractall(path=Dataset.__RAW_FOLDER)

        # Remove zip
        remove(Dataset.__ZIP_FILE)

    @staticmethod
    def __process_raw_dataset():
        # Check if raw file exists
        if not path.exists(Dataset.__RAW_FILE):
            Dataset.__download_dataset()

        logger.info("Processing dataset")

        # Ensure folders exist
        Dataset.__ensure_folders_exist()

        # Function to convert Unix timestamp to formatted datetime string
        def convert_timestamp(ts):
            dt = datetime.fromtimestamp(float(ts), tz=UTC)
            timezone_str = dt.strftime("%z")
            formatted_timezone = f"{timezone_str[:3]}:{timezone_str[3:]}"
            return dt.strftime("%Y-%m-%d %H:%M:%S") + formatted_timezone

        # Copy the original file to processed directory
        copy2(Dataset.__RAW_FILE, Dataset.__PROCESSED_FILE)

        # Convert Timestamp column to datetime format
        df = Dataset.__read_csv(Dataset.__PROCESSED_FILE, False)
        df["datetime"] = df["Timestamp"].apply(convert_timestamp)
        df.set_index("Timestamp", inplace=True)

        # Save the processed data
        df.to_csv(Dataset.__PROCESSED_FILE, index=False)

        return df

    @staticmethod
    def split_dataset():
        """
        Data Splitting Strategy
        For our time series, we'll split the dataset into three distinct segments:
        1. **Training Set (60%)**: The earliest portion of our chronological data used to train the model and establish
           patterns.
        2. **Validation Set (20%)**: The middle segment used to tune hyperparameters and prevent overfitting during the
           development phase.
        3. **Test Set (20%)**: The most recent data, kept completely separate until final evaluation to simulate real-world
           performance.
        This chronological splitting approach is crucial for financial time series data to prevent data leakage and maintain
        the temporal nature of the information.
        :return:
        """
        # Ensure folders exist
        Dataset.__ensure_folders_exist()

        # Check if split files already exist
        if (
            path.exists(Dataset.__TRAIN_DATA_FILE)
            and path.exists(Dataset.__VALIDATION_DATA_FILE)
            and path.exists(Dataset.__TEST_DATA_FILE)
        ):
            logger.info("Split datasets already exist, loading from files")
            train_data = Dataset.__read_csv(Dataset.__TRAIN_DATA_FILE)
            valid_data = Dataset.__read_csv(Dataset.__VALIDATION_DATA_FILE)
            test_data = Dataset.__read_csv(Dataset.__TEST_DATA_FILE)
            return train_data, valid_data, test_data

        # Check if processed file exists
        if path.exists(Dataset.__PROCESSED_FILE):
            df = Dataset.__read_csv(Dataset.__PROCESSED_FILE)
        else:
            df = Dataset.__process_raw_dataset()

        if PLOT_DATA:
            exploring_dataframe(df)
            plot_missing_data(df)

        logger.info("Splitting dataset")

        df.drop(columns=["datetime"], inplace=True)

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
        logger.info(
            f"Training set: {train_data.index.min()} to {train_data.index.max()}"
        )
        logger.info(
            f"Validation set: {valid_data.index.min()} to {valid_data.index.max()}"
        )
        logger.info(f"Test set: {test_data.index.min()} to {test_data.index.max()}")

        # Saving the split data records
        train_data.to_csv(Dataset.__TRAIN_DATA_FILE)
        valid_data.to_csv(Dataset.__VALIDATION_DATA_FILE)
        test_data.to_csv(Dataset.__TEST_DATA_FILE)

        return train_data, valid_data, test_data
