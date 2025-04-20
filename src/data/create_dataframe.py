import pandas as pd

from .config import PROCESSED_FILE
from . import data_logger as logger


def create_dataframe():
    logger.info(f"Loading data from {PROCESSED_FILE}")
    df = pd.read_csv(PROCESSED_FILE)

    logger.info("Converting timestamp and setting index")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
    df.set_index("Timestamp", inplace=True)

    logger.info("Dropping redundant datetime column")
    df.drop(columns=["datetime"], inplace=True)

    logger.info(f"Dataframe created with shape: {df.shape}")
    logger.debug("Dataframe info:")
    df.info(buf=logger.debug)

    pd.set_option("display.precision", 2)
    logger.debug("Dataframe statistics:\n%s", df.describe().to_string())

    return df
