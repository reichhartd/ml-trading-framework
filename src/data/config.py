import os


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
