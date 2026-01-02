import pandas as pd

SQL_KEYWORDS = [
    "select", "insert", "update", "delete",
    "drop", "union", "or", "and", "where"
]

SPECIAL_CHARS = ["'", "\"", ";", "--", "#", "="]


def extract_features(query: str) -> dict:
    """
    Extract numerical features from a SQL query.
    """
    features = {}

    q = query.lower()

    features["length"] = len(q)
    features["num_special_chars"] = sum(q.count(c) for c in SPECIAL_CHARS)
    features["num_keywords"] = sum(1 for kw in SQL_KEYWORDS if kw in q)
    features["num_spaces"] = q.count(" ")
    features["num_digits"] = sum(c.isdigit() for c in q)

    return features


def build_feature_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert cleaned queries into a feature DataFrame.
    """
    feature_rows = df["clean_query"].apply(extract_features)

    features_df = pd.DataFrame(list(feature_rows))
    features_df["label"] = df["label"].values

    return features_df


if __name__ == "__main__":
    from preprocessing import load_and_prepare_data

    data = load_and_prepare_data()
    features = build_feature_dataframe(data)

    print(features.head())
