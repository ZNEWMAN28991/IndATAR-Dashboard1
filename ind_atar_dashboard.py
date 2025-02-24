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

# Streamlit Page Configuration
st.set_page_config(page_title="Ind ATAR Dashboard", layout="wide")

# Page Title
st.title("📊 Ind ATAR Subject Comparison Dashboard")
st.write("Compare the performance of different subjects based on Indicative ATAR, HSC Scores, and Scaled Scores.")

# Sidebar Filters
st.sidebar.header("🔍 Select Subjects to Compare")
selected_year = st.sidebar.selectbox("Select Year:", sorted(df["Year"].unique()), index=0)
subject_1 = st.sidebar.selectbox("Select First Subject:", sorted(df["Subject"].unique()), index=0)
subject_2 = st.sidebar.selectbox("Select Second Subject:", sorted(df["Subject"].unique()), index=1)

# Filter Data for Selected Subjects
df_subject_1 = df[(df["Year"] == selected_year) & (df["Subject"] == subject_1)]
df_subject_2 = df[(df["Year"] == selected_year) & (df["Subject"] == subject_2)]

# Check if data exists for both subjects
if df_subject_1.empty or df_subject_2.empty:
    st.warning("⚠️ Not enough data for one or both subjects in the selected year.")
else:
    # Display Side-by-Side Comparison
    st.subheader(f"📌 {subject_1} vs. {subject_2} - {selected_year}")
    
    comparison_data = {
        "Metric": ["Avg Indicative ATAR", "Avg HSC Score", "Avg Scaled Score"],
        subject_1: [
            df_subject_1["IndATAR"].mean(),
            df_subject_1["ModeratedHSCScore"].mean(),
            df_subject_1["ScaledScore"].mean(),
        ],
        subject_2: [
            df_subject_2["IndATAR"].mean(),
            df_subject_2["ModeratedHSCScore"].mean(),
            df_subject_2["ScaledScore"].mean(),
        ]
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df)

    # Bar Chart for Comparison
    st.subheader("📊 Subject Score Comparison")
    fig, ax = plt.subplots(figsize=(6, 4))
    comparison_df.set_index("Metric").plot(kind="bar", ax=ax)
    ax.set_title(f"{subject_1} vs. {subject_2} - {selected_year}")
    ax.set_ylabel("Scores")
    plt.xticks(rotation=0)
    st.pyplot(fig)

    # Line Chart: Subject Trends Over Time
    st.subheader("📈 Subject Performance Trends Over Time")
    
    df_trend_1 = df[df["Subject"] == subject_1].groupby("Year")["IndATAR"].mean()
    df_trend_2 = df[df["Subject"] == subject_2].groupby("Year")["IndATAR"].mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df_trend_1.index, df_trend_1.values, marker="o", linestyle="-", label=subject_1, color="b")
    ax.plot(df_trend_2.index, df_trend_2.values, marker="s", linestyle="--", label=subject_2, color="r")
    ax.set_title(f"Ind ATAR Trends: {subject_1} vs. {subject_2}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Indicative ATAR")
    ax.legend()
    st.pyplot(fig)

# Footer
st.sidebar.write("📌 Developed for Ind ATAR Subject Analysis")
