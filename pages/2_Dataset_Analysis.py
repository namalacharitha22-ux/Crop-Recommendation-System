import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dataset Analysis")

# Load Dataset
df = pd.read_csv("Crop_recommendation.csv")

st.success("Dataset Loaded Successfully ✅")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.subheader("Column Names")
st.write(list(df.columns))

st.subheader("Statistical Summary")
st.dataframe(df.describe())

st.subheader("Missing Values")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.subheader("Crop Classes")
st.write(df["label"].value_counts())
