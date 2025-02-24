import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "IndATAR_PowerBI_Dataset.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("❌ Dataset not found. Please upload 'IndATAR_PowerBI_Dataset.csv' to your repository.")
    st.stop()

# Set up Streamlit Page Configuration
st.set_page_config(page_title="Ind ATAR Dashboard", layout="wide")

# Create Sidebar Navigation
st.sidebar.title("📌 Navigation")
