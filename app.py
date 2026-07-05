import streamlit as st

st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AI Crop Recommendation System")

st.markdown("""
## Welcome 👋

This application uses **Machine Learning** to recommend the most suitable crop
based on soil nutrients and environmental conditions.

### 📌 Features

- 🏠 Home
- 📊 Dataset Analysis
- 🌾 Crop Prediction
- 📈 Model Performance
- ℹ️ About Project

👈 Use the **left sidebar** to navigate between pages.
""")

st.success("Select any page from the sidebar to continue.")
