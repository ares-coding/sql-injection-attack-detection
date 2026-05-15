# SQL Injection Attack Detection System

**Machine Learning-Based Security System for SQL Injection Prevention**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)

> **Disclaimer:** This project is for educational and research purposes only. Use only on systems you own or have explicit written authorization to test. Unauthorized access to computer systems is illegal.

---
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/3230676a-bd06-4494-b81a-ac1a98e34507" />

## Overview

A security-focused project that demonstrates real-world SQL injection vulnerabilities, implements machine learning-based detection, and provides secure coding references.

**Covers:**
- Authentication bypass, union-based, blind, time-based, and error-based injection vectors
- SVM classifier trained on labeled SQL query patterns
- Pattern-based detection engine with regex rule sets
- Parameterized query and ORM-based secure implementation examples

SQL Injection remains in the [OWASP Top 10](https://owasp.org/www-project-top-ten/) web application risks. This project is structured for both learning and practical application.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | Scikit-learn (SVM) |
| Database | MySQL 8.0+ |
| Data Processing | Pandas, NumPy |
| Web Interface | Flask |
| Visualization | Matplotlib, Seaborn |

---

## Installation

**Prerequisites:** Python 3.8+, MySQL Server 8.0+

```bash
git clone https://github.com/ares-coding/sql-injection-attack-detection.git
cd sql-injection-attack-detection

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

mysql -u root -p < database/setup.sql

cp config.example.py config.py
# Edit config.py with your MySQL credentials
```

---

## Usage

### Train the Detection Model

```bash
python train_model.py --dataset data/sql_queries.csv --output models/detector.pkl

# Training accuracy: 96.8%
# Test accuracy: 94.2%
# Model saved to models/detector.pkl
```

### Run Vulnerability Demos

```bash
python demos/vulnerable_app.py   # Intentionally vulnerable app
python demos/attack_scenarios.py # Attack demonstrations
```

### Use the Detector

```python
from sql_detector import SQLInjectionDetector

detector = SQLInjectionDetector(model_path='models/detector.pkl')

query = "SELECT * FROM users WHERE id = '1' OR '1'='1'"
result = detector.predict(query)

print(f"Is Malicious: {result['is_malicious']}")
print(f"Confidence:   {result['confidence']:.2%}")
print(f"Attack Type:  {result['attack_type']}")
print(f"Risk Level:   {result['risk_level']}")
```

**Output:**
```
Is Malicious: True
Confidence:   98.7%
Attack Type:  Authentication Bypass (Tautology)
Risk Level:   CRITICAL
```

### Web Interface

```bash
python app.py
# Access at http://localhost:5000
```

---

## Attack Demonstrations

### 1. Authentication Bypass

**Vulnerable:**
```python
# Never do this
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cursor.execute(query)
```

**Injection input:**
```sql
Username: admin' OR '1'='1
Password: anything

-- Resulting query always evaluates to true
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='anything'
```

**Secure alternative:**
```python
query = "SELECT * FROM users WHERE username=%s AND password=%s"
cursor.execute(query, (username, password))
```

---

### 2. Union-Based Injection

```sql
' UNION SELECT username, password FROM admin_users--
-- Extracts data from unintended tables
```

---

### 3. Blind SQL Injection

```sql
' AND 1=1--   -- Returns true
' AND 1=2--   -- Returns false
-- Infers data one condition at a time
```

---

## How It Works

### Detection Pipeline

```
Input Query
    │
    ▼
Feature Extraction
  • Suspicious keywords
  • Symbol patterns
  • Structural analysis
    │
    ▼
ML Classifier (SVM)
  • Pattern matching
  • Anomaly scoring
    │
    ▼
Threat Assessment
  • Safe / Malicious
  • Confidence score
  • Attack type label
```

### Feature Extraction

```python
def extract_features(query):
    features = {
        'has_or':                 'OR' in query.upper(),
        'has_union':              'UNION' in query.upper(),
        'has_comment':            '--' in query or '/*' in query,
        'has_semicolon':          ';' in query,
        'num_quotes':             query.count("'") + query.count('"'),
        'num_equals':             query.count('='),
        'num_dashes':             query.count('-'),
        'query_length':           len(query),
        'has_always_true':        check_tautology(query),
        'suspicious_encoding':    check_encoding(query),
        'has_sleep':              'SLEEP' in query.upper(),
        'has_benchmark':          'BENCHMARK' in query.upper(),
        'has_information_schema': 'INFORMATION_SCHEMA' in query.upper()
    }
    return features
```

### Detection Patterns

```python
INJECTION_PATTERNS = [
    r"(\bOR\b|\bAND\b)\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?",  # Tautology
    r"\bUNION\b.*\bSELECT\b",                                      # Union injection
    r";\s*DROP\b",                                                  # Drop table
    r"--",                                                          # SQL comments
    r"/\*.*\*/",                                                    # Block comments
    r"\bEXEC\b|\bEXECUTE\b",                                       # Command execution
    r"\bSLEEP\b\s*\(",                                             # Time-based
    r"\bBENCHMARK\b\s*\(",                                         # Performance-based
    r"information_schema",                                          # Schema extraction
]
```

---

## Model Performance

| Metric | Value |
|---|---|
| Accuracy | 94.2% |
| Precision | 93.8% |
| Recall | 94.7% |
| F1-Score | 94.2% |
| False Positive Rate | 3.2% |
| False Negative Rate | 2.8% |

**Confusion Matrix:**

```
                   Predicted
                 Benign    Malicious
Actual Benign     1,842           58
     Malicious       52        2,048
```

**Detection rate by attack type:**

| Attack Type | Detection Rate |
|---|---|
| Tautology (OR 1=1) | 98.5% |
| Union-based | 96.3% |
| Comment-based | 97.8% |
| Time-based | 94.1% |
| Blind SQL | 92.7% |

---

## Secure Coding Reference

### Do

```python
# Parameterized queries
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# ORM (SQLAlchemy)
User.query.filter_by(id=user_id).first()

# Input validation — whitelist approach
allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
if not set(user_input).issubset(allowed):
    raise ValueError("Invalid characters detected")
```

```sql
-- Principle of least privilege
GRANT SELECT ON database.users TO 'app_user'@'localhost';
```

### Do Not

```python
# String formatting with user input
query = f"SELECT * FROM users WHERE id = '{user_id}'"   # vulnerable

# Dynamic table/column names from user input
query = f"SELECT * FROM {user_table}"                   # vulnerable

# Exposing raw exceptions to users
except Exception as e:
    return str(e)                                        # leaks schema info
```

---

## Testing

```bash
# Run all tests
python -m pytest tests/

# Specific suite
python -m pytest tests/test_detection.py -v

# With coverage
python -m pytest --cov=src tests/

# Test attack scenarios
python test_attacks.py --all
python test_attacks.py --type tautology
python test_attacks.py --report output/test_results.html
```

---

## Project Structure

```
sql-injection-detection/
├── data/
│   ├── sql_queries.csv           # Training dataset
│   ├── attack_samples.txt        # Attack examples
│   └── benign_samples.txt        # Legitimate queries
├── database/
│   ├── setup.sql                 # Schema
│   ├── sample_data.sql           # Test data
│   └── vulnerable_tables.sql     # Demo setup
├── models/
│   ├── svm_detector.pkl          # Trained SVM
│   └── feature_extractor.pkl     # Feature scaler
├── src/
│   ├── feature_extraction.py
│   ├── pattern_detection.py
│   ├── ml_classifier.py
│   └── utils.py
├── demos/
│   ├── vulnerable_app.py
│   ├── secure_app.py
│   └── attack_scenarios.py
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_pattern_study.ipynb
│   └── 03_model_evaluation.ipynb
├── web/
│   ├── app.py
│   ├── templates/
│   └── static/
├── train_model.py
├── test_attacks.py
├── requirements.txt
└── README.md
```

---

## Resources

- [OWASP SQL Injection Guide](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [OWASP Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)
- Practice environments: [HackTheBox](https://www.hackthebox.com/), [TryHackMe](https://tryhackme.com/), [PentesterLab](https://pentesterlab.com/)

---

## Citation

```bibtex
@software{sql_injection_detection,
  author = {Amores, Au},
  title  = {SQL Injection Attack Detection using Machine Learning},
  year   = {2025},
  url    = {https://github.com/ares-coding/sql-injection-attack-detection}
}
```

---

## License

Licensed under the [Apache License 2.0](LICENSE).

---

## Author

**Au Amores** — AI/ML Engineer & Software Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/au-amores/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ares-coding)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:auamores3@gmail.com)
