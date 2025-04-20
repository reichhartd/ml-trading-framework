import pandas as pd

from .config import PROCESSED_FILE


def create_dataframe():
    df = pd.read_csv(PROCESSED_FILE)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
    df.set_index("Timestamp", inplace=True)
    df.drop(columns=["datetime"], inplace=True)
    df.info()
    return df
