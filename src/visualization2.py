import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_premium_distribution_by_province(df, save_dir=None):
    plt.figure(figsize=(12,6))
    sns.boxplot(x='Province', y='TotalPremium', data=df)
    plt.xticks(rotation=45)
    plt.title("Distribution of Total Premium by Province")
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/premium_by_province.png")
    plt.show()

def plot_claims_vs_premium_scatter(df, save_dir=None):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='Province', data=df, alpha=0.7)
    plt.title("Scatter Plot of Total Claims vs Total Premium by Province")
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/claims_vs_premium_scatter.png")
    plt.show()

def plot_vehicle_make_counts(df, save_dir=None):
    plt.figure(figsize=(14,6))
    top_makes = df['make'].value_counts().nlargest(10)
    sns.barplot(x=top_makes.index, y=top_makes.values, palette="viridis")
    plt.title("Top 10 Vehicle Makes by Count")
    plt.ylabel("Number of Vehicles")
    plt.xlabel("Vehicle Make")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/top_vehicle_makes.png")
    plt.show()
