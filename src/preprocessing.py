import pandas as pd
import re

def clean_query(query: str) -> str:
    """
    Clean and normalize SQL queries for ML processing.
    """
    if not isinstance(query, str):
        return ""

    # Convert to lowercase
    query = query.lower()

    # Remove extra whitespace
    query = re.sub(r"\s+", " ", query)

    # Strip leading/trailing spaces
    query = query.strip()

    return query


def load_and_prepare_data():
    """
    Load normal and SQL injection datasets, clean queries,
    and return a combined DataFrame.
    """
    normal_df = pd.read_csv("dataset/normal_queries.csv")
    injection_df = pd.read_csv("dataset/sql_injection_queries.csv")

    df = pd.concat([normal_df, injection_df], ignore_index=True)

    df["clean_query"] = df["query"].apply(clean_query)

    return df


if __name__ == "__main__":
    df = load_and_prepare_data()
    print(df.head())
    print("\nDataset size:", len(df))
