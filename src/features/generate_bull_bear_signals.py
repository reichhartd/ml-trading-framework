import numpy as np
from . import feature_logger as logger


def generate_bull_bear_signals(df, verbose=True):
    # Calculate 20-week SMA for minute-level data
    # 20 weeks = 20 weeks * 7 days * 24 hours * 60 minutes = 201,600 minutes
    df["SMA_20W"] = (
        df["Close"].rolling(window=201600, min_periods=1, center=False).mean()
    )

    # Calculate 21-week EMA for minute-level data
    # 21 weeks = 21 weeks * 7 days * 24 hours * 60 minutes = 211,680 minutes
    df["EMA_21W"] = df["Close"].ewm(span=211680, min_periods=1, adjust=False).mean()

    # Create Bull Market Support Band (the lower of the two indicators)
    df["Bull_Support_Band"] = df[["SMA_20W", "EMA_21W"]].min(axis=1)

    # Create signals: 1 (buy) when Close is above Bull Market Support Band, 0 (sell) otherwise
    df["signal"] = np.where(df["Close"] > df["Bull_Support_Band"], 1.0, 0.0)

    if verbose:
        logger.info(df["signal"].value_counts())
