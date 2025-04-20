import matplotlib.pyplot as plt
import seaborn as sns


def plot_target_correlation(df, target="demand", figsize=(20, 1), return_corr=False):
    # Calculate correlation matrix
    corr = df.corr()[target].drop(target, errors="ignore")

    if return_corr:
        return corr

    # Plot
    plt.figure(figsize=figsize)
    sns.heatmap(
        corr.to_frame().T,
        annot=True,
        cmap="coolwarm",
        center=0,
        vmin=-0.3,
        vmax=0.3,
        cbar=False,
        linewidths=1,
    )
    plt.title(f"Feature Correlation with {target}")
    plt.subplots_adjust(bottom=0.3, top=0.8)

    plt.gcf()
