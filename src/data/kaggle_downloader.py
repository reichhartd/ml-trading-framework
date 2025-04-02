"""
Script for downloading cryptocurrency data from Kaggle.
"""
import os
import subprocess
import pandas as pd
from src.config import DATA_RAW_DIR

def download_kaggle_dataset(dataset, path=DATA_RAW_DIR, unzip=True):
    """
    Downloads a Kaggle dataset.

    Args:
        dataset (str): Kaggle dataset ID (e.g., 'sudalairajkumar/cryptocurrency-historical-prices-volume')
        path (str): Path to save the data
        unzip (bool): Whether to unzip the downloaded ZIP file

    Returns:
        str: Path where the data was saved
    """
    os.makedirs(path, exist_ok=True)

    # Construct Kaggle command
    cmd = f"kaggle datasets download -d {dataset} -p {path}"
    if unzip:
        cmd += " --unzip"

    print(f"Download command: {cmd}")

    # Execute command
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"Dataset '{dataset}' successfully downloaded to {path}")
        return path
    except subprocess.CalledProcessError as e:
        print(f"Error downloading '{dataset}': {e}")
        return None

def list_and_explore_files(directory=DATA_RAW_DIR):
    """
    Lists downloaded files and provides information about CSV files.
    """
    print(f"Files in {directory}:")
    all_files = []

    # Navigate through the directory (including subdirectories)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            all_files.append(relative_path)
            print(f"- {relative_path}")

    print(f"\nFound: {len(all_files)} files")

    # Analyze CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]
    print(f"\nAnalyzing {len(csv_files)} CSV files:")

    for csv_file in csv_files:
        full_path = os.path.join(directory, csv_file)
        try:
            df = pd.read_csv(full_path)
            print(f"\nFile: {csv_file}")
            print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
            print(f"Columns: {', '.join(df.columns)}")
            if 'timestamp' in df.columns or 'date' in df.columns or 'time' in df.columns or 'Date' in df.columns:
                date_col = next(col for col in ['timestamp', 'date', 'time', 'Date'] if col in df.columns)
                min_date = df[date_col].min()
                max_date = df[date_col].max()
                print(f"Time period: {min_date} to {max_date}")
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

if __name__ == "__main__":
    # Recommended crypto datasets from Kaggle
    CRYPTO_DATASETS = [
        "sudalairajkumar/cryptocurrency-historical-prices-volume",  # Multiple cryptocurrencies, daily data
        "mczielinski/bitcoin-historical-data",  # Bitcoin minute data from multiple exchanges
        "jessevent/all-crypto-currencies-hourly-data"  # Hourly data for many cryptocurrencies
    ]

    # First dataset for BTC and ETH (daily data, multiple cryptocurrencies)
    print("Downloading the main dataset...")
    download_kaggle_dataset(CRYPTO_DATASETS[0])

    # Optional: More datasets if needed
    download_more = input("Do you want to download additional datasets? (y/n): ")
    if download_more.lower() == 'y':
        for i, dataset in enumerate(CRYPTO_DATASETS[1:], 1):
            print(f"\nDataset {i+1}/{len(CRYPTO_DATASETS)}: {dataset}")
            download = input(f"Download this dataset? (y/n): ")
            if download.lower() == 'y':
                download_kaggle_dataset(dataset)

    # Explore downloaded files
    list_and_explore_files()

    print("\nSuggestions for next steps:")
    print("1. Open the notebook 'notebooks/01_Data_Exploration.ipynb'")
    print("2. Load one of the CSV files and examine its structure")
    print("3. Implement feature engineering in the next step")