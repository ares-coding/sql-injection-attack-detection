import joblib
import pandas as pd

from preprocessing import clean_query
from feature_extraction import extract_features


def predict_query(query: str):
    # Load trained model
    model = joblib.load("models/svm_model.pkl")

    # Clean query
    cleaned = clean_query(query)

    # Extract features
    features = extract_features(cleaned)
    features_df = pd.DataFrame([features])

    # Predict
    prediction = model.predict(features_df)[0]
    probability = model.predict_proba(features_df)[0].max()

    label = "SQL Injection" if prediction == 1 else "Normal Query"

    return label, probability


if __name__ == "__main__":
    print("=== SQL Injection Detection Demo ===")
    user_query = input("Enter SQL query: ")

    label, confidence = predict_query(user_query)

    print(f"\nPrediction: {label}")
    print(f"Confidence: {confidence:.2f}")
