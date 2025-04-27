from os import path, makedirs, remove
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile


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
    __TRAIN_DATA_BASELINE_FILE = path.join(__PROCESSED_FOLDER, "train_data_base.csv")
    __TRAIN_DATA_TECHNICAL_FILE = path.join(__PROCESSED_FOLDER, "train_data_tech.csv")

    __VALIDATION_DATA_FILE = path.join(__PROCESSED_FOLDER, "validation_data.csv")
    __VALIDATION_DATA_BASELINE_FILE = path.join(
        __PROCESSED_FOLDER, "validation_data_base.csv"
    )
    __VALIDATION_DATA_TECHNICAL_FILE = path.join(
        __PROCESSED_FOLDER, "validation_data_tech.csv"
    )

    __TEST_DATA_FILE = path.join(__PROCESSED_FOLDER, "test_data.csv")

    @staticmethod
    def __ensure_folders_exist():
        makedirs(Dataset.__ZIP_FOLDER, exist_ok=True)
        makedirs(Dataset.__RAW_FOLDER, exist_ok=True)
        makedirs(Dataset.__PROCESSED_FOLDER, exist_ok=True)

    @staticmethod
    def __download_dataset():
        """
        Dataset
        CSV file for the bitcoin price for the time period of 01.01.2012 10:01 until 26.04.2025 00:43.
        :return:
        """
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
