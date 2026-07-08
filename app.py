import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Background */
[data-testid="stAppViewContainer"]{
    background:#f4f8f4;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #d9e4d9;
}

[data-testid="stSidebar"] *{
    color:#222222;
}

/* Header Card */
.header{
    background:linear-gradient(90deg,#2e7d32,#43a047);
    color:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.header h1{
    color:white;
    font-size:42px;
    margin-bottom:5px;
}

.header p{
    color:white;
    font-size:18px;
}

/* KPI Cards */
.card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 18px rgba(0,0,0,.08);
    text-align:center;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0px 10px 25px rgba(0,0,0,.15);
}

.card h2{
    color:#2e7d32;
    margin:0;
}

.card p{
    color:#666;
    font-size:16px;
}

/* Feature Box */
.feature{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 18px rgba(0,0,0,.08);
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#2e7d32;
    color:white;
    border-radius:10px;
    height:3em;
    border:none;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1b5e20;
    color:white;
}

/* Metrics */
div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="header">
<h1>🌾 AI Crop Recommendation System</h1>
<p>Machine Learning Based Smart Agriculture Recommendation Platform</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- KPI CARDS ---------------- #

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
    <h2>🌱 Soil</h2>
    <p>NPK Analysis</p>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>🌦 Weather</h2>
    <p>Climate Prediction</p>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h2>🤖 AI Model</h2>
    <p>Crop Recommendation</p>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
    <h2>📈 Accuracy</h2>
    <p>High Performance</p>
    </div>
    """,unsafe_allow_html=True)

st.write("")

# ---------------- PROJECT OVERVIEW ---------------- #

st.markdown("""
<div class="feature">

## 📋 Project Overview

This application recommends the **best suitable crop** using **Machine Learning**
based on:

- 🌱 Nitrogen
- 🌾 Phosphorus
- 🌿 Potassium
- 🌡 Temperature
- 💧 Humidity
- 🌧 Rainfall
- ⚗ pH Value

</div>
""",unsafe_allow_html=True)

st.write("")

# ---------------- FEATURES ---------------- #

st.markdown("""
<div class="feature">

## 🚀 Dashboard Features

✅ Home

✅ Dataset Analysis

✅ Crop Prediction

✅ Model Performance

✅ About Project

</div>
""",unsafe_allow_html=True)

st.success("👈 Select any page from the sidebar to continue.")
