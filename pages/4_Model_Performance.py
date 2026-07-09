import streamlit as st

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")

st.markdown("### Machine Learning Model Evaluation")

st.markdown("---")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("🎯 Accuracy", "99%")
col2.metric("🎯 Precision", "99%")
col3.metric("🎯 Recall", "99%")
col4.metric("🎯 F1-Score", "99%")

st.markdown("---")

st.subheader("🤖 Machine Learning Model")

st.success("""
**Algorithm Used:** Random Forest Classifier

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.
""")

st.markdown("---")

st.subheader("📊 Model Summary")

st.info("""
✔ Dataset Used : Crop Recommendation Dataset

✔ Total Features : 7

✔ Number of Crop Classes : 22

✔ Train-Test Split : 80% - 20%

✔ Data Scaling : StandardScaler

✔ Label Encoding : Applied

✔ Best Model : Random Forest Classifier
""")

st.markdown("---")

st.subheader("📋 Performance Analysis")

st.write("""
- ✅ High Accuracy
- ✅ Fast Prediction
- ✅ Handles Multiple Crop Classes
- ✅ Robust Against Overfitting
- ✅ Suitable for Agricultural Decision Support
""")

st.markdown("---")

st.success("🎉 The Random Forest model achieved excellent performance for crop recommendation.")
