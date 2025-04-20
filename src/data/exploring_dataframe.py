import pandas as pd
import io
import os
from .config import PROCESSED_FILE
from . import data_logger as logger


def exploring_dataframe():
    logger.info("Exploring dataframe")

    # Skip if processed file doesn't exist
    if not os.path.exists(PROCESSED_FILE):
        raise FileNotFoundError(
            f"Processed file {PROCESSED_FILE} not found. Run process_dataset() first."
        )

    df = pd.read_csv(PROCESSED_FILE)

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True)
    df.set_index("Timestamp", inplace=True)

    df.drop(columns=["datetime"], inplace=True)

    logger.info("Dataframe info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    logger.info(buffer.getvalue())

    pd.set_option("display.float_format", "{:.2f}".format)
    pd.set_option("display.max_columns", None)
    logger.info("Dataframe statistics:\n%s", df.describe().to_string())

    return df
