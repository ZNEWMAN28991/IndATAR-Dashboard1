import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "IndATAR_PowerBI_Dataset.csv"  # Update this if needed
df = pd.read_csv(file_path)

# Streamlit Page Configuration
st.set_page_config(page_title="Ind ATAR Dashboard", layout="wide")

# Page Title
st.title("📊 Ind ATAR Analysis Dashboard")
st.write("Analyze subject performance, ATAR trends, and rankings over time.")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
selected_year = st.sidebar.selectbox("Select Year:", sorted(df["Year"].unique()), index=0)
selected_subject = st.sidebar.selectbox("Select Subject:", sorted(df["Subject"].unique()), index=0)

# Filtered Data
filtered_df = df[(df["Year"] == selected_year) & (df["Subject"] == selected_subject)]

# Display Selected Data
st.subheader(f"📌 Data for {selected_subject} in {selected_year}")
st.dataframe(filtered_df)

# Line Chart: ATAR Trends Over Time
st.subheader("📈 ATAR Trends Over the Years")
atar_trend = df[df["Subject"] == selected_subject].groupby("Year")["avg_IndATAR"].mean()

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(atar_trend.index, atar_trend.values, marker="o", linestyle="-", color="b")
ax.set_title(f"Ind ATAR Trend for {selected_subject}")
ax.set_xlabel("Year")
ax.set_ylabel("Average Indicative ATAR")
st.pyplot(fig)

# Bar Chart: Subject Rankings
st.subheader(f"🏆 Subject Rankings by ATAR in {selected_year}")
yearly_ranking = df[df["Year"] == selected_year].sort_values("avg_IndATAR", ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(yearly_ranking["Subject"], yearly_ranking["avg_IndATAR"], color="skyblue")
ax.set_xlabel("Average Indicative ATAR")
ax.set_ylabel("Subject")
ax.set_title(f"Subject Rankings - {selected_year}")
st.pyplot(fig)

# ATAR Gap Analysis
st.subheader(f"⚖️ ATAR Gap Analysis in {selected_year}")
gap_ranking = df[df["Year"] == selected_year].sort_values("avg_Gap", ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(gap_ranking["Subject"], gap_ranking["avg_Gap"], color="red")
ax.set_xlabel("Average ATAR Gap")
ax.set_ylabel("Subject")
ax.set_title(f"Subject ATAR Gaps - {selected_year}")
st.pyplot(fig)

# Footer
st.sidebar.write("📌 Developed for Ind ATAR Teaching Analysis")
