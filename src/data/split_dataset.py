import os

from .config import PROCESSED_PATH


def split_dataset(df):
    # Chronological split with 60/20/20
    train_size = int(0.6 * len(df))
    valid_size = int(0.2 * len(df))

    # Split in chronological order
    train_data = df.iloc[:train_size]
    valid_data = df.iloc[train_size : train_size + valid_size]
    test_data = df.iloc[train_size + valid_size :]

    print(f"Training set: {len(train_data)} entries")
    print(f"Validation set: {len(valid_data)} entries")
    print(f"Test set: {len(test_data)} entries")

    # Check time ranges
    print(f"Training set: {train_data.index.min()} to {train_data.index.max()}")
    print(f"Validation set: {valid_data.index.min()} to {valid_data.index.max()}")
    print(f"Test set: {test_data.index.min()} to {test_data.index.max()}")

    # Saving the split data records
    train_data.to_csv(os.path.join(PROCESSED_PATH, "train_data.csv"))
    valid_data.to_csv(os.path.join(PROCESSED_PATH, "validation_data.csv"))
    test_data.to_csv(os.path.join(PROCESSED_PATH, "test_data.csv"))
