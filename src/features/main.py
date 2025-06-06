from . import feature_logger as logger
from .calculate_technical_indicators import calculate_technical_indicators
from .generate_bull_bear_signals import generate_bull_bear_signals
import os
import pandas as pd

from ..config import (
    TRAIN_DATA_BASELINE_FILE,
    VALIDATION_DATA_BASELINE_FILE,
    TRAIN_DATA_TECHNICAL_FILE,
    VALIDATION_DATA_TECHNICAL_FILE,
    DATA_LIMIT,
)


def prepare_features(train_data, valid_data):
    """
    Baseline Features
    The baseline features include: `Timestamp`, `Open`, `High`, `Low`, `Close`, `Volume`.
    - Working with the full index dataset (7.0M entries) can lead to excessive training times.
    - We'll restrict our dataset to the most recent `100,000` data points, which are likely more relevant for future
      predictions.
    - Note that a `training period` of only two months may not capture all relevant trends, despite containing
      substantial data.
    :param train_data:
    :param valid_data:
    :return:
    """
    logger.info("Starting feature preparation")
    try:
        if (
            os.path.exists(TRAIN_DATA_BASELINE_FILE)
            and os.path.exists(VALIDATION_DATA_BASELINE_FILE)
            and os.path.exists(TRAIN_DATA_TECHNICAL_FILE)
            and os.path.exists(VALIDATION_DATA_TECHNICAL_FILE)
        ):
            logger.info("Feature files already exist, loading directly")

            train_data_baseline = pd.read_csv(TRAIN_DATA_BASELINE_FILE)
            train_data_baseline.set_index("Timestamp", inplace=True)

            valid_data_baseline = pd.read_csv(VALIDATION_DATA_BASELINE_FILE)
            valid_data_baseline.set_index("Timestamp", inplace=True)

            train_data_technical = pd.read_csv(TRAIN_DATA_TECHNICAL_FILE)
            train_data_technical.set_index("Timestamp", inplace=True)

            valid_data_technical = pd.read_csv(VALIDATION_DATA_TECHNICAL_FILE)
            valid_data_technical.set_index("Timestamp", inplace=True)

            return (
                train_data_baseline,
                valid_data_baseline,
                train_data_technical,
                valid_data_technical,
            )

        logger.info("Feature files don't exist, generating features")

        if DATA_LIMIT is not None:
            logger.info(f"Limiting datasets to the last {DATA_LIMIT} entries")
            train_data = train_data.tail(DATA_LIMIT).copy()
            valid_data = valid_data.tail(DATA_LIMIT).copy()
        else:
            logger.info("Using full dataset without limit")
            train_data = train_data.copy()
            valid_data = valid_data.copy()

        train_data_baseline = generate_bull_bear_signals(train_data.copy())
        valid_data_baseline = generate_bull_bear_signals(valid_data.copy())

        train_data_baseline.to_csv(TRAIN_DATA_BASELINE_FILE)
        valid_data_baseline.to_csv(VALIDATION_DATA_BASELINE_FILE)

        train_data_technical = calculate_technical_indicators(train_data_baseline.copy())
        valid_data_technical = calculate_technical_indicators(valid_data_baseline.copy())

        train_data_technical.to_csv(TRAIN_DATA_TECHNICAL_FILE)
        valid_data_technical.to_csv(VALIDATION_DATA_TECHNICAL_FILE)

        return (
            train_data_baseline,
            valid_data_baseline,
            train_data_technical,
            valid_data_technical,
        )

    except Exception as e:
        logger.error(f"Error preparing features: {e}", exc_info=True)
        raise
