import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")

st.markdown("### Performance Metrics of the Trained Machine Learning Model")

# ===== Replace these values with your actual results =====
accuracy = 99.32
precision = 99.31
recall = 99.32
f1_score = 99.31

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", f"{accuracy}%")
col2.metric("Precision", f"{precision}%")
col3.metric("Recall", f"{recall}%")
col4.metric("F1 Score", f"{f1_score}%")

st.divider()

st.subheader("📋 Performance Summary")

performance = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Value (%)": [accuracy, precision, recall, f1_score]
})

st.dataframe(performance, use_container_width=True)

st.info("💡 Replace the above values with your model's actual evaluation metrics.")
