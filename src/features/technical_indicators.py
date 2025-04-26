import pandas as pd
import numpy as np


# Simple Moving Average
def calc_sma(df, period):
    return pd.Series(
        df["Close"].rolling(period, min_periods=period).mean(),
        name=f"SMA_{period}",
    )


# Exponential Moving Average
def calc_ema(df, period):
    return pd.Series(
        df["Close"].ewm(span=period, min_periods=period).mean(),
        name=f"EMA_{period}",
    )


# Momentum
def calc_mom(df, period):
    return pd.Series(df["Close"].diff(period), name=f"Momentum_{period}")


# Rate Of Change
def calc_roc(df, period):
    return pd.Series(
        ((df["Close"].diff(period - 1) / df["Close"].shift(period - 1)) * 100),
        name=f"ROC_{period}",
    )


# Relative Strength Index
def calc_rsi(df, period):
    # Calculate price changes
    price_changes = df["Close"].diff().dropna()

    # Initialize gains and losses series with zeros
    gains = price_changes * 0
    losses = gains.copy()

    # Fill gains and losses based on price movement direction
    gains[price_changes > 0] = price_changes[price_changes > 0]
    losses[price_changes < 0] = -price_changes[price_changes < 0]

    # Set first usable value as average of initial period
    gains[gains.index[period - 1]] = np.mean(
        gains[:period]
    )  # First value is average of initial gains
    gains = gains.drop(gains.index[: (period - 1)])  # Remove initialization data

    losses[losses.index[period - 1]] = np.mean(
        losses[:period]
    )  # First value is average of initial losses
    losses = losses.drop(losses.index[: (period - 1)])  # Remove initialization data

    # Calculate relative strength using exponential weighted moving average
    relative_strength = (
        gains.ewm(com=period - 1, adjust=False).mean()
        / losses.ewm(com=period - 1, adjust=False).mean()
    )

    # Calculate and return RSI values
    rsi_values = 100 - 100 / (1 + relative_strength)
    return pd.Series(rsi_values, name=f"RSI_{period}")


# Stochastic Oscillator
def calc_osc(df, period, k_or_d="k"):
    """
    Calculate Stochastic Oscillator values.

    Parameters:
    - df: DataFrame
    - period
    - k_or_d:
        - "k": Returns %K line (raw stochastic value)
        - "d": Returns %D line (3-period moving average of %K)
    """
    stoch_k = (
        (df["Close"] - df["Low"].rolling(period).min())
        / (df["High"].rolling(period).max() - df["Low"].rolling(period).min())
    ) * 100
    if k_or_d.lower() == "k":
        return pd.Series(stoch_k, name=f"Stochastic_%K_{period}")
    else:
        stoch_d = stoch_k.rolling(3).mean()
        return pd.Series(stoch_d, name=f"Stochastic_%D_{period}")
