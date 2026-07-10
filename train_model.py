import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# To run this script, simply place 'malicious_phish.csv' in the same folder as this file.
csv_path = "malicious_phish.csv"

if not os.path.exists(csv_path):
    print(f"❌ Error: '{csv_path}' not found in the current directory.")
    print("Please copy your downloaded Kaggle CSV file into this folder and rename it to 'malicious_phish.csv'.")
    exit()

print("📖 Reading dataset...")
df = pd.read_csv(csv_path, nrows=50000)

print("🏷️ Mapping labels to binary values (0 = Safe, 1 = Malicious)...")
df['label'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

# 2. Hardened Feature Engineering Pipeline
def extract_features(url_list):
    features = []
    suspicious_tlds = ['.xyz', '.tk', '.cc', '.info', '.top', '.ga', '.cf', '.ml', '.biz', '.icu']
    # Upgraded keyword engine targeting payment, bank, and financial engineering anchors
    scam_keywords = ['login', 'verify', 'secure', 'bank', 'account', 'update', 'payment', 'pay', 'boleto', 'invoice']
    
    for url in url_list:
        url_str = str(url).lower()
        features.append({
            'url_length': len(url_str),
            'has_dash': 1 if '-' in url_str else 0,
            'has_at': 1 if '@' in url_str else 0,
            'has_question': 1 if '?' in url_str else 0,
            'has_equals': 1 if '=' in url_str else 0,
            'is_http': 1 if url_str.startswith('http://') else 0,
            'subdomain_count': url_str.count('.'),
            'has_double_slash': 1 if url_str.count('//') > 1 else 0,
            'is_suspicious_tld': 1 if any(tld in url_str for tld in suspicious_tlds) else 0,
            
            # 🔥 NEW EXPERT CYBERSECURITY RULES:
            'is_php_or_exe': 1 if '.php' in url_str or '.exe' in url_str else 0,
            'has_scam_keyword': 1 if any(k in url_str for k in scam_keywords) else 0,
            'digit_ratio': sum(c.isdigit() for c in url_str) / (len(url_str) + 1)
        })
    return pd.DataFrame(features)

print("⚙️ Extracting hardened security markers from 50,000 strings...")
X = extract_features(df['url'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🧠 Optimizing Random Forest Classifier weights on CPU...")
model = RandomForestClassifier(n_estimators=75, max_depth=18, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
print("✅ Training complete!")

y_pred = model.predict(X_test)
print("\n📊 --- UPDATED PERFORMANCE PROFILE ---")
print(f"Overall Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nDetailed Matrix Classification:")
print(classification_report(y_test, y_pred, target_names=['Safe (0)', 'Malicious (1)']))

# Save weights to local disk
model_filename = 'phishing_detector_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)
print(f"💾 Saved updated intelligence matrix to: '{model_filename}'")