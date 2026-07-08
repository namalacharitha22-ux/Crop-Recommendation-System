import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: linear-gradient(to right,#eef2ff,#ffffff);
}

[data-testid="stSidebar"]{
    background:#1e293b;
}

[data-testid="stSidebar"] *{
    color:white;
}
section[data-testid="stSidebar"] a {
    color: white !important;
}

section[data-testid="stSidebar"] .stPageLink {
    color: white !important;
}

section[data-testid="stSidebar"] button {
    color: white !important;
}

h1,h2,h3{
    color:#0f172a !important;
}

p,li,span,label,div{
    color:#111827 !important;
}

.stButton>button{
    width:100%;
    background:#16a34a;
    color:white !important;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#15803d;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
st.sidebar.title("🌾 AI Crop Recommendation")

# ---------------- Home Page ----------------
st.title("🌾 AI Crop Recommendation System")

st.header("👋 Welcome")

st.write(
    "This application uses **Machine Learning** to recommend the most suitable crop "
    "based on soil nutrients and environmental conditions."
)

st.markdown("---")

st.header("📌 Features")

st.markdown("""
- 🏠 Home
- 📊 Dataset Analysis
- 🌱 Crop Prediction
- 📈 Model Performance
- ℹ️ About Project
""")

st.info("👉 Use the left sidebar to navigate between pages.")

st.success("Select any page from the sidebar to continue.")
