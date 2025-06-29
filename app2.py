import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and features
model = joblib.load("XGBoost_prewelding_model.pkl")
top_features = joblib.load("features_b.pkl")

# App config
st.set_page_config(page_title="Model B: Pre-Welding Rod Estimator", layout="wide")
st.title("🔧 Model B - Welding Rod Estimator (Pre-Welding Stage)")
st.markdown("""
This app predicts **welding rod consumption (kg/ton)** just before welding begins.  
It uses real-time inputs from the production floor.
""")

# --- Input Section ---
st.header("📋 Enter Pre-Welding Inputs")

input_dict = {}
for feature in top_features:
    if 'encoded' in feature or feature in ['RT Req', 'Nozzle']:
        input_dict[feature] = st.number_input(f"{feature}", value=0, step=1)
    elif feature in ['GougRodQty', 'TotDespCastWt(Ton)', 'PouringTemp', 'TappingTemp']:
        input_dict[feature] = st.number_input(f"{feature}", value=0.0, step=0.1)
    else:
        input_dict[feature] = st.text_input(f"{feature}", value="")

# Predict button
if st.button("🚀 Predict Welding Rod Usage"):
    df_input = pd.DataFrame([input_dict])
    try:
        log_prediction = model.predict(df_input)[0]
        prediction = np.expm1(log_prediction)
        st.success(f"🔩 Estimated Welding Rod Consumption: **{prediction:.2f} kg/ton**")
    except Exception as e:
        st.error("❌ Prediction failed. Please check the input format.")
        st.exception(e)
