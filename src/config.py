"""
Configuration file for the ML trading framework.
"""

# Data paths
DATA_RAW_DIR = "data/raw"
DATA_PROCESSED_DIR = "data/processed"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

# Feature Engineering
WINDOW_SIZES = [5, 10, 20] # For moving averages