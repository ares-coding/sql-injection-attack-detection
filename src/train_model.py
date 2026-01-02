import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

from preprocessing import load_and_prepare_data
from feature_extraction import build_feature_dataframe


def train_svm_model():
    # Load and prepare dataset
    data = load_and_prepare_data()

    # Extract features
    features_df = build_feature_dataframe(data)

    X = features_df.drop("label", axis=1)
    y = features_df["label"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Initialize SVM model
    model = SVC(kernel="linear", probability=True)

    # Train model
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.4f}")

    # Save trained model
    joblib.dump(model, "models/svm_model.pkl")
    print("Model saved to models/svm_model.pkl")


if __name__ == "__main__":
    train_svm_model()
