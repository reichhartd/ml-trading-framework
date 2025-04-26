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

# Training Set (60%)
TRAIN_DATA_NAME = "train_data.csv"
TRAIN_DATA_FILE = os.path.join(PROCESSED_PATH, TRAIN_DATA_NAME)

TRAIN_DATA_BASELINE_NAME = "train_data_baseline.csv"
TRAIN_DATA_BASELINE_FILE = os.path.join(PROCESSED_PATH, TRAIN_DATA_BASELINE_NAME)

TRAIN_DATA_TECHNICAL_NAME = "train_data_technical.csv"
TRAIN_DATA_TECHNICAL_FILE = os.path.join(PROCESSED_PATH, TRAIN_DATA_TECHNICAL_NAME)

# Validation Set (20%)
VALIDATION_DATA_NAME = "validation_data.csv"
VALIDATION_DATA_FILE = os.path.join(PROCESSED_PATH, VALIDATION_DATA_NAME)

VALIDATION_DATA_BASELINE_NAME = "validation_data_baseline.csv"
VALIDATION_DATA_BASELINE_FILE = os.path.join(PROCESSED_PATH, TRAIN_DATA_BASELINE_NAME)

VALIDATION_DATA_TECHNICAL_NAME = "validation_data_technical.csv"
VALIDATION_DATA_TECHNICAL_FILE = os.path.join(PROCESSED_PATH, TRAIN_DATA_TECHNICAL_NAME)

# Test Set (20%)
TEST_DATA_NAME = "test_data.csv"
TEST_DATA_FILE = os.path.join(PROCESSED_PATH, TEST_DATA_NAME)

# Visualization
PLOT_DATA = True
# 8h * 60 min -> First 8 hours
PLOT_DATA_POINTS = 8 * 60
