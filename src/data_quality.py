def summarize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Return count and percentage of missing values in each column."""
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100
    missing_df = pd.DataFrame({
        "MissingCount": missing_count,
        "MissingPercent": missing_percent.round(2)
    })
    missing_df = missing_df[missing_df["MissingCount"] > 0]
    return missing_df.sort_values(by="MissingCount", ascending=False)
