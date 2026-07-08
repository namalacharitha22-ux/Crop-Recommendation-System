import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Background */
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg,#f4fff6,#ffffff);
}

/* Header */
h1{
    color:#1b5e20;
    font-weight:700;
}

h2,h3{
    color:#2e7d32;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:2px solid #e8f5e9;
}

/* Sidebar Title */
[data-testid="stSidebar"] h1{
    color:#1b5e20 !important;
}

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:#2e7d32 !important;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#2e7d32;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1b5e20;
}

/* Cards */
div[data-testid="metric-container"]{
    background:white;
    border:1px solid #c8e6c9;
    border-radius:15px;
    padding:18px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

/* Info Box */
[data-testid="stAlert"]{
    border-radius:12px;
}

/* Horizontal Line */
hr{
    border:1px solid #c8e6c9;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌾 AI Crop Recommendation")
st.sidebar.success("Machine Learning Based Crop Prediction")

# ---------------- HOME ----------------
st.title("🌾 AI Crop Recommendation System")

st.markdown("""
### 🌱 Welcome

This application uses **Machine Learning** to recommend the most suitable crop based on:

- 🌿 Soil Nutrients
- 🌡 Temperature
- 💧 Humidity
- 🌧 Rainfall
- 🧪 Soil pH

---

### 🚀 Features

✅ Dataset Analysis

✅ Crop Prediction

✅ Model Performance

✅ About Project

---

### 📌 Objective

To help farmers choose the best crop based on soil and environmental conditions using Artificial Intelligence.

""")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Dataset","2200 Records")

with col2:
    st.metric("Features","7")

with col3:
    st.metric("Algorithm","Random Forest")

st.success("👈 Select any page from the sidebar to continue.")
