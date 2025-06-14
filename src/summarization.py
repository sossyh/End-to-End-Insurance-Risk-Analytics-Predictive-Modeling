# src/summarization.py

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load pipe-separated data file."""
    df = pd.read_csv(filepath, delimiter='|')
    df.columns = df.columns.str.strip()  # clean up any whitespace
    return df

def get_descriptive_stats(df: pd.DataFrame, numeric_cols: list) -> pd.DataFrame:
    """Return descriptive statistics of selected numerical columns."""
    return df[numeric_cols].describe().T

def get_variability(df: pd.DataFrame, numeric_cols: list) -> pd.Series:
    """Return standard deviation (variability) of selected numeric columns."""
    return df[numeric_cols].std()

def check_data_types(df: pd.DataFrame) -> pd.Series:
    """Return data types of columns."""
    return df.dtypes

def summarize_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return count of missing values in each column."""
    return df.isnull().sum()
