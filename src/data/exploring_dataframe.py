import pandas as pd
import io
from . import data_logger as logger


def exploring_dataframe(df=None):
    logger.info("Exploring dataframe")

    logger.info("Dataframe info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    logger.info(buffer.getvalue())

    pd.set_option("display.float_format", "{:.2f}".format)
    pd.set_option("display.max_columns", None)
    logger.info("Dataframe statistics:\n%s", df.describe().to_string())

    return df
