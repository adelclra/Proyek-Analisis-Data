import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_path = "dashboard/all_data.csv" 
df = pd.read_csv(data_path) 

df["cnt"] = df["cnt_x"] + df["cnt_y"]


df["dteday"] = pd.to_datetime(df["dteday"])


st.sidebar.title("Filter")
year_selected = st.sidebar.selectbox("Pilih Tahun", df["dteday"].dt.year.unique())
df_filtered = df[df["dteday"].dt.year == year_selected]


st.title("Dashboard Rata-rata Peminjaman Sepeda")

st.subheader("Rata-rata Peminjaman Sepeda per Bulan")
monthly_rentals = df_filtered.groupby(df_filtered["dteday"].dt.month)["cnt"].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_rentals.index, y=monthly_rentals.values, marker="o")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
plt.xlabel("Bulan")
plt.ylabel("Rata-rata Peminjaman")
plt.title("Rata-rata Bulanan Peminjaman Sepeda")
st.pyplot(plt)


peak_month = monthly_rentals.idxmax()
st.markdown(f"**Bulan dengan rata-rata peminjaman tertinggi: {peak_month} ({monthly_rentals.max():.2f} sepeda/hari)**")

st.subheader("Rata-rata Peminjaman: Hari Kerja vs. Akhir Pekan")
weekday_rentals = df_filtered[df_filtered["workingday_x"] == 1]["cnt"].mean()
weekend_rentals = df_filtered[df_filtered["workingday_x"] == 0]["cnt"].mean()

plt.figure(figsize=(6, 4))
sns.barplot(x=["Hari Kerja", "Akhir Pekan"], y=[weekday_rentals, weekend_rentals], palette=["blue", "orange"])
plt.ylabel("Rata-rata Peminjaman")
st.pyplot(plt)

st.markdown(f"**Rata-rata peminjaman di hari kerja: {weekday_rentals:.2f} sepeda/hari**")
st.markdown(f"**Rata-rata peminjaman di akhir pekan: {weekend_rentals:.2f} sepeda/hari**")
