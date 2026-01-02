# 🔐 SQL Injection Attack Detection using Machine Learning

A complete **machine learning–based security system** that detects whether an SQL query is **normal** or a **SQL injection attack** using feature engineering and an SVM classifier.

This project demonstrates an **end-to-end ML pipeline**: from dataset preparation to real-time prediction.

---

## 🧠 System Overview

The system analyzes raw SQL queries, extracts statistical and structural features, and classifies them using a trained Support Vector Machine (SVM).

### 🔄 Architecture Flow

```
SQL Query
   │
   ▼
Preprocessing
(cleaning & normalization)
   │
   ▼
Feature Extraction
(length, keywords, symbols, digits, etc.)
   │
   ▼
SVM Classifier
   │
   ▼
Prediction
(Normal / SQL Injection)
```

---

## 📂 Project Structure

```
sql-injection-attack-detection/
├── dataset/
│   ├── normal_queries.csv
│   └── sql_injection_queries.csv
├── src/
│   ├── preprocessing.py        # Query cleaning
│   ├── feature_extraction.py   # Feature engineering
│   ├── train_model.py          # SVM training
│   ├── evaluate_model.py       # Metrics & evaluation
│   └── predict.py              # Real-time prediction demo
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/ares-coding/sql-injection-attack-detection.git
cd sql-injection-attack-detection

# Install dependencies
pip install -r requirements.txt
```

---

## 🏋️ Model Training

Train the SVM model using the prepared dataset:

```bash
python src/train_model.py
```

This will generate a trained model file:

```
models/svm_model.pkl
```

---

## 📊 Model Evaluation

Evaluate the trained model using standard classification metrics:

```bash
python src/evaluate_model.py
```

**Metrics included:**

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🔮 Prediction Demo (Real-Time)

Run the prediction script:

```bash
python src/predict.py
```

### 🧪 Sample Input

```
' OR 1=1 --
```

### ✅ Sample Output

```
Prediction: SQL Injection
Confidence: 0.97
```

Another example:

**Input**

```
SELECT * FROM users WHERE id = 5
```

**Output**

```
Prediction: Normal Query
Confidence: 0.94
```

---

## 🧩 Features Used

The model is trained on handcrafted features extracted from SQL queries:

* Query length
* Number of SQL keywords
* Number of special characters
* Number of digits
* Whitespace count

These features help distinguish malicious patterns from legitimate queries.

---

## 🛡️ Why Machine Learning?

Traditional rule-based systems struggle with:

* Obfuscated SQL injection
* New attack patterns

This ML-based approach **generalizes better** and adapts to unseen attacks.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Au Amores (ares-coding)**
Software Developer & AI Engineer

---

⭐ If you find this project useful, consider starring the repository.
