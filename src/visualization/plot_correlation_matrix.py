import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_matrix(
    df,
    target="",
):
    if target not in df.columns:
        raise ValueError(f"Target variable '{target}' not found in dataframe columns")

    corr = df.corr()[target].sort_values(ascending=False).to_frame()
    corr = corr[corr.index != target]

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
    plt.title(f"Feature Correlation to {target}")
    plt.tight_layout()
    plt.show()
