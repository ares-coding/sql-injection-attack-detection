import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from preprocessing import load_and_prepare_data
from feature_extraction import build_feature_dataframe


def evaluate_model():
    # Load trained model
    model = joblib.load("models/svm_model.pkl")

    # Load and prepare dataset
    data = load_and_prepare_data()
    features_df = build_feature_dataframe(data)

    X = features_df.drop("label", axis=1)
    y = features_df["label"]

    # Predict
    y_pred = model.predict(X)

    # Metrics
    print("Accuracy :", accuracy_score(y, y_pred))
    print("Precision:", precision_score(y, y_pred))
    print("Recall   :", recall_score(y, y_pred))
    print("F1-score :", f1_score(y, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y, y_pred))


if __name__ == "__main__":
    evaluate_model()
