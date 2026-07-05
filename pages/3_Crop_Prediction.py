import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("best_crop_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Crop Prediction", page_icon="🌱")

st.title("🌱 Crop Recommendation")

N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH Value", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Predict Crop"):

    sample = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    sample = scaler.transform(sample)

    prediction = model.predict(sample)

    crop = encoder.inverse_transform(prediction)

    st.success(f"🌾 Recommended Crop: {crop[0]}")
