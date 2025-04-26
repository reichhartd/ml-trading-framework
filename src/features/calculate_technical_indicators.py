from .technical_indicators import (
    calc_sma,
    calc_ema,
    calc_mom,
    calc_roc,
    calc_rsi,
    calc_osc,
)
from ..config import PLOT_DATA, PLOT_DATA_POINTS
from ..visualization import plot_time_series
from ..visualization.plot_correlation_matrix import plot_correlation_matrix


def calculate_technical_indicators(df):
    indicator_groups = {}

    df["SMA_10"] = calc_sma(df, 10)
    df["SMA_30"] = calc_sma(df, 30)
    df["SMA_200"] = calc_sma(df, 200)
    indicator_groups["Simple Moving Average"] = ["SMA_10", "SMA_30", "SMA_200"]

    df["EMA_10"] = calc_ema(df, 10)
    df["EMA_30"] = calc_ema(df, 30)
    df["EMA_200"] = calc_ema(df, 200)
    indicator_groups["Exponential Moving Average"] = ["EMA_10", "EMA_30", "EMA_200"]

    df["MOM_10"] = calc_mom(df, 10)
    df["MOM_30"] = calc_mom(df, 30)
    df["MOM_200"] = calc_mom(df, 200)
    indicator_groups["Momentum"] = ["MOM_10", "MOM_30", "MOM_200"]

    df["ROC_10"] = calc_roc(df, 10)
    df["ROC_30"] = calc_roc(df, 30)
    df["ROC_200"] = calc_roc(df, 200)
    indicator_groups["Rate of Change"] = ["ROC_10", "ROC_30", "ROC_200"]

    df["RSI_10"] = calc_rsi(df, 10)
    df["RSI_30"] = calc_rsi(df, 30)
    df["RSI_200"] = calc_rsi(df, 200)
    indicator_groups["Relative Strength Index"] = ["RSI_10", "RSI_30", "RSI_200"]

    df["STOCH_%K_10"] = calc_osc(df, 5, "k")
    df["STOCH_%K_30"] = calc_osc(df, 10, "k")
    df["STOCH_%K_200"] = calc_osc(df, 20, "k")
    indicator_groups["Stochastic Oscillator (Slow)"] = [
        "STOCH_%K_10",
        "STOCH_%K_30",
        "STOCH_%K_200",
    ]

    df["STOCH_%D_10"] = calc_osc(df, 10, "d")
    df["STOCH_%D_30"] = calc_osc(df, 30, "d")
    df["STOCH_%D_200"] = calc_osc(df, 200, "d")
    indicator_groups["Stochastic Oscillator (Fast)"] = [
        "STOCH_%D_10",
        "STOCH_%D_30",
        "STOCH_%D_200",
    ]

    if PLOT_DATA:
        df_copy = df.tail(PLOT_DATA_POINTS).copy()
        for title, indicators in indicator_groups.items():
            plot_time_series(
                df_copy[indicators],
                indicators,
                title=f"{title} (periods=10,30,200)",
            )
        plot_correlation_matrix(df, "signal")

    return df
