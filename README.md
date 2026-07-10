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

```
## 🛡️ Real-World Edge Case Analysis: The .com Masking Problem

A core engineering highlight of this project was conducting production-level vulnerability testing using active scam URLs. During an evaluation, the baseline model encountered a **False Negative** on the following phishing URL:
`premierpaymentprocessing.com/includes/boleto-2via-07-2012.php`

### The Diagnostic

Because the scam domain utilizes an established `.com` TLD and standard English text blocks (`paymentprocessing`), it bypassed generic character counters with an initial 99.64% safety confidence score.

### The Engineering Patch

To counter this, the extraction pipeline was hardened by introducing:

1. **Targeted Behavioral Keyword Heuristics:** Scanning for specific invoice/transaction anchors (`boleto`, `payment`, `invoice`).
2. **Execution Vector Tracking:** Detecting the presence of unmasked executable scripts (`.php`, `.exe`) embedded within deeper directory paths.
3. **Digit-to-Length Ratio Calculations:** Quantifying dense numeric injection blocks often used by bad actors to fake transaction dates.

This reduced the model's confidence in the malicious asset significantly down to 88%, proving that engineering structural context reduces systemic blindspots.

---

## 🕹️ Quick Start: How to Install & Run

Follow these terminal commands line by line to clone the repository, set up your dependencies, compile the model, and launch the user interface.

### 1. Clone & Navigate

Clone the repository to your local system and move directly into the project directory:

```bash
git clone https://github.com/maheshapurvastudio/Scam-Link-Ai.git
cd Scam-Link-Ai

```

### 2. Install Lightweight Dependencies

Install the required local processing and frontend UI packages via pip:

```bash
pip install pandas scikit-learn streamlit

```

### 3. Step 1: Run the Training Model Backend

Before launching the app, you must train the machine learning brain. **Make sure your `malicious_phish.csv` dataset file is placed directly inside this project folder**, then run the training pipeline first:

```bash
python train_model.py

```

*This script will process the data, print out the 94.75% accuracy matrices, and automatically generate a saved model weights file named `phishing_detector_model.pkl` completely offline.*

### 4. Step 2: Launch the Cyberpunk Frontend UI Dashboard

Once your training script finishes and the `.pkl` file is generated, launch the interactive user application using Streamlit:

```bash
streamlit run app.py

```

---

## 🖥️ Using the Diagnostic Interface

Once the terminal launches the Streamlit network server, your web browser will open up the dashboard automatically.

1. **Input Stage:** Paste or type any suspicious link or payment URL into the input text area.
2. **Execution:** Click the neon-accented **`RUN DIAGNOSTIC SCAN`** button.
3. **Analysis Display:** The application will instantly calculate the lexical layout parameters and print a color-coded security metric:
* 🔴 **MALICIOUS PATTERNS CONFIRMED:** Displays a threat metric confidence score alerting you to high-risk script anomalies or phishing patterns.
* 🟢 **URL STATUS: VERIFIED CLEAN:** Displays a green safety confidence metric indicating a baseline secure structure.



---

## 🎯 Future Roadmap Scope

* **Natural Language Feature Overhaul:** Integrating a `TF-IDF Vectorizer` to break down strings into character n-grams to catch subtle lexical typosquatting (e.g., matching `paypa1` vs `paypal`).
* **Active Content Crawling:** Coupling the lexical engine with a lightweight web scraper to verify destination HTML page branding signatures and SSL configurations.
