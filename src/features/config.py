import os

from src.data import PROCESSED_PATH

# Training Set (60%)
TRAIN_DATA_WITH_FEATURES_NAME = "train_data_with_features.csv"
TRAIN_DATA_WITH_FEATURES_FILE = os.path.join(
    PROCESSED_PATH, TRAIN_DATA_WITH_FEATURES_NAME
)

# Validation Set (20%)
VALIDATION_DATA_WITH_FEATURES_NAME = "validation_data_with_features.csv"
VALIDATION_DATA_WITH_FEATURES_FILE = os.path.join(
    PROCESSED_PATH, VALIDATION_DATA_WITH_FEATURES_NAME
)
