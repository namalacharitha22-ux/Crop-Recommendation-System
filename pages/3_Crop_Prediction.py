import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Crop Prediction",
    page_icon="🌾",
    layout="wide"
)

# Load Model
model = joblib.load("best_crop_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

st.title("🌾 Crop Recommendation System")
st.markdown("### Enter the soil and environmental values below")

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("🌱 Nitrogen (N)", min_value=0.0, value=90.0)
    P = st.number_input("🌾 Phosphorus (P)", min_value=0.0, value=42.0)
    K = st.number_input("🍃 Potassium (K)", min_value=0.0, value=43.0)
    temperature = st.number_input("🌡 Temperature (°C)", min_value=0.0, value=20.8)

with col2:
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0, value=82.0)
    ph = st.number_input("⚗ pH Value", min_value=0.0, value=6.5)
    rainfall = st.number_input("🌧 Rainfall (mm)", min_value=0.0, value=202.9)

st.markdown("")

# Predict Button
if st.button("🌱 Predict Crop", use_container_width=True):

    values = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    values = scaler.transform(values)

    prediction = model.predict(values)

    crop = encoder.inverse_transform(prediction)

    st.markdown("---")

    st.success(f"## ✅ Recommended Crop: {crop[0].title()}")

    st.balloons()

    st.info("""
### 🌾 Prediction Summary

The Machine Learning model analyzed:

- 🌱 Nitrogen
- 🌾 Phosphorus
- 🍃 Potassium
- 🌡 Temperature
- 💧 Humidity
- ⚗ pH Value
- 🌧 Rainfall

Based on these parameters, the recommended crop is shown above.
""")
