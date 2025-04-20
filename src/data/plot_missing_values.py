import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from . import data_logger as logger


def plot_missing_values(df, figsize=(12, 8)):
    # Create a figure with two subplots
    fig, axes = plt.subplots(2, 1, figsize=figsize)

    # Heatmap of missing values
    sns.heatmap(df.isna(), cmap="viridis", yticklabels=False, cbar=False, ax=axes[0])
    axes[0].set_title("Missing Values Heatmap")
    axes[0].set_xlabel("Variables")
    axes[0].set_ylabel("Observations")

    # Percentage of missing values per column
    missing_percentage = df.isna().sum() / len(df) * 100
    missing_percentage.sort_values(ascending=False).plot(kind="bar", ax=axes[1])
    axes[1].set_title("Percentage of Missing Values per Column")
    axes[1].set_xlabel("Columns")
    axes[1].set_ylabel("Percentage of Missing Values")
    axes[1].grid(axis="y", linestyle="--", alpha=0.7)

    # Space between subplots
    plt.tight_layout()
    plt.show()

    # Print summary of missing values
    missing_values = df.isna().sum()
    missing_percent = missing_values / len(df) * 100
    summary = pd.DataFrame(
        {"Missing Values": missing_values, "Percentage": missing_percent}
    )
    # Only show columns with missing values
    summary = summary[summary["Missing Values"] > 0].sort_values(
        "Percentage", ascending=False
    )

    if len(summary) > 0:
        logger.info(f"Found {len(summary)} columns with missing values")
        logger.info("Missing Values Summary:\n%s", summary.to_string())
    else:
        logger.info("No missing values found in the dataset")

    return summary
