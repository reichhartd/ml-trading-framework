from sklearn.metrics import accuracy_score
import pandas as pd
from .selected_models import selected_models
import time
from . import models_logger as logger
from ..visualization import plot_train_validation_data, plot_model_evaluation_results


def evaluate_models(train_data, valid_data, target_feature="signal", dataset_type=""):
    train_data = train_data.dropna()
    valid_data = valid_data.dropna()

    y_train = train_data[target_feature]
    X_train = train_data.loc[:, train_data.columns != target_feature]

    y_valid = valid_data[target_feature]
    X_valid = valid_data.loc[:, valid_data.columns != target_feature]

    logger.info(f"Dataset type: {dataset_type}")
    logger.info(f"Features used: {X_train.columns}")
    logger.info(f"Target variable: {target_feature}")
    logger.info(f"Training data shape after removing NaN values: {X_train.shape}")
    logger.info(f"Validation data shape after removing NaN values: {X_valid.shape}")

    plot_train_validation_data(train_data, valid_data, target_feature, dataset_type)

    model_names = []
    train_results = []
    valid_results = []
    train_times = []

    for name, model in selected_models:
        model_names.append(name)

        # Train and evaluate on training data
        train_start_time = time.time()
        trained_model = model.fit(X_train, y_train)
        train_result = accuracy_score(trained_model.predict(X_train), y_train)
        train_results.append(train_result)

        # Evaluate on validation data
        valid_result = accuracy_score(trained_model.predict(X_valid), y_valid)
        valid_results.append(valid_result)
        train_valid_time = time.time() - train_start_time
        train_times.append(train_valid_time)

        logger.info(f"{name} : Train: {train_result:.3f}, Valid: {valid_result:.3f} -> {train_valid_time:.2f}s")

    results_df = pd.DataFrame(
        {
            "Training": train_results,
            "Validation": valid_results,
            "Completion Time (s)": train_times,
        },
        index=model_names,
    )

    plot_model_evaluation_results(results_df, dataset_type)

    return results_df
