import streamlit as st

st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AI Crop Recommendation System")

st.markdown("""
# Welcome 👋

This application recommends the best crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

👈 Use the sidebar to navigate through the application.
""")
