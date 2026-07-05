import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 AI Crop Recommendation System")

st.markdown("""
# Welcome 👋

Welcome to the **AI Crop Recommendation System**.

This application helps farmers and agricultural professionals choose the most suitable crop based on:

- 🌱 Nitrogen (N)
- 🌱 Phosphorus (P)
- 🌱 Potassium (K)
- 🌡 Temperature
- 💧 Humidity
- ⚗ pH Value
- 🌧 Rainfall

---

## 📌 Available Pages

- 🏠 Home
- 📊 Dataset Analysis
- 🌾 Crop Prediction
- 📈 Model Performance
- ℹ️ About Project

---

### 🚀 How to Use

1. Open **Crop Prediction** page.
2. Enter soil and weather values.
3. Click **Predict Crop**.
4. View the recommended crop.

👈 Use the left sidebar to navigate between pages.
""")

st.success("Ready to explore the application!")
