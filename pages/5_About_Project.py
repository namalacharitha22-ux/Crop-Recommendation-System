import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About AI Crop Recommendation System")

st.markdown("### Final Year Machine Learning Project")

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
The AI Crop Recommendation System helps farmers identify the most suitable crop
based on soil nutrients and environmental conditions using Machine Learning.
The system improves crop productivity and supports smart farming decisions.
""")

st.markdown("---")

st.header("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.success("""
- Python
- Streamlit
- NumPy
- Pandas
- Scikit-Learn
""")

with col2:
    st.success("""
- Joblib
- Machine Learning
- Random Forest
- GitHub
- Streamlit Cloud
""")

st.markdown("---")

st.header("🧠 Machine Learning Workflow")

st.info("""
1️⃣ Data Collection

2️⃣ Data Preprocessing

3️⃣ Feature Scaling

4️⃣ Model Training

5️⃣ Model Evaluation

6️⃣ Crop Prediction

7️⃣ Deployment using Streamlit
""")

st.markdown("---")

st.header("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("🌾 Crop Classes", "22")
col2.metric("📋 Features", "7")
col3.metric("🎯 Accuracy", "99%")

st.markdown("---")

st.header("🚀 Future Scope")

st.write("""
✅ Weather API Integration

✅ Fertilizer Recommendation

✅ Disease Detection

✅ Mobile Application

✅ Multi-language Support

✅ GPS-based Farming Assistance
""")

st.markdown("---")

st.success("🌱 Thank you for exploring the AI Crop Recommendation System!")
