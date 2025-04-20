from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os

from src.data.dataset import ZIP_PATH, RAW_PATH, ZIP_NAME


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
