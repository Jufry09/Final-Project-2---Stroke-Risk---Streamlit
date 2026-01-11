import streamlit as st

# About Page — Informasi Umum Aplikasi
# ====================================
st.title("About — Stroke Risk Prediction App")

st.write(
    """
    Aplikasi **Stroke Risk Prediction** adalah aplikasi berbasis web
    yang dibangun menggunakan **Streamlit** dan **Machine Learning**.
    
    Aplikasi ini bertujuan untuk memberikan gambaran awal mengenai
    risiko stroke berdasarkan data kesehatan individu, serta menjadi
    media edukasi terkait penerapan analisis data di bidang kesehatan.
    """
)


# Tujuan Aplikasi
# ===============
st.subheader("Tujuan Aplikasi")

st.write(
    """
    Tujuan utama dari aplikasi ini adalah:
    - Memberikan gambaran risiko stroke secara kuantitatif
    - Membantu memahami faktor-faktor risiko stroke berbasis data
    - Menunjukkan alur kerja proyek data science end-to-end
    - Menjadi portofolio pembelajaran Machine Learning
    """
)


# Dataset yang Digunakan
# =======================
st.subheader("Dataset")

st.write(
    """
    Dataset yang digunakan merupakan dataset kesehatan yang berisi
    informasi demografis dan kondisi medis pasien, seperti:
    
    - Usia
    - Jenis kelamin
    - Hipertensi
    - Penyakit jantung
    - Status pernikahan
    - Tipe pekerjaan
    - Kadar glukosa rata-rata
    - Indeks massa tubuh (BMI)
    - Status merokok
    
    Dataset ini telah melalui tahap pembersihan data (data cleaning),
    eksplorasi data (EDA), serta feature engineering sebelum digunakan
    dalam proses pemodelan.
    """
)


# Pendekatan Machine Learning
# ============================
st.subheader("Pendekatan Machine Learning")

st.write(
    """
    Model Machine Learning digunakan untuk mempelajari pola hubungan
    antara faktor-faktor kesehatan dengan risiko stroke.
    
    Model yang digunakan **bukan alat diagnosis medis**, melainkan
    alat bantu analisis risiko berbasis data. Hasil prediksi harus
    diinterpretasikan secara hati-hati dan tidak menggantikan
    konsultasi dengan tenaga medis profesional.
    """
)

# Teknologi yang Digunakan
# =========================
st.subheader("Teknologi")

st.write(
    """
    Teknologi utama yang digunakan dalam aplikasi ini meliputi:
    
    - Python
    - Pandas & NumPy untuk pengolahan data
    - Scikit-learn untuk Machine Learning
    - Matplotlib untuk visualisasi
    - Streamlit untuk pembuatan aplikasi web interaktif
    """
)


# Catatan Etika & Disclaimer
# ==========================
st.subheader("Catatan Penting")

st.write(
    """
    Aplikasi ini dibuat untuk tujuan edukasi dan pembelajaran.
    
    Prediksi yang dihasilkan tidak bersifat diagnosis medis dan
    tidak boleh digunakan sebagai dasar pengambilan keputusan
    klinis tanpa konsultasi dengan dokter atau tenaga kesehatan.
    """
)