from . import feature_logger as logger
from .generate_bull_bear_signals import generate_bull_bear_signals


def prepare_features(train_data, valid_data):
    logger.info("Starting feature preparation")
    try:
        # Limit to the last 100,000 entries (most recent)
        train_data = train_data.tail(100000)
        valid_data = valid_data.tail(100000)

        generate_bull_bear_signals(train_data, verbose=True)
        generate_bull_bear_signals(valid_data, verbose=True)

    except Exception as e:
        logger.error(f"Error preparing features: {e}", exc_info=True)
        raise
