import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_numeric_distributions(df, columns, save_dir=None):
    """Plot histograms for numerical columns."""
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            plt.savefig(f"{save_dir}/{col}_hist.png")
        plt.show()

def plot_categorical_distributions(df, columns, save_dir=None):
    """Plot bar charts for categorical columns."""
    for col in columns:
        plt.figure(figsize=(10, 5))
        df[col].value_counts(dropna=False).plot(kind='bar')
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            plt.savefig(f"{save_dir}/{col}_bar.png")
        plt.show()
