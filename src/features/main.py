from . import feature_logger as logger
from .calculate_technical_indicators import calculate_technical_indicators
from .generate_bull_bear_signals import generate_bull_bear_signals
from ..config import TRAIN_DATA_WITH_FEATURES_FILE, VALIDATION_DATA_WITH_FEATURES_FILE
from ..data import to_timestamp_csv
from ..visualization import plot_target_correlation


def prepare_features(train_data, valid_data):
    logger.info("Starting feature preparation")
    try:
        # Limit to the last 100,000 entries (most recent)
        train_data = train_data.tail(100000).copy()
        valid_data = valid_data.tail(100000).copy()

        generate_bull_bear_signals(train_data)
        generate_bull_bear_signals(valid_data)

        calculate_technical_indicators(train_data)
        calculate_technical_indicators(valid_data)

        plot_target_correlation(train_data, "signal")

        train_data.to_csv(TRAIN_DATA_WITH_FEATURES_FILE)
        valid_data.to_csv(VALIDATION_DATA_WITH_FEATURES_FILE)

    except Exception as e:
        logger.error(f"Error preparing features: {e}", exc_info=True)
        raise
