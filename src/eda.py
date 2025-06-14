# src/eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    return pd.read_csv(filepath, delimiter='\t')

def summarize_data(df):
    print("\nDescriptive Statistics:\n", df.describe())
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())

def plot_distributions(df, numeric_cols, output_dir):
    for col in numeric_cols:
        if col in df.columns:
            sns.histplot(df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.savefig(os.path.join(output_dir, f'{col}_hist.png'))
            plt.clf()
        else:
            print(f"Warning: Column '{col}' not found in DataFrame")


def plot_categorical(df, col, output_dir):
    df[col].value_counts().plot(kind='bar')
    plt.title(f'{col} Distribution')
    plt.savefig(os.path.join(output_dir, f'{col}_bar.png'))
    plt.clf()

def plot_scatter(df, x, y, hue, output_dir):
    sns.scatterplot(x=x, y=y, hue=hue, data=df)
    plt.title(f'{x} vs {y} by {hue}')
    plt.savefig(os.path.join(output_dir, f'{x}_vs_{y}_by_{hue}.png'))
    plt.clf()

def plot_correlation(df, output_dir):
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
    plt.clf()

def plot_boxplots(df, numeric_cols, output_dir):
    for col in numeric_cols:
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.savefig(os.path.join(output_dir, f'{col}_box.png'))
        plt.clf()
