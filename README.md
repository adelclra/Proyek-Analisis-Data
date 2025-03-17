# Panduan Instalasi dan Menjalankan Streamlit Dashboard
# 1. Instalasi Dependensi
## a. Pastikan Python dan pip Terinstal
Cek apakah Python dan pip sudah terpasang dengan perintah berikut:
python --version
pip --version

Jika pip belum tersedia, instal dengan:
python -m ensurepip --default-pip

## b. Buat Virtual Environment (Opsional, tetapi Direkomendasikan)
Gunakan virtual environment untuk menghindari konflik dependensi:
python -m venv venv

Aktifkan virtual environment:
Windows (PowerShell):
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

## c. Instalasi Paket yang Dibutuhkan
Pasang pustaka yang diperlukan dengan:
pip install streamlit pandas matplotlib seaborn

Simpan daftar dependensi untuk memudahkan instalasi ulang:
pip freeze > requirements.txt

# 2. Menjalankan Streamlit Dashboard
Pastikan berada di direktori proyek, lalu jalankan:
cd Proyek-Analisis-Data
streamlit run dashboard.py

Jika berhasil, akan muncul pesan seperti:
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Buka http://localhost:8501 di browser untuk melihat dashboard.

# 3. Troubleshooting
🔹 Error: Modul Tidak Ditemukan
Jalankan kembali perintah berikut:
pip install -r requirements.txt

🔹 Error: Port 8501 Sudah Digunakan
Gunakan port lain:
streamlit run dashboard.py --server.port 8502

🔹 Error: Virtual Environment Tidak Aktif
Aktifkan kembali dengan:
Windows:
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

🔹 Error: Dataset Tidak Ditemukan
Pastikan file dataset bernama main_data.csv ada di direktori proyek.