import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Project")

st.markdown("""
# 🌾 AI Crop Recommendation System

## 📌 Project Objective

The objective of this project is to recommend the most suitable crop
based on soil nutrients and environmental conditions using Machine Learning.

---

## 📊 Dataset Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

Target:
- Crop Name

---

## 🤖 Machine Learning Models Used

- Random Forest
- XGBoost
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Multi-Layer Perceptron (MLP)

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🛠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib

---

## 🎯 Outcome

The application predicts the most suitable crop based on user inputs,
helping farmers make informed agricultural decisions.

---

### 👩‍💻 Developed By

**Charitha**
""")
