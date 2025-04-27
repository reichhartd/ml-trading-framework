from . import models_logger as logger
from .evaluate_models import evaluate_models
from ..visualization import plot_comparative_model_performance


def prepare_models(
    train_data_baseline, valid_data_baseline, train_data_technical, valid_data_technical
):
    logger.info("Starting model preparation")
    try:
        # Evaluate each dataset type
        baseline_results = evaluate_models(
            train_data_baseline, valid_data_baseline, dataset_type="Baseline"
        )
        technical_results = evaluate_models(
            train_data_technical, valid_data_technical, dataset_type="Technical"
        )

        # Compare model performance across different feature sets
        results_dict = {"Baseline": baseline_results, "Technical": technical_results}

        # Plot comparative model performance for training accuracy
        plot_comparative_model_performance(results_dict, metric="Training")

        # Plot comparative model performance for validation accuracy
        plot_comparative_model_performance(results_dict, metric="Validation")

    except Exception as e:
        logger.error(f"Error preparing models: {e}", exc_info=True)
        raise
