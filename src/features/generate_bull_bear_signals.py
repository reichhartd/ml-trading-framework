import numpy as np

from ..config import PLOT_DATA, PLOT_DATA_POINTS
from ..visualization import plot_time_series
from ..visualization.plot_correlation_matrix import plot_correlation_matrix


def generate_bull_bear_signals(df):
    """
    Target Variable
    - We define our prediction variable `signal` using the `Close` price relative to the Bull Market Support Band (the
      lower of 20-week SMA and 21-week EMA).
    - If closing price falls below the Bull Market Support Band, it signals a bear market, otherwise a bull market.
    - The trading strategy assigns signal value = 1 (buy) in bull markets and signal value = 0 (sell) in bear markets.
    - The window values for both moving averages are configurable parameters, both of which are arbitrary, and can
      affect the results, ideally an optimisation study needs to be carried out to find optimum values.
    :param df:
    :return:
    """

    # The arbitrarily chosen window values of 10 and 60 for SMA_10 and SMA_60 respectively impact performance
    # significantly and should ideally be optimized through dedicated analysis.
    df["SMA_10"] = df["Close"].rolling(window=10, min_periods=1, center=False).mean()
    df["SMA_60"] = df["Close"].rolling(window=60, min_periods=1, center=False).mean()

    # When the Short Term Moving Average (SMA_10) exceeds the Long Term Moving Average (SMA_60),
    # the strategy generates a buy signal (1); otherwise it produces a sell signal (0).
    df["signal"] = np.where(df["SMA_10"] > df["SMA_60"], 1.0, 0.0)

    if PLOT_DATA:
        plot_time_series(df, ["Close", "signal"], "Signal (Bull-Bear-Signal)", 2)
        plot_time_series(
            df.tail(PLOT_DATA_POINTS).copy(),
            ["SMA_10", "SMA_60", "signal"],
            title="SMA_10, SMA_60, Signal (Bull-Bear-Signal)",
            secondary_y=[False, False, True],
        )
        plot_correlation_matrix(df, "signal")

    return df
