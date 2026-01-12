import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Machine Learning Overview")

st.subheader("Tujuan Penggunaan Machine Learning")

st.write(
    """
    Tujuan utama penggunaan Machine Learning pada aplikasi ini adalah
    untuk membantu mengidentifikasi individu yang memiliki risiko stroke
    lebih tinggi berdasarkan data kesehatan yang tersedia.

    Model ini tidak dimaksudkan sebagai alat diagnosis medis,
    melainkan sebagai alat bantu analisis dan edukasi untuk memahami
    faktor-faktor risiko stroke secara lebih sistematis.
    """
)

st.write(
    """
    Halaman ini menjelaskan pendekatan Machine Learning yang digunakan
    dalam aplikasi prediksi risiko stroke.

    Model **TIDAK** dilatih ulang di aplikasi Streamlit.
    Seluruh proses training dan validasi dilakukan secara terpisah
    pada tahap modeling.
    """
)

st.subheader("1. Dataset dan Preprocessing")

st.write(
    """
    Dataset yang digunakan berasal dari data kesehatan dan telah melalui:
    - Data cleaning (missing value, duplikasi)
    - Exploratory Data Analysis (EDA)
    - Feature engineering final
    - Pemisahan data train dan test
    - Scaling fitur numerik (hanya pada data training)
 
    Dataset final digunakan khusus untuk kebutuhan Machine Learning.
    """
)

st.subheader("2. Model yang digunakan")

st.write(
    """
    Model final yang digunakan adalah:
    **Random Forest Classifier**
    
    Alasan pemilihan model:
     - Mampu menangkap hubungan non-linear antar fitur
     - Performa lebih baik dibandingkan baseline Logistic Regression
     - Stabil berdasarkan evaluasi cross-validation
     - Memiliki recall tinggi, sesuai untuk konteks kasus medis
    """
)

st.subheader("3. Evaluasi Model")

st.write(
    """
    Evaluasi model dilakukan menggunakan data testing
    yang tidak pernah digunakan selama proses training.
    Pendekatan ini bertujuan untuk mengukur kemampuan model
    dalam melakukan generalisasi terhadap data baru.
    """
)

st.markdown(
    """
    **Hasil utama:**
    - Accuracy ≈ 97%
    - Recall (stroke) ≈ sangat tinggi
    - Cross-validation recall stabil (5-Fold)
    """
)

st.subheader("5. Ringkasan Performa Model (Final)")

accuracy = 0.97
recall_stroke = 0.99

st.write("**Accuracy:**", accuracy)
st.write("**Recall (Stroke):**", recall_stroke)

st.write(
    """
    Nilai performa di atas menunjukkan bahwa model memiliki kemampuan
    yang sangat baik dalam mendeteksi kasus stroke, dengan tingkat kesalahan
    yang relatif rendah pada data pengujian.
    """
)

st.write(
    """
    Confusion matrix berikut merupakan hasil evaluasi model
    pada data testing dan ditampilkan untuk memberikan gambaran
    performa klasifikasi secara visual.
    """
)

conf_matrix = np.array([
    [559, 24],
    [2, 387]
])

fig, ax = plt.subplots()

from matplotlib.colors import ListedColormap

cmap = ListedColormap(['#FF6B6B', '#FFD93D', '#6BCB77'])  # merah → kuning → hijau
im = ax.imshow(conf_matrix, cmap=cmap)

for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(j, i, conf_matrix[i, j],
                ha="center", va="center")

ax.set_xlabel("Predicted Label")
ax.set_ylabel("True Label")
ax.set_title("Confusion Matrix - Random Forest Model")

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Tidak Stroke", "Stroke"])
ax.set_yticklabels(["Tidak Stroke", "Stroke"])

st.pyplot(fig)

st.subheader("Interpretasi Hasil Model")

st.write(
    """
    Berdasarkan confusion matrix di atas, dapat dilihat bahwa model
    mampu mengidentifikasi hampir seluruh kasus stroke dengan sangat baik.

    Kesalahan yang paling kritis dalam kasus medis adalah ketika pasien
    yang sebenarnya berisiko stroke diprediksi sebagai tidak stroke.
    Pada model ini, jumlah kesalahan tersebut relatif sangat kecil.

    Oleh karena itu, metrik **recall** menjadi fokus utama dalam evaluasi,
    karena menunjukkan kemampuan model dalam mendeteksi kasus stroke
    secara maksimal, meskipun dengan konsekuensi adanya beberapa false alarm.
    """
)

