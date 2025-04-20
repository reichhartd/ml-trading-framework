import os
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
from datetime import datetime
import pytz
import shutil
import pandas as pd

# Zip
ZIP_PATH = "data/zip/"
ZIP_NAME = "bitcoin-historical-data.zip"
ZIP_FILE = os.path.join(ZIP_PATH, ZIP_NAME)

# Raw
RAW_PATH = "data/raw/"
RAW_NAME = "btcusd_1-min_data.csv"
RAW_FILE = os.path.join(RAW_PATH, RAW_NAME)

# Processed
PROCESSED_PATH = "data/processed/"
PROCESSED_NAME = "btcusd_1-min_data_processed.csv"
PROCESSED_FILE = os.path.join(PROCESSED_PATH, PROCESSED_NAME)


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


def process_dataset():
    # Validate folders exist
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Function to convert Unix timestamp to formatted datetime string
    def convert_timestamp(ts):
        dt = datetime.fromtimestamp(float(ts), tz=pytz.UTC)
        timezone_str = dt.strftime("%z")
        formatted_timezone = f"{timezone_str[:3]}:{timezone_str[3:]}"
        return dt.strftime("%Y-%m-%d %H:%M:%S") + formatted_timezone

    # Copy the original file to processed directory
    shutil.copy2(RAW_FILE, PROCESSED_FILE)

    # Convert Timestamp column to datetime format
    df = pd.read_csv(PROCESSED_FILE, low_memory=False)
    df["datetime"] = df["Timestamp"].apply(convert_timestamp)

    # Save the processed data
    df.to_csv(PROCESSED_FILE, index=False)
