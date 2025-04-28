import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_matrix(
    df,
    target="",
    dataset_type="",
):
    if target not in df.columns:
        raise ValueError(f"Target variable '{target}' not found in dataframe columns")

    corr = df.corr()[target].to_frame()

    plt.figure()
    sns.heatmap(
        corr.T,
        vmin=-0.3,
        vmax=0.3,
        center=0,
        cmap="coolwarm",
        square=False,
        lw=2,
        annot=True,
        cbar=False,
    )
    plt.title(f"{dataset_type} Features - Correlation to {target}")
    plt.tight_layout()
    plt.show()
