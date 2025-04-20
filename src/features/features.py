from . import feature_logger as logger
from ..data import prepare_dataset


def prepare_features():

    logger.info("Starting feature preparation")

    try:
        train_data, valid_data, test_data = prepare_dataset()
    except Exception as e:
        logger.error(f"Error preparing features: {e}", exc_info=True)
        raise
