import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# Sidebar Title
st.sidebar.title("🌾 Crop AI")

# ---------------- CSS ---------------- #

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stAppViewContainer"]{
    background:#f4f8f4;
}

[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #d9e4d9;
}

[data-testid="stSidebar"] *{
    color:#222222;
}

h1,h2,h3{
    color:#1b5e20;
}

.stButton>button{
    width:100%;
    background:#2e7d32;
    color:white;
    border-radius:10px;
    border:none;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1b5e20;
    color:white;
}

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #e0e0e0;
    border-radius:15px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
}

.hero{
background:linear-gradient(90deg,#2e7d32,#43a047);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
box-shadow:0 8px 20px rgba(0,0,0,.15);
margin-bottom:20px;
}

.hero h1{
color:white;
font-size:42px;
margin-bottom:10px;
}

.hero p{
color:white;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>🌾 AI Crop Recommendation System</h1>

<p>
Machine Learning Based Smart Agriculture Recommendation Platform
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- KPI ---------------- #

st.subheader("📊 Dashboard Overview")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("🌱 Soil Inputs","7")

with c2:
    st.metric("🤖 ML Model","Random Forest")

with c3:
    st.metric("📈 Accuracy","98%")

with c4:
    st.metric("🌾 Output","Best Crop")

st.write("")

# ---------------- INPUT PARAMETERS ---------------- #

st.subheader("🌱 Input Parameters")

a,b,c=st.columns(3)

with a:
    st.success("🌱 Nitrogen")
    st.success("🌾 Phosphorus")
    st.success("🌿 Potassium")

with b:
    st.success("🌡 Temperature")
    st.success("💧 Humidity")

with c:
    st.success("🌧 Rainfall")
    st.success("🧪 pH Value")

st.write("")

# ---------------- FEATURES ---------------- #

st.subheader("🚀 Dashboard Features")

x,y=st.columns(2)

with x:
    st.info("📊 Dataset Analysis")
    st.info("🌾 Crop Prediction")

with y:
    st.info("📈 Model Performance")
    st.info("ℹ️ About Project")

st.write("")

st.success("👈 Use the left sidebar to explore all dashboard pages.")
