import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def calculate_monthly_changes(df, group_col, value_cols):
    """
    Calculate monthly changes (percentage change) of specified columns grouped by a column like PostalCode.
    Returns a dataframe with the changes.
    """
    df_sorted = df.sort_values(by=["TransactionMonth"])
    # Group by group_col and calculate pct_change for each value column
    df_changes = df_sorted.groupby(group_col)[value_cols].pct_change().reset_index()
    df_changes[group_col] = df_sorted[group_col].values  # ensure group_col stays aligned
    df_changes["TransactionMonth"] = df_sorted["TransactionMonth"].values
    return df_changes

def plot_correlation_matrix(df, cols, save_dir=None):
    """
    Plot and optionally save a correlation heatmap for specified columns.
    """
    corr = df[cols].corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/correlation_matrix.png")
    plt.show()

def scatter_by_group(df, x_col, y_col, group_col, save_dir=None, max_groups=10):
    """
    Scatter plot of y_col vs x_col colored by group_col.
    Limits to max_groups unique groups for clarity.
    """
    unique_groups = df[group_col].unique()[:max_groups]
    plt.figure(figsize=(10, 6))
    for group in unique_groups:
        subset = df[df[group_col] == group]
        plt.scatter(subset[x_col], subset[y_col], label=str(group), alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} by {group_col}")
    plt.legend(title=group_col)
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/scatter_{x_col}_vs_{y_col}.png")
    plt.show()
