from .technical_indicators import (
    calc_sma,
    calc_ema,
    calc_mom,
    calc_roc,
    calc_rsi,
    calc_osc,
)
from ..visualization import plot_time_series


def calculate_technical_indicators(df, plot_data=True, plot_period=None):
    indicator_groups = {}

    df["SMA_10"] = calc_sma(df, 10)
    df["SMA_30"] = calc_sma(df, 30)
    df["SMA_200"] = calc_sma(df, 200)
    indicator_groups["Simple Moving Average"] = ["MA_10", "MA_30", "MA_200"]

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

    df["STOCH_K_10"] = calc_osc(df, 10, "k")
    df["STOCH_K_30"] = calc_osc(df, 30, "k")
    df["STOCH_K_200"] = calc_osc(df, 200, "k")
    indicator_groups["Stochastic Oscillator (Fast)"] = [
        "STOCH_K_10",
        "STOCH_K_30",
        "STOCH_K_200",
    ]

    df["STOCH_D_10"] = calc_osc(df, 10, "d")
    df["STOCH_D_30"] = calc_osc(df, 30, "d")
    df["STOCH_D_200"] = calc_osc(df, 200, "d")
    indicator_groups["Stochastic Oscillator (Slow)"] = [
        "STOCH_D_10",
        "STOCH_D_30",
        "STOCH_D_200",
    ]

    if plot_data:
        plot_period_data = df if plot_period is None else df.loc[plot_period]

        for title, indicators in indicator_groups.items():
            plot_time_series(
                plot_period_data[indicators],
                indicators,
                title=f"{title} (periods=10,30,200)",
            )

    return df
