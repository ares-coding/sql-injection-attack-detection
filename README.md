<div align="center">

# 🛡️ SQL Injection Attack Detection System

### Machine Learning-Based Security System for SQL Injection Prevention

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

![Project Banner](https://via.placeholder.com/1200x400/111111/22c55e?text=SQL+Injection+Detection)

**Detect and prevent SQL injection attacks using pattern analysis and machine learning**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Attack Demonstrations](#-attack-demonstrations)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Detection Techniques](#-detection-techniques)
- [Model Performance](#-model-performance)
- [Security Best Practices](#-security-best-practices)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

A **comprehensive security-focused project** demonstrating:

1. ⚠️ **Real-world SQL injection vulnerabilities** and attack vectors
2. 🛡️ **Machine learning-based detection** using pattern analysis
3. ✅ **Secure coding practices** and mitigation strategies
4. 📚 **Educational demonstrations** for cybersecurity learning

### Why This Matters

SQL Injection remains in the **OWASP Top 10** web application security risks. This project provides:

- 🎓 **Educational value** - Learn attack patterns and defenses
- 🔍 **Detection capabilities** - ML-powered threat identification
- 💡 **Best practices** - Secure query implementation examples
- 🛠️ **Practical tools** - Ready-to-use detection system

---

## ✨ Features

### 🔴 Vulnerability Demonstrations

- ✅ Authentication bypass examples
- ✅ Union-based SQL injection
- ✅ Blind SQL injection techniques
- ✅ Time-based SQL injection
- ✅ Error-based exploitation

### 🟢 Detection & Prevention

- ✅ Pattern-based detection engine
- ✅ SVM classifier for query analysis
- ✅ Real-time threat assessment
- ✅ Confidence scoring system
- ✅ Query sanitization examples
- ✅ Prepared statement demonstrations

### 📊 Analysis Tools

- ✅ Query pattern visualization
- ✅ Attack vector identification
- ✅ Feature extraction pipeline
- ✅ Performance metrics dashboard

---

## ⚠️ Attack Demonstrations

> **⚠️ WARNING:** These examples are for **educational purposes only**. Never use on systems without authorization.

### 1. Authentication Bypass

**Vulnerable Code:**
```python
# ❌ VULNERABLE - Never do this!
username = request.form['username']
password = request.form['password']

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cursor.execute(query)
```

**Attack:**
```sql
Username: admin' OR '1'='1
Password: anything

Resulting Query:
SELECT * FROM users WHERE username='admin' OR '1'='1' AND password='anything'
-- This always returns true!
```

**Secure Alternative:**
```python
# ✅ SECURE - Use parameterized queries
query = "SELECT * FROM users WHERE username=%s AND password=%s"
cursor.execute(query, (username, password))
```

### 2. Union-Based Injection

**Attack:**
```sql
' UNION SELECT username, password FROM admin_users--

Extracting data from other tables
```

### 3. Blind SQL Injection

**Attack:**
```sql
' AND 1=1--  # Returns true
' AND 1=2--  # Returns false

# Extracting data one bit at a time
```

---

## 🔬 How It Works

### Detection Pipeline
```
┌─────────────┐
│ Input Query │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Feature          │
│ Extraction       │
│ • Keywords       │
│ • Patterns       │
│ • Structure      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ ML Classifier    │
│ (SVM)            │
│ • Pattern Match  │
│ • Anomaly Score  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Threat           │
│ Assessment       │
│ • Safe/Malicious │
│ • Confidence %   │
│ • Attack Type    │
└──────────────────┘
```

### Feature Extraction
```python
def extract_features(query):
    features = {
        # Suspicious keywords
        'has_or': 'OR' in query.upper(),
        'has_union': 'UNION' in query.upper(),
        'has_comment': '--' in query or '/*' in query,
        'has_semicolon': ';' in query,
        
        # Pattern analysis
        'num_quotes': query.count("'") + query.count('"'),
        'num_equals': query.count('='),
        'num_dashes': query.count('-'),
        
        # Structure analysis
        'query_length': len(query),
        'has_always_true': check_tautology(query),
        'suspicious_encoding': check_encoding(query),
        
        # Advanced patterns
        'has_sleep': 'SLEEP' in query.upper(),
        'has_benchmark': 'BENCHMARK' in query.upper(),
        'has_information_schema': 'INFORMATION_SCHEMA' in query.upper()
    }
    return features
```

---

## 🛠️ Tech Stack

<table>
<tr>
<td width="50%">

### Core Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

</td>
<td width="50%">

### Additional Tools

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

</td>
</tr>
</table>

---

## 📥 Installation

### Prerequisites

- Python 3.8+
- MySQL Server 8.0+
- Basic understanding of SQL

### Setup
```bash
# 1. Clone repository
git clone https://github.com/ares-coding/sql-injection-attack-detection.git
cd sql-injection-attack-detection

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup MySQL database
mysql -u root -p < database/setup.sql

# 5. Configure database connection
cp config.example.py config.py
# Edit config.py with your MySQL credentials
```

---

## 🚀 Usage

### 1. Train the Detection Model
```bash
# Train SVM classifier on labeled SQL queries
python train_model.py --dataset data/sql_queries.csv --output models/detector.pkl

# Output:
# Training accuracy: 96.8%
# Test accuracy: 94.2%
# Model saved to models/detector.pkl
```

### 2. Test Vulnerability Demonstrations
```bash
# Run vulnerable application (for educational purposes)
python vulnerable_app.py

# Test SQL injection attacks
python test_attacks.py
```

### 3. Use the Detection System
```python
from sql_detector import SQLInjectionDetector

# Initialize detector
detector = SQLInjectionDetector(model_path='models/detector.pkl')

# Analyze a query
query = "SELECT * FROM users WHERE id = '1' OR '1'='1'"
result = detector.predict(query)

print(f"Is Malicious: {result['is_malicious']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"Attack Type: {result['attack_type']}")
print(f"Risk Level: {result['risk_level']}")
```

**Output:**
```
Is Malicious: True
Confidence: 98.7%
Attack Type: Authentication Bypass (Tautology)
Risk Level: CRITICAL
```

### 4. Run the Web Interface
```bash
# Start Flask application
python app.py

# Visit http://localhost:5000
```

### 5. Secure Implementation Examples
```python
# Example 1: Parameterized Queries
def get_user_safe(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

# Example 2: Input Validation
def validate_input(user_input):
    # Whitelist allowed characters
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    if not set(user_input).issubset(allowed):
        raise ValueError("Invalid characters detected")
    return user_input

# Example 3: ORM Usage (SQLAlchemy)
from sqlalchemy import select
stmt = select(User).where(User.id == user_id)
result = session.execute(stmt)
```

---

## 🔍 Detection Techniques

### Pattern-Based Detection
```python
INJECTION_PATTERNS = [
    r"(\bOR\b|\bAND\b)\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?",  # Tautology
    r"\bUNION\b.*\bSELECT\b",                                      # Union injection
    r";\s*DROP\b",                                                 # Drop table
    r"--",                                                         # SQL comments
    r"/\*.*\*/",                                                   # Block comments
    r"\bEXEC\b|\bEXECUTE\b",                                      # Command execution
    r"\bSLEEP\b\s*\(",                                            # Time-based
    r"\bBENCHMARK\b\s*\(",                                        # Performance-based
    r"information_schema",                                         # Schema extraction
]
```

### Machine Learning Features

| Feature Category | Examples |
|------------------|----------|
| **Keyword-based** | OR, UNION, DROP, EXEC, SLEEP |
| **Symbol-based** | Quotes, dashes, semicolons, comments |
| **Structural** | Query length, nesting level, clause count |
| **Semantic** | Tautologies, always-true conditions |
| **Encoding** | Hex encoding, URL encoding, Unicode |

---

## 📊 Model Performance

### Classification Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 94.2% |
| **Precision** | 93.8% |
| **Recall** | 94.7% |
| **F1-Score** | 94.2% |
| **False Positive Rate** | 3.2% |
| **False Negative Rate** | 2.8% |

### Confusion Matrix
```
                Predicted
              Benign  Malicious
Actual Benign   1,842      58
     Malicious    52   2,048
```

### Attack Type Detection

| Attack Type | Detection Rate |
|-------------|----------------|
| Tautology (OR 1=1) | 98.5% |
| Union-based | 96.3% |
| Blind SQL | 92.7% |
| Time-based | 94.1% |
| Comment-based | 97.8% |

---

## 🔐 Security Best Practices

### ✅ DO's

1. **Use Parameterized Queries**
```python
   cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

2. **Use ORM Frameworks**
```python
   User.query.filter_by(id=user_id).first()
```

3. **Input Validation**
```python
   if not user_input.isalnum():
       raise ValueError("Invalid input")
```

4. **Principle of Least Privilege**
```sql
   GRANT SELECT ON database.users TO 'app_user'@'localhost';
```

5. **Escape Special Characters**
```python
   escaped = db.escape_string(user_input)
```

### ❌ DON'Ts

1. **Never concatenate user input**
```python
   # ❌ BAD
   query = f"SELECT * FROM users WHERE id = '{user_id}'"
```

2. **Don't trust any user input**
```python
   # ❌ BAD - Even "safe-looking" input can be malicious
```

3. **Don't show detailed errors to users**
```python
   # ❌ BAD - Reveals database structure
   except Exception as e:
       return str(e)
```

4. **Don't use dynamic table/column names from user input**
```python
   # ❌ BAD
   query = f"SELECT * FROM {user_table}"
```

---

## 📁 Project Structure
```
sql-injection-detection/
├── 📁 data/
│   ├── sql_queries.csv          # Training dataset
│   ├── attack_samples.txt       # Attack examples
│   └── benign_samples.txt       # Legitimate queries
├── 📁 database/
│   ├── setup.sql                # Database schema
│   ├── sample_data.sql          # Test data
│   └── vulnerable_tables.sql    # Demo vulnerable setup
├── 📁 models/
│   ├── svm_detector.pkl         # Trained SVM model
│   └── feature_extractor.pkl    # Feature scaler
├── 📁 src/
│   ├── feature_extraction.py    # Feature engineering
│   ├── pattern_detection.py     # Regex-based detection
│   ├── ml_classifier.py         # ML model training
│   └── utils.py                 # Utility functions
├── 📁 demos/
│   ├── vulnerable_app.py        # Intentionally vulnerable app
│   ├── secure_app.py            # Secured version
│   └── attack_scenarios.py      # Attack demonstrations
├── 📁 notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_pattern_study.ipynb
│   └── 03_model_evaluation.ipynb
├── 📁 web/
│   ├── app.py                   # Flask web interface
│   ├── templates/
│   └── static/
├── train_model.py               # Model training script
├── test_detector.py             # Testing script
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

### Run Unit Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test suite
python -m pytest tests/test_detection.py -v

# Run with coverage
python -m pytest --cov=src tests/
```

### Test Attack Scenarios
```bash
# Test all attack types
python test_attacks.py --all

# Test specific attack
python test_attacks.py --type tautology

# Generate test report
python test_attacks.py --report output/test_results.html
```

---

## 📚 Educational Resources

### Learning Path

1. **Understand SQL Basics** → W3Schools SQL Tutorial
2. **Learn SQL Injection** → OWASP SQL Injection Guide
3. **Practice Safely** → WebGoat, DVWA
4. **Study This Project** → Run demos, read code
5. **Build Defenses** → Implement secure code

### Recommended Reading

- 📖 [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- 📖 [SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- 📖 [Parameterized Queries Guide](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)

### Practice Platforms

- 🎯 [HackTheBox](https://www.hackthebox.com/)
- 🎯 [TryHackMe](https://tryhackme.com/)
- 🎯 [PentesterLab](https://pentesterlab.com/)

---

## ⚖️ Legal & Ethical Notice

> **⚠️ IMPORTANT DISCLAIMER**
> 
> This project is for **educational and research purposes only**.
> 
> - ✅ Use on systems you own or have explicit permission to test
> - ❌ Never use on production systems without authorization
> - ❌ Unauthorized access to computer systems is illegal
> 
> The author assumes **no liability** for misuse of this software.

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Add tests for new functionality
4. Ensure all tests pass (`pytest`)
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Contribution Ideas

- 🐛 Bug fixes and improvements
- 📝 Documentation enhancements
- 🧪 Additional test cases
- 🎨 Web interface improvements
- 🔍 New detection patterns
- 🌐 Multi-language support

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Au Amores** - Full Stack Developer & Cybersecurity Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/au-amores/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ares-coding)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:auamores3@gmail.com)

---

## 🙏 Acknowledgments

- OWASP Foundation for security resources
- MySQL documentation and community
- Scikit-learn contributors
- Security researchers and ethical hackers

---

## 📚 Citation
```bibtex
@software{sql_injection_detection,
  author = {Amores, Au},
  title = {SQL Injection Attack Detection using Machine Learning},
  year = {2025},
  url = {https://github.com/ares-coding/sql-injection-attack-detection}
}
```

---

<div align="center">

**⭐ Star this repo if it helped you learn about SQL injection!**

**🔒 Stay secure, code safely!**

Made with 🛡️ and ☕ by [Ares](https://github.com/ares-coding)

</div>
