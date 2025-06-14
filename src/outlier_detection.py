import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_boxplots_for_outliers(df, numeric_cols, save_dir=None):
    """
    Plot box plots for given numerical columns to detect outliers.
    
    Args:
        df (pd.DataFrame): Dataframe containing the data
        numeric_cols (list): List of numerical column names to plot
        save_dir (str): Directory to save the plots (optional)
    """
    num_cols = len(numeric_cols)
    plt.figure(figsize=(6 * num_cols, 6))
    
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(1, num_cols, i)
        sns.boxplot(y=df[col])
        plt.title(f"Box plot of {col}")
    
    plt.tight_layout()
    
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(f"{save_dir}/boxplots_outliers.png")
    plt.show()
