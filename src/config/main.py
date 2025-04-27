from os import path


# Processed
PROCESSED_FOLDER = "data/processed/"
TRAIN_DATA_BASELINE_FILE = path.join(PROCESSED_FOLDER, "train_data_baseline.csv")
TRAIN_DATA_TECHNICAL_FILE = path.join(PROCESSED_FOLDER, "train_data_technical.csv")
VALIDATION_DATA_BASELINE_FILE = path.join(PROCESSED_FOLDER, "validation_data_baseline.csv")
VALIDATION_DATA_TECHNICAL_FILE = path.join(PROCESSED_FOLDER, "validation_data_technical.csv")


# Visualization
PLOT_DATA = True
# 8h * 60 min -> First 8 hours
PLOT_DATA_POINTS = 8 * 60
