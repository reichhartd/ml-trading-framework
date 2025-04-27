import pandas as pd
import numpy as np


def calc_sma(df, period):
    """
    Simple Moving Average (SMA)
    This indicator reveals price trends by smoothing out market fluctuations, effectively filtering out short-term noise
    from price data.
    :param df:
    :param period:
    :return:
    """
    return pd.Series(
        df["Close"].rolling(period, min_periods=period).mean(),
        name=f"SMA_{period}",
    )


def calc_ema(df, period):
    """
    Exponential Moving Average (EMA)
    This indicator reveals price trends by smoothing out market fluctuations, effectively filtering out short-term noise
    from price data.
    :param df:
    :param period:
    :return:
    """
    return pd.Series(
        df["Close"].ewm(span=period, min_periods=period).mean(),
        name=f"EMA_{period}",
    )


def calc_mom(df, period):
    """
    Momentum (MOM)
    This metric quantifies the acceleration of a security's price or volume, essentially measuring how rapidly prices
    are changing in a given direction.
    :param df:
    :param period:
    :return:
    """
    return pd.Series(df["Close"].diff(period), name=f"MOM_{period}")


def calc_roc(df, period):
    """
    Rate Of Change (ROC)
    This momentum oscillator calculates the percentage difference between current price and the price n periods ago.
    Assets displaying **elevated ROC values** typically signal overbought conditions, while **depressed ROC readings**
    often indicate oversold market states.
    :param df:
    :param period:
    :return:
    """
    return pd.Series(
        ((df["Close"].diff(period - 1) / df["Close"].shift(period - 1)) * 100),
        name=f"ROC_{period}",
    )


def calc_rsi(df, period):
    """
    Relative Strength Index (RSI)
    A momentum measurement that evaluates the speed and magnitude of recent price movements to identify potential
    overbought or oversold conditions. It operates on a scale of 0-100, with **readings above 70 suggesting an
    overbought asset** and **readings below 30 indicating an undervalued, oversold condition**.
    :param df:
    :param period:
    :return:
    """

    # Calculate price changes
    price_changes = df["Close"].diff().dropna()

    # Initialize gains and losses series with zeros
    gains = price_changes * 0
    losses = gains.copy()

    # Fill gains and losses based on price movement direction
    gains[price_changes > 0] = price_changes[price_changes > 0]
    losses[price_changes < 0] = -price_changes[price_changes < 0]

    # Set first usable value as average of initial period
    gains_start = gains.iloc[:period].mean()
    gains = gains.iloc[period - 1 :]
    gains.iloc[0] = gains_start

    losses_start = losses.iloc[:period].mean()
    losses = losses.iloc[period - 1 :]
    losses.iloc[0] = losses_start

    # Calculate relative strength using exponential weighted moving average
    relative_strength = (
        gains.ewm(com=period - 1, adjust=False).mean()
        / losses.ewm(com=period - 1, adjust=False).mean()
    )

    # Calculate and return RSI values
    rsi_values = 100 - 100 / (1 + relative_strength)
    return pd.Series(rsi_values, name=f"RSI_{period}")


def calc_osc(df, period, k_or_d="k"):
    """
    Stochastic Oscillator
    This momentum tool compares a security's closing price to its price range over a specific timeframe. The %K line
    represents the faster signal, while %D serves as the slower, more smoothed indicator.
    :param df:
    :param period:
    :param k_or_d:
        - "k": Returns %K line (raw stochastic value)
        - "d": Returns %D line (3-period moving average of %K)
    :return:
    """
    stoch_k = (
        (df["Close"] - df["Low"].rolling(period).min())
        / (df["High"].rolling(period).max() - df["Low"].rolling(period).min())
    ) * 100
    if k_or_d.lower() == "k":
        return pd.Series(stoch_k, name=f"STOCH_%K_{period}")
    else:
        stoch_d = stoch_k.rolling(3).mean()
        return pd.Series(stoch_d, name=f"STOCH_%D_{period}")
