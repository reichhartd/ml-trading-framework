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
)


def prepare_features(train_data, valid_data):
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

        # Limit to the last 100,000 entries (most recent)
        train_data = train_data.tail(100000).copy()
        valid_data = valid_data.tail(100000).copy()

        train_data_baseline = generate_bull_bear_signals(train_data.copy())
        valid_data_baseline = generate_bull_bear_signals(valid_data.copy())

        train_data_baseline.to_csv(TRAIN_DATA_BASELINE_FILE)
        valid_data_baseline.to_csv(VALIDATION_DATA_BASELINE_FILE)

        train_data_technical = calculate_technical_indicators(
            train_data_baseline.copy()
        )
        valid_data_technical = calculate_technical_indicators(
            valid_data_baseline.copy()
        )

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
