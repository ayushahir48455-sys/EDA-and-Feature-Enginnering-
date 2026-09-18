import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# Page configuration
# -------------------------------

st.set_page_config(
    page_title="EDA & ML Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------

st.title("📊 Exploratory Data Analysis Dashboard")
st.write("EDA and Data Analysis using Python, Pandas and NumPy")

# -------------------------------
# Load dataset
# -------------------------------

df = pd.read_csv("Ayush.csv")

# -------------------------------
# Dataset Overview
# -------------------------------

st.header("📋 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())
col4.metric("Duplicate Rows", df.duplicated().sum())

# -------------------------------
# Dataset
# -------------------------------

st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)

# -------------------------------
# Statistical Summary
# -------------------------------

st.header("📈 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

# -------------------------------
# Missing Values
# -------------------------------

st.header("🔍 Missing Value Analysis")

missing = df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Values": missing.values
})

st.dataframe(
    missing_df,
    use_container_width=True
)

# -------------------------------
# Data Types
# -------------------------------

st.header("🧾 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values
})

st.dataframe(
    dtype_df,
    use_container_width=True
)