import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def avg_premium_by_region(df, region_col="Province", premium_col="TotalPremium"):
    """
    Calculate average premium per region.
    """
    avg_premium = df.groupby(region_col)[premium_col].mean().reset_index().sort_values(premium_col, ascending=False)
    return avg_premium

def plot_avg_premium_by_region(df, region_col="Province", premium_col="TotalPremium", save_dir=None):
    """
    Plot average premium by region as a bar chart.
    """
    avg_premium = avg_premium_by_region(df, region_col, premium_col)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=avg_premium, x=region_col, y=premium_col, palette="viridis")
    plt.xticks(rotation=45)
    plt.title(f"Average {premium_col} by {region_col}")
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/avg_{premium_col}_by_{region_col}.png")
    plt.show()

def plot_cover_type_distribution(df, region_col="Province", cover_col="CoverType", save_dir=None):
    """
    Plot distribution of insurance cover types across regions as grouped bar chart.
    """
    cover_counts = df.groupby([region_col, cover_col]).size().reset_index(name='counts')
    plt.figure(figsize=(14, 7))
    sns.barplot(data=cover_counts, x=region_col, y='counts', hue=cover_col)
    plt.xticks(rotation=45)
    plt.title(f"Distribution of {cover_col} by {region_col}")
    plt.legend(title=cover_col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/{cover_col}_distribution_by_{region_col}.png")
    plt.show()

def plot_make_distribution_by_region(df, region_col="Province", make_col="make", top_n=10, save_dir=None):
    """
    Plot distribution of top N vehicle makes across regions.
    """
    top_makes = df[make_col].value_counts().nlargest(top_n).index
    filtered_df = df[df[make_col].isin(top_makes)]
    make_counts = filtered_df.groupby([region_col, make_col]).size().reset_index(name='counts')
    plt.figure(figsize=(14, 7))
    sns.barplot(data=make_counts, x=region_col, y='counts', hue=make_col)
    plt.xticks(rotation=45)
    plt.title(f"Distribution of Top {top_n} Vehicle Makes by {region_col}")
    plt.legend(title=make_col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/top_{top_n}_makes_by_{region_col}.png")
    plt.show()
