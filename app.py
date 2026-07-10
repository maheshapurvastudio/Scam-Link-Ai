import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

# Custom injection for dark mode cyberpunk visuals
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    h1 { color: #00FF66; font-family: 'Courier New', monospace; }
    .stButton>button { 
        background-color: #00FF66; color: #000000; 
        font-weight: bold; border-radius: 5px; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ SCAM LINK AI")
st.subheader("Machine Learning Phishing URL Detector")
st.write("Input an engineering or transactional URL payload below to calculate live security metrics.")

@st.cache_resource
def load_security_model():
    with open('phishing_detector_model.pkl', 'rb') as f:
        return pickle.load(f)

try:
    model = load_security_model()
except FileNotFoundError:
    st.error("❌ Model weights file 'phishing_detector_model.pkl' not found! Execute your training script first.")
    st.stop()

# Match feature extraction mapping exactly
def extract_features(url_str):
    suspicious_tlds = ['.xyz', '.tk', '.cc', '.info', '.top', '.ga', '.cf', '.ml', '.biz', '.icu']
    scam_keywords = ['login', 'verify', 'secure', 'bank', 'account', 'update', 'payment', 'pay', 'boleto', 'invoice']
    url_str = str(url_str).lower()
    
    features = {
        'url_length': len(url_str),
        'has_dash': 1 if '-' in url_str else 0,
        'has_at': 1 if '@' in url_str else 0,
        'has_question': 1 if '?' in url_str else 0,
        'has_equals': 1 if '=' in url_str else 0,
        'is_http': 1 if url_str.startswith('http://') else 0,
        'subdomain_count': url_str.count('.'),
        'has_double_slash': 1 if url_str.count('//') > 1 else 0,
        'is_suspicious_tld': 1 if any(tld in url_str for tld in suspicious_tlds) else 0,
        
        # Hardened updates
        'is_php_or_exe': 1 if '.php' in url_str or '.exe' in url_str else 0,
        'has_scam_keyword': 1 if any(k in url_str for k in scam_keywords) else 0,
        'digit_ratio': sum(c.isdigit() for c in url_str) / (len(url_str) + 1)
    }
    return pd.DataFrame([features])

user_input = st.text_input("Enter URL to Scan:", placeholder="https://example.com/path/to/file.php")

if st.button("RUN DIAGNOSTIC SCAN"):
    if user_input.strip() == "":
        st.warning("Please input a text sequence to continue.")
    else:
        processed_features = extract_features(user_input)
        prediction = model.predict(processed_features)[0]
        probabilities = model.predict_proba(processed_features)[0]
        
        st.markdown("---")
        if prediction == 1:
            confidence = probabilities[1] * 100
            st.error(f"🚨 **ALERT: MALICIOUS PATTERNS CONFIRMED**")
            st.metric(label="Threat Metric Confidence", value=f"{confidence:.2f}%")
            st.write("Flagged: Contains structural anomalies, active script target configurations, or signature blacklisted threat vectors.")
        else:
            confidence = probabilities[0] * 100
            st.success(f"🟢 **URL STATUS: VERIFIED CLEAN**")
            st.metric(label="Safety Verification Confidence", value=f"{confidence:.2f}%")
            st.write("Structural markers indicate a baseline safe domain layout architecture.")