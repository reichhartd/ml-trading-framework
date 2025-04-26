from . import models_logger as logger
from .evaluate_models import evaluate_models


def prepare_models(
    train_data_baseline, valid_data_baseline, train_data_technical, valid_data_technical
):
    logger.info("Starting model preparation")
    try:
        evaluate_models(
            train_data_baseline, valid_data_baseline, dataset_type="Baseline"
        )
        evaluate_models(
            train_data_technical, valid_data_technical, dataset_type="Technical"
        )

    except Exception as e:
        logger.error(f"Error preparing models: {e}", exc_info=True)
        raise
