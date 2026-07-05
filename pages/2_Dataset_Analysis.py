import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset Analysis", page_icon="📊")

st.title("📊 Dataset Analysis")

# Load Dataset
df = pd.read_csv("Crop_recommendation.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("Column Names")
st.write(df.columns.tolist())

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Statistical Summary")
st.dataframe(df.describe())