st.subheader("Faktor Risiko yang Paling Berpengaruh (Feature Importance)")

import pandas as pd

feature_names = [
    "age",
    "hypertension",
    "heart_disease",
    "avg_glucose_level",
    "bmi"
]

importance_values = [0.42, 0.28, 0.17, 0.09, 0.04]

importance_df = pd.DataFrame({
    "Fitur": feature_names,
    "Pengaruh Relatif": importance_values
}).sort_values(by="Pengaruh Relatif", ascending=True)

fig, ax = plt.subplots()
ax.barh(
    importance_df["Fitur"],
    importance_df["Pengaruh Relatif"]
)
ax.set_xlabel("Tingkat Pengaruh terhadap Risiko Stroke")
ax.set_title("Faktor Risiko Stroke Berdasarkan Model")

st.pyplot(fig)

st.write(
    """
    Grafik di atas menunjukkan faktor-faktor yang paling berpengaruh
    dalam menentukan risiko stroke berdasarkan model yang digunakan.
    Semakin besar nilai pengaruhnya, semakin besar kontribusi faktor tersebut
    terhadap peningkatan risiko stroke menurut data historis.
    """
)

st.subheader("Faktor Risiko yang Paling Berpengaruh")

st.write(
    """
    Berdasarkan analisis data, eksplorasi awal (EDA), serta pemahaman domain kesehatan,
    terdapat beberapa faktor utama yang berkontribusi terhadap peningkatan risiko stroke.

    Faktor-faktor tersebut antara lain:
    - **Usia**: Risiko stroke cenderung meningkat seiring bertambahnya usia.
    - **Hipertensi**: Tekanan darah tinggi merupakan salah satu faktor risiko utama stroke.
    - **Kadar glukosa darah**: Nilai rata-rata glukosa yang tinggi berkorelasi dengan risiko stroke.
    - **Riwayat penyakit jantung**: Individu dengan penyakit jantung memiliki risiko yang lebih tinggi.
    - **Faktor gaya hidup**: Kebiasaan merokok dan tingkat aktivitas fisik juga berperan dalam meningkatkan risiko.

    Penjelasan faktor-faktor ini bertujuan untuk memberikan gambaran umum,
    bukan sebagai penilaian medis individual.
    """
)

st.subheader("Rekomendasi dan Catatan Penggunaan")

st.write(
    """
    Berdasarkan hasil analisis dan prediksi model, terdapat beberapa hal yang dapat
    dijadikan perhatian secara umum, antara lain:

    - Menjaga pola hidup sehat dengan aktivitas fisik yang cukup
    - Mengontrol tekanan darah dan kadar gula darah secara berkala
    - Menghindari kebiasaan merokok
    - Melakukan pemeriksaan kesehatan rutin, terutama bagi individu dengan faktor risiko

    Seluruh rekomendasi ini bersifat umum dan tidak menggantikan konsultasi
    dengan tenaga medis profesional.
    """
)

st.subheader("Model Limitation")

st.write(
    """
    Model machine learning yang digunakan pada aplikasi ini dibangun
    berdasarkan dataset historis yang memiliki keterbatasan dalam
    merepresentasikan seluruh populasi. Oleh karena itu, hasil prediksi
    yang dihasilkan tidak dapat digunakan sebagai alat diagnosis medis,
    melainkan sebagai alat bantu screening awal untuk membantu memahami
    potensi risiko stroke. Keputusan medis tetap harus dilakukan oleh
    tenaga kesehatan profesional dengan mempertimbangkan pemeriksaan
    klinis dan faktor lain di luar dataset.
    """
)

st.subheader("4. Catatan Penting")

st.info(
    """
    Model ini dikembangkan untuk tujuan edukasi.
    Hasil prediksi tidak dapat dijadikan sebagai diagnosis medis.
    """
)