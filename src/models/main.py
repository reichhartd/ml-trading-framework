from . import models_logger as logger
from .evaluate_models import evaluate_models


def prepare_models(train_data, valid_data):
    logger.info("Starting model preparation")
    try:
        evaluate_models(train_data, valid_data)

    except Exception as e:
        logger.error(f"Error preparing models: {e}", exc_info=True)
        raise
