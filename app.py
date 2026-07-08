import streamlit as st

st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)
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

h1,h2,h3{
    color:#0f172a;
}

.stButton>button{
    width:100%;
    background:#16a34a;
    color:white;
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
