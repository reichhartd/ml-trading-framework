import pandas as pd
import io
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

    logger.info("Dataframe info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    logger.info(buffer.getvalue())

    pd.set_option("display.float_format", "{:.2f}".format)
    pd.set_option("display.max_columns", None)
    logger.info("Dataframe statistics:\n%s", df.describe().to_string())

    return df
