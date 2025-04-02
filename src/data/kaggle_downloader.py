import kagglehub
import os
from src.config import DATA_RAW_DIR

# Make sure target directory exists
os.makedirs(DATA_RAW_DIR, exist_ok=True)

# Download directly to DATA_RAW_DIR
path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data", path=DATA_RAW_DIR)

print(f"Dataset downloaded to: {path}")
