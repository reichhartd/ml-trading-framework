import pandas as pd


def calculate_simple_moving_average(df, period):
    return pd.Series(
        df["Close"].rolling(period, min_periods=period).mean(),
        name=f"SMA_{period}",
    )


def calculate_exponential_moving_average(df, period):
    return pd.Series(
        df["Close"].ewm(span=period, min_periods=period).mean(),
        name=f"EMA_{period}",
    )


def calculate_momentum(df, period):
    return pd.Series(df["Close"].diff(period), name=f"Momentum_{period}")


def calculate_rate_of_change(df, period):
    current_price = df["Close"]
    price_n_periods_ago = df["Close"].shift(period)
    return pd.Series(
        ((current_price - price_n_periods_ago) / price_n_periods_ago) * 100,
        name=f"ROC_{period}",
    )


def calculate_relative_strength_index(df, period):
    delta = df["Close"].diff()

    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)

    avg_gain = gains.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = losses.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    epsilon = 1e-10
    rs = avg_gain / (avg_loss + epsilon)

    rsi = 100 - (100 / (1 + rs))

    return pd.Series(rsi, name=f"RSI_{period}")


def calculate_stochastic_oscillator(df, period, k_or_d="k"):
    stoch_k = (
        (df["Close"] - df["Low"].rolling(period).min())
        / (df["High"].rolling(period).max() - df["Low"].rolling(period).min())
    ) * 100
    if k_or_d.lower() == "k":
        return pd.Series(stoch_k, name=f"Stochastic_K_{period}")
    else:
        stoch_d = stoch_k.rolling(3).mean()
        return pd.Series(stoch_d, name=f"Stochastic_D_{period}")
