from sklearn.metrics import accuracy_score
import pandas as pd
from src.models.selected_models import selected_models
import time
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from . import models_logger as logger


def evaluate_models(train_data, valid_data, target_feature="signal", dataset_type=""):
    # Handle NaN values in the dataset
    train_data = train_data.dropna()
    valid_data = valid_data.dropna()

    y_train = train_data[target_feature]
    x_train = train_data.loc[:, train_data.columns != target_feature]

    y_valid = valid_data[target_feature]
    x_valid = valid_data.loc[:, valid_data.columns != target_feature]

    # Complete dataset for full evaluation
    x_complete = pd.concat([x_train, x_valid], axis=0)
    y_complete = pd.concat([y_train, y_valid], axis=0)

    logger.info(f"Dataset type: {dataset_type}")
    logger.info(f"Features used: {x_train.columns}")
    logger.info(f"Target variable: {target_feature}")
    logger.info(f"Training data shape after removing NaN values: {x_train.shape}")
    logger.info(f"Validation data shape after removing NaN values: {x_valid.shape}")

    # Visualize
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=train_data.index,
            y=train_data[target_feature],
            mode="lines",
            name="Training Data",
            line={"width": 0.25},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=valid_data.index,
            y=valid_data[target_feature],
            mode="lines",
            name="Validation Data",
            line={"width": 0.25},
        )
    )
    fig.update_layout(
        autosize=True,
        template="plotly_white",
        title=f"{dataset_type} Features - Training/Validation Data Visualization",
        margin=dict(l=50, r=80, t=50, b=40),
    )
    fig.show(config={"responsive": True})

    # Initialize result lists
    model_names = []
    train_results = []
    valid_results = []
    complete_results = []

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

        # Evaluate on complete dataset
        complete_start_time = time.time()
        complete_model = model.fit(x_complete, y_complete)
        complete_result = accuracy_score(complete_model.predict(x_complete), y_complete)
        complete_results.append(complete_result)
        complete_time = time.time() - complete_start_time

        # Output results
        logger.info(
            f"{name} : {train_result:.3f} & {valid_result:.3f} -> {train_valid_time:.2f}s | {complete_result:.3f} -> {complete_time:.2f}s"
        )

    # Summarize results in DataFrame
    results_df = pd.DataFrame(
        {
            "Training": train_results,
            "Validation": valid_results,
            "Complete": complete_results,
        },
        index=model_names,
    )

    # Visualize results
    sns.set(style="whitegrid")
    plt.figure()
    sns.heatmap(
        results_df,
        vmin=0.5,
        vmax=1.0,
        center=0.75,
        square=False,
        lw=2,
        annot=True,
        fmt=".3f",
        cmap="Blues",
    )
    plt.title(f"{dataset_type} Features - Accuracy Scores")
    plt.tight_layout()
    plt.show()

    return results_df
