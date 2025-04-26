"""
Main entry point for the src package.

Run this module with: python -m src
"""

from src.features import prepare_features
from src.models import prepare_models
from src.utils.logger import setup_logger
from src.data import prepare_dataset

logger = setup_logger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Starting ML trading framework execution")

        train_data, valid_data, test_data = prepare_dataset()
        train_data_with_features, valid_data_with_features = prepare_features(
            train_data, valid_data
        )
        prepare_models(train_data_with_features, valid_data_with_features)

        logger.info("ML trading framework execution completed successfully")
    except Exception as e:
        logger.critical(f"ML trading framework execution failed: {e}", exc_info=True)
        exit(1)
