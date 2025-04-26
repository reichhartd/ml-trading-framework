from . import data_logger as logger
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os

from ..config import ZIP_PATH, RAW_PATH, ZIP_FILE, RAW_FILE


def download_dataset():
    # Validate folders exist
    os.makedirs(ZIP_PATH, exist_ok=True)
    os.makedirs(RAW_PATH, exist_ok=True)

    # Skip if raw file already exists
    if os.path.exists(RAW_FILE):
        return

    logger.info("Downloading dataset")

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files("mczielinski/bitcoin-historical-data", path=ZIP_PATH)

    # Extract zip
    zip_file = ZipFile(ZIP_FILE)
    zip_file.extractall(path=RAW_PATH)

    # Remove zip
    os.remove(ZIP_FILE)
