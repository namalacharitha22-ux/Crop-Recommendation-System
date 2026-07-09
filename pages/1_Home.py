import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AI Crop Recommendation System")

st.markdown("""
## 👋 Welcome

Welcome to the **AI Crop Recommendation System**.

This application uses **Machine Learning** to recommend the most suitable crop based on soil nutrients and environmental conditions.
""")

st.write("")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌱 Soil Features", "7")

with col2:
    st.metric("🤖 ML Model", "Random Forest")

with col3:
    st.metric("📊 Accuracy", "99%")

with col4:
    st.metric("🌾 Crops", "22")

st.write("")
st.markdown("---")

# Project Overview
st.subheader("📋 Project Overview")

st.info("""
This application recommends the best suitable crop using Machine Learning based on:

• 🌱 Nitrogen (N)

• 🌾 Phosphorus (P)

• 🌿 Potassium (K)

• 🌡 Temperature

• 💧 Humidity

• 🌧 Rainfall

• ⚗ pH Value
""")

st.write("")

# Dashboard Features
st.subheader("🚀 Dashboard Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🏠 Home")
    st.success("📊 Dataset Analysis")
    st.success("🌾 Crop Prediction")

with col2:
    st.success("📈 Model Performance")
    st.success("ℹ️ About Project")
    st.success("🤖 AI Recommendation")

st.write("")
st.markdown("---")

st.success("✅ Select any page from the left sidebar to continue.")
