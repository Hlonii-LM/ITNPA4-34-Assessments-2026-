# ==========================================
# PART 2: STREAMLIT WEB APP (2.3)
# Save this as 'app.py' and run in terminal
# ==========================================

import streamlit as st
import joblib

# Load the model saved from the Jupyter Notebook
@st.cache_resource
def load_model():
    try:
        return joblib.load('best_classifier_model.pkl')
    except FileNotFoundError:
        return None

model = load_model()

# --- Page Configuration ---
st.set_page_config(page_title="Researchly Classifier", page_icon="🔬", layout="centered")

# --- UI Header (Replicating the image) ---
st.markdown("""
    <h1 style='color: #1E293B; font-family: sans-serif;'>
    Researchly Research Abstract<br>Classifier
    </h1>
    <p style='font-size: 16px; color: #334155;'>
    This app classifies research abstracts as either AI-related or classical research.
    </p>
""", unsafe_allow_html=True)

# --- Input Area ---
st.markdown("<p style='font-weight: bold; font-size: 14px;'>Enter research abstract:</p>", unsafe_allow_html=True)
abstract_text = st.text_area(
    label="Abstract Input", 
    height=200, 
    placeholder="Artificial intelligence (AI) has become a transformative technology...",
    label_visibility="collapsed"
)

# --- Prediction Button ---
if st.button("Classify Abstract"):
    if model is None:
        st.error("Model file not found! Please run the Jupyter Notebook part first to generate 'best_classifier_model.pkl'.")
    elif abstract_text.strip() == "":
        st.warning("Please enter an abstract to classify.")
    else:
        # Make prediction
        with st.spinner('Classifying...'):
            prediction = model.predict([abstract_text])[0]
            
            # --- Prediction Display ---
            st.markdown("<h3 style='color: #1E293B;'>Prediction</h3>", unsafe_allow_html=True)
            
            # Note: Our dataset labels: 1 = sci.space (simulated AI), 0 = alt.atheism (simulated Classical)
            if prediction == 1: 
                st.success("The abstract is classified as: **artificial intelligence**")
            else:
                st.info("The abstract is classified as: **classical research**")