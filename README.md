# 🛡️ Scam Link AI: Machine Learning Phishing URL Detector

A lightweight, high-performance cybersecurity asset that utilizes classical machine learning to parse raw URL strings and instantly classify them as **Safe** or **Malicious (Phishing/Scams)**. 

The entire engine runs **100% offline** on local CPU architectures, making it optimized for edge deployment or resource-constrained environments.

---

## 🚀 Core Architecture & Features

Traditional security software relies heavily on signature blacklists or strict, rigid rule sets that attackers can easily bypass by altering a single character. This project takes an engineering approach: analyzing the mathematical, structural layout (**lexical geometry**) of a URL string to predict threats before a user lands on a page.

* **High-Efficiency Backend:** Built using a Scikit-Learn `Random Forest Classifier` optimized to execute parallel core processing (`n_jobs=-1`).
* **Advanced Feature Engineering Pipeline:** Extracts 12 distinct structural, keyword, and numerical metrics from raw text inputs.
* **Interactive Cyberpunk Dashboard:** A dark-mode, responsive user interface built using Streamlit for local interactive diagnostics.

---

## 📊 Performance Metrics

Trained on a robust split subset of **50,000 data sequences** sourced from the `sid321axn/malicious-urls-dataset` on Kaggle, the model achieves strong classification metrics:

* **Overall Classification Accuracy:** 94.75%
* **Malicious Link Precision:** 96.00% (Ensures an incredibly low False Positive rate)
* **Malicious Link Recall:** 84.00% 

### Matrix Classification Profile
```text
               precision    recall  f1-score   support

    Safe (0)       0.94      0.99      0.96      7301
Malicious (1)      0.96      0.84      0.90      2699