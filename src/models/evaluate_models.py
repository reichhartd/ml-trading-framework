from sklearn.metrics import accuracy_score
import pandas as pd
from src.models.selected_models import selected_models
import time


def evaluate_models(train_df, valid_df):
    target_column = "signal"
    feature_columns = [column for column in train_df.columns if column != target_column]

    x_train = train_df[feature_columns]
    y_train = train_df[target_column]
    x_valid = valid_df[feature_columns]
    y_valid = valid_df[target_column]

    # Store results
    model_names = []
    train_accuracies = []
    eval_accuracies = []
    runtimes = []

    # Evaluate each model (models is assumed to be defined externally)
    for name, model in selected_models:
        model_names.append(name)

        # Train model
        start_time = time.time()
        model.fit(x_train, y_train)

        # Evaluate on training data
        train_predictions = model.predict(x_train)
        train_accuracy = accuracy_score(train_predictions, y_train)

        # Evaluate on evaluation data
        eval_predictions = model.predict(x_valid)
        eval_accuracy = accuracy_score(eval_predictions, y_valid)

        end_time = time.time()
        runtime = end_time - start_time

        train_accuracies.append(train_accuracy)
        eval_accuracies.append(eval_accuracy)
        runtimes.append(runtime)

        print(
            f"{name}: Train Accuracy = {train_accuracy:.3f}, Eval Accuracy = {eval_accuracy:.3f}, Time = {runtime:.2f}s"
        )

    # Create results DataFrame
    results_df = pd.DataFrame(
        {
            "Model": model_names,
            "Train_Accuracy": train_accuracies,
            "Eval_Accuracy": eval_accuracies,
            "Runtime": runtimes,
        }
    )

    return results_df
