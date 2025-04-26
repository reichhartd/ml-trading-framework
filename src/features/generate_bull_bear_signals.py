import numpy as np
from . import feature_logger as logger


def generate_bull_bear_signals(df, verbose=True):
    # The arbitrarily chosen window values of 10 and 60 for SMA_10 and SMA_60 respectively impact performance
    # significantly and should ideally be optimized through dedicated analysis.
    df["SMA_10"] = df["Close"].rolling(window=10, min_periods=1, center=False).mean()
    df["SMA_60"] = df["Close"].rolling(window=60, min_periods=1, center=False).mean()

    # When the Short Term Moving Average (SMA_10) exceeds the Long Term Moving Average (SMA_60),
    # the strategy generates a buy signal (1); otherwise it produces a sell signal (0).
    df["signal"] = np.where(df["SMA_10"] > df["SMA_60"], 1.0, 0.0)

    if verbose:
        logger.info(df["signal"].value_counts())
