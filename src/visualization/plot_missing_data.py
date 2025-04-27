import matplotlib.pyplot as plt
import seaborn as sns
from . import visualization_logger as logger


def plot_missing_data(df):
    missing_percentage = (df.isnull().sum() / len(df) * 100).sort_values(
        ascending=False
    )

    missing_percentage = missing_percentage[missing_percentage > 0]
    if len(missing_percentage) == 0:
        logger.info("No missing values found in the dataframe.")
        return

    plt.figure()

    axes = plt.axes()
    sns.barplot(
        x=missing_percentage,
        y=missing_percentage.index,
        edgecolor="black",
        hue=missing_percentage.index,
        legend=False,
    )

    for spine_position in ["top", "right", "bottom", "left"]:
        axes.spines[spine_position].set_color("black")

    axes.spines["top"].set_visible(True)
    axes.spines["right"].set_visible(False)
    axes.spines["bottom"].set_visible(False)
    axes.spines["left"].set_visible(False)

    plt.title("Missing values (%)", size=15, fontweight="bold")
    plt.xlabel("Percent (%)")
    plt.ylabel("")

    axes.grid(axis="x", linestyle="--", alpha=0.9)

    plt.tight_layout()
    plt.show()
