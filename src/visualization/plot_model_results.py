import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_train_validation_data(train_data, valid_data, target_feature="signal", dataset_type=""):
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


def plot_model_evaluation_results(results_df, dataset_type=""):
    sns.set(style="whitegrid")
    plt.figure()
    performance_cols = [col for col in results_df.columns if col != "Completion Time (s)"]
    time_df = results_df[["Completion Time (s)"]]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [len(performance_cols), 1]})
    sns.heatmap(
        results_df[performance_cols],
        vmin=0.5,
        vmax=1.0,
        center=0.75,
        square=False,
        lw=2,
        annot=True,
        fmt=".3f",
        cmap="RdYlGn",
        ax=ax1,
    )
    sns.heatmap(time_df, square=False, lw=2, annot=True, fmt=".2f", cmap="Blues", ax=ax2)
    plt.suptitle(f"{dataset_type} Features - Model Performance Metrics")
    plt.tight_layout()
    plt.show()


def plot_comparative_model_performance(results_dict, metric="accuracy"):
    plt.figure()

    # Extract model names and performance values
    feature_sets = list(results_dict.keys())
    all_models = set()
    for df in results_dict.values():
        all_models.update(df.index)

    all_models = sorted(list(all_models))
    data = []

    for model in all_models:
        model_data = []
        for feature_set in feature_sets:
            if model in results_dict[feature_set].index:
                model_data.append(results_dict[feature_set].loc[model, metric])
            else:
                model_data.append(np.nan)
        data.append(model_data)

    # Create DataFrame for plotting
    plot_df = pd.DataFrame(data, index=all_models, columns=feature_sets)

    # Plot
    ax = plot_df.plot(kind="bar")
    plt.title(f"Comparative Model Performance ({metric})")
    plt.xlabel("Models")
    plt.ylabel(f"{metric.capitalize()} Score")
    plt.xticks(rotation=45)
    plt.legend(title="Feature Sets")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Add value labels on top of bars
    for i, container in enumerate(ax.containers):
        ax.bar_label(container, fmt="%.3f", padding=3)

    plt.show()
