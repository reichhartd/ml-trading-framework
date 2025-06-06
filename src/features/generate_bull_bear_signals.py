import numpy as np

from ..config import PLOT_DATA, PLOT_DATA_POINTS
from ..visualization import plot_time_series
from ..visualization.plot_correlation_matrix import plot_correlation_matrix


def generate_bull_bear_signals(df):
    """
    Target Variable
    - We define our prediction variable `signal` based on the relationship between Short-Term (10-minute) and
      Long-Term (60-minute) Simple Moving Averages (SMA).
    - When the 10-minute SMA exceeds the 60-minute SMA, it signals a bullish market; otherwise a bearish market.
    - The trading strategy assigns signal value = 1 (buy) in bull markets and signal value = 0 (sell) in bear markets.
    - The window values for both moving averages (10 and 60) are arbitrarily chosen and can affect the results.
    :param df:
    :return:
    """
    sma_10 = df["Close"].rolling(window=10, min_periods=1, center=False).mean()
    sma_60 = df["Close"].rolling(window=60, min_periods=1, center=False).mean()

    # When the Short Term Moving Average (SMA_10) exceeds the Long Term Moving Average (SMA_60),
    # the strategy generates a buy signal (1); otherwise it produces a sell signal (0).
    df["signal"] = np.where(sma_10 > sma_60, 1.0, 0.0)

    if PLOT_DATA:
        plot_time_series(df, ["Close", "signal"], "Signal (Bull-Bear-Signal)", 2, dataset_type="Baseline")

        temp_df = df.copy()
        temp_df["SMA_10"] = sma_10
        temp_df["SMA_60"] = sma_60

        plot_time_series(
            temp_df.tail(PLOT_DATA_POINTS).copy(),
            ["SMA_10", "SMA_60", "signal"],
            title="SMA_10, SMA_60, Signal (Bull-Bear-Signal)",
            secondary_y=[False, False, True],
            dataset_type="Baseline",
        )
        plot_correlation_matrix(df, "signal", dataset_type="Baseline")

    return df
