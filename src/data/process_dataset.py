from .config import PROCESSED_FILE, RAW_FILE, PROCESSED_PATH
import os
import shutil
from datetime import datetime
import pandas as pd
import pytz
from . import data_logger as logger


def process_dataset():
    # Validate folders exist
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    # Skip if processed file already exists
    if os.path.exists(PROCESSED_FILE):
        return

    logger.info("Processing dataset")

    # Check if raw file exists
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError(
            f"Raw file {RAW_FILE} not found. Run download_dataset() first."
        )

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
