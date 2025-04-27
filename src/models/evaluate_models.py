from sklearn.metrics import accuracy_score
import pandas as pd
from .selected_models import selected_models
import time
from . import models_logger as logger
from ..visualization import plot_train_validation_data, plot_model_evaluation_results


def evaluate_models(train_data, valid_data, target_feature="signal", dataset_type=""):
    # Handle NaN values in the dataset
    train_data = train_data.dropna()
    valid_data = valid_data.dropna()

    y_train = train_data[target_feature]
    X_train = train_data.loc[:, train_data.columns != target_feature]

    y_valid = valid_data[target_feature]
    X_valid = valid_data.loc[:, valid_data.columns != target_feature]

    logger.info(f"Dataset type: {dataset_type}")
    logger.info(f"Features used: {x_train.columns}")
    logger.info(f"Target variable: {target_feature}")
    logger.info(f"Training data shape after removing NaN values: {x_train.shape}")
    logger.info(f"Validation data shape after removing NaN values: {x_valid.shape}")

    # Visualize the train/validation data
    plot_train_validation_data(train_data, valid_data, target_feature, dataset_type)

    # Initialize result lists
    model_names = []
    train_results = []
    valid_results = []
    train_times = []

    # Evaluate models
    for name, model in selected_models:
        model_names.append(name)

        # Train and evaluate on training data
        train_start_time = time.time()
        trained_model = model.fit(x_train, y_train)
        train_result = accuracy_score(trained_model.predict(x_train), y_train)
        train_results.append(train_result)

        # Evaluate on validation data
        valid_result = accuracy_score(trained_model.predict(x_valid), y_valid)
        valid_results.append(valid_result)
        train_valid_time = time.time() - train_start_time
        train_times.append(train_valid_time)

        # Output results
        logger.info(f"{name} : Train: {train_result:.3f}, Valid: {valid_result:.3f} -> {train_valid_time:.2f}s")

    # Summarize results in DataFrame
    results_df = pd.DataFrame(
        {
            "Training": train_results,
            "Validation": valid_results,
            "Time (s)": train_times,
        },
        index=model_names,
    )

    # Visualize model evaluation results
    plot_model_evaluation_results(results_df, dataset_type)

    return results_df
