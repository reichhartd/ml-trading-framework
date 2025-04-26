from .technical_indicators import (
    calculate_simple_moving_average,
    calculate_exponential_moving_average,
    calculate_momentum,
    calculate_rate_of_change,
    calculate_relative_strength_index,
    calculate_stochastic_oscillator,
)
from ..visualization import plot_line


def calculate_technical_indicators(df, plot_data=True, plot_period=None):
    indicator_groups = {}

    df["MA10"] = calculate_simple_moving_average(df, 10)
    df["MA30"] = calculate_simple_moving_average(df, 30)
    df["MA200"] = calculate_simple_moving_average(df, 200)
    indicator_groups["Simple Moving Average"] = ["MA10", "MA30", "MA200"]

    df["EMA10"] = calculate_exponential_moving_average(df, 10)
    df["EMA30"] = calculate_exponential_moving_average(df, 30)
    df["EMA200"] = calculate_exponential_moving_average(df, 200)
    indicator_groups["Exponential Moving Average"] = ["EMA10", "EMA30", "EMA200"]

    df["MOM10"] = calculate_momentum(df, 10)
    df["MOM30"] = calculate_momentum(df, 30)
    df["MOM200"] = calculate_momentum(df, 200)
    indicator_groups["Momentum"] = ["MOM10", "MOM30", "MOM200"]

    df["ROC10"] = calculate_rate_of_change(df, 10)
    df["ROC30"] = calculate_rate_of_change(df, 30)
    df["ROC200"] = calculate_rate_of_change(df, 200)
    indicator_groups["Rate of Change"] = ["ROC10", "ROC30", "ROC200"]

    df["RSI10"] = calculate_relative_strength_index(df, 10)
    df["RSI30"] = calculate_relative_strength_index(df, 30)
    df["RSI200"] = calculate_relative_strength_index(df, 200)
    indicator_groups["Relative Strength Index"] = ["RSI10", "RSI30", "RSI200"]

    df["STOCH_K_10"] = calculate_stochastic_oscillator(df, 10, "k")
    df["STOCH_K_30"] = calculate_stochastic_oscillator(df, 30, "k")
    df["STOCH_K_200"] = calculate_stochastic_oscillator(df, 200, "k")
    indicator_groups["Stochastic Oscillator (Fast)"] = [
        "STOCH_K_10",
        "STOCH_K_30",
        "STOCH_K_200",
    ]

    df["STOCH_D_10"] = calculate_stochastic_oscillator(df, 10, "d")
    df["STOCH_D_30"] = calculate_stochastic_oscillator(df, 30, "d")
    df["STOCH_D_200"] = calculate_stochastic_oscillator(df, 200, "d")
    indicator_groups["Stochastic Oscillator (Slow)"] = [
        "STOCH_D_10",
        "STOCH_D_30",
        "STOCH_D_200",
    ]

    if plot_data:
        plot_period_data = df if plot_period is None else df.loc[plot_period]

        for title, indicators in indicator_groups.items():
            plot_line(
                plot_period_data[indicators],
                indicators,
                title=f"{title} (periods=10,30,200)",
            )

    return df
