import os
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile

# Zip
ZIP_PATH = "data/zip/"
ZIP_NAME = "bitcoin-historical-data.zip"
ZIP_FILE = os.path.join(ZIP_PATH, ZIP_NAME)

# Raw
RAW_PATH = "data/raw/"
RAW_NAME = "btcusd_1-min_data.csv"
RAW_FILE = os.path.join(RAW_PATH, RAW_NAME)


def download_dataset():
    # Validate folders exist
    os.makedirs(ZIP_PATH, exist_ok=True)
    os.makedirs(RAW_PATH, exist_ok=True)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files("mczielinski/bitcoin-historical-data", path=ZIP_PATH)

    # Extract zip
    zip_file = ZipFile(ZIP_PATH + ZIP_NAME)
    zip_file.extractall(path=RAW_PATH)

    # Remove zip
    os.remove(ZIP_PATH + ZIP_NAME)
