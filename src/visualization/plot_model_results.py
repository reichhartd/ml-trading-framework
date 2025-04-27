import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


def plot_train_validation_data(
    train_data, valid_data, target_feature="signal", dataset_type=""
):
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
