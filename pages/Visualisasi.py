import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
# ===================
st.set_page_config(page_title="Eksplorasi Data", layout="centered")

st.title("Eksplorasi Data Kesehatan")

st.write(
    """
    Halaman ini menyajikan eksplorasi data kesehatan yang digunakan
    dalam pengembangan model prediksi risiko stroke.

    Tujuan utama dari halaman ini adalah membantu pengguna memahami
    pola umum dalam data, khususnya faktor-faktor yang berkaitan
    dengan risiko stroke.
    """
)

# Load dataset CLEAN
# ==================
DATA_PATH = "data/stroke_cleaned.csv"
df = pd.read_csv(DATA_PATH)

# 1. Distribusi Kasus Stroke
# =========================
st.subheader("Distribusi Kasus Stroke")

stroke_counts = df["stroke"].value_counts()

fig, ax = plt.subplots()
ax.bar(
    ["Tidak Stroke", "Stroke"],
    stroke_counts.values
)
ax.set_ylabel("Jumlah Individu")
ax.set_title("Perbandingan Kasus Stroke dan Non-Stroke")

st.pyplot(fig)

st.write(
    """
    Visualisasi ini menunjukkan bahwa jumlah individu yang mengalami
    stroke jauh lebih sedikit dibandingkan dengan individu yang tidak
    mengalami stroke. Kondisi ini umum terjadi pada data kesehatan
    dan dikenal sebagai data tidak seimbang.
    """
)

# 2. Distribusi Usia
# =================
st.subheader("Distribusi Usia Individu")

fig, ax = plt.subplots()
ax.hist(df["age"], bins=20)
ax.set_xlabel("Usia")
ax.set_ylabel("Jumlah Individu")
ax.set_title("Distribusi Usia")

st.pyplot(fig)

st.write(
    """
    Sebagian besar individu berada pada rentang usia dewasa hingga
    lanjut usia. Usia merupakan salah satu faktor penting yang
    berhubungan dengan risiko stroke.
    """
)


# 3. Hubungan Usia dengan Stroke
# =============================
st.subheader("Hubungan Usia dengan Kejadian Stroke")

fig, ax = plt.subplots()
ax.hist(
    df[df["stroke"] == 0]["age"],
    bins=20,
    alpha=0.7,
    label="Tidak Stroke"
)
ax.hist(
    df[df["stroke"] == 1]["age"],
    bins=20,
    alpha=0.7,
    label="Stroke"
)

ax.set_xlabel("Usia")
ax.set_ylabel("Jumlah Individu")
ax.set_title("Distribusi Usia Berdasarkan Status Stroke")
ax.legend()

st.pyplot(fig)

st.write(
    """
    Terlihat bahwa kasus stroke lebih banyak ditemukan pada kelompok
    usia yang lebih tinggi. Hal ini sejalan dengan pengetahuan medis
    bahwa risiko stroke meningkat seiring bertambahnya usia.
    """
)


# 4. Hipertensi dan Stroke
# =========================
st.subheader("Hipertensi sebagai Faktor Risiko Stroke")

hypertension_counts = pd.crosstab(df["hypertension"], df["stroke"])

fig, ax = plt.subplots()
hypertension_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Hipertensi (0 = Tidak, 1 = Ya)")
ax.set_ylabel("Jumlah Individu")
ax.set_title("Hubungan Hipertensi dengan Kejadian Stroke")

st.pyplot(fig)


st.write(
    """
    Individu dengan kondisi hipertensi memiliki proporsi kejadian
    stroke yang lebih tinggi dibandingkan individu tanpa hipertensi.
    Hal ini menunjukkan bahwa tekanan darah tinggi merupakan salah
    satu faktor risiko penting stroke.
    """
)

# 5. Gender dan Stroke
# ====================
st.subheader("Distribusi Kasus Stroke Berdasarkan Gender")

gender_stroke_counts = pd.crosstab(df["gender"], df["stroke"])

fig, ax = plt.subplots()
gender_stroke_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Gender")
ax.set_ylabel("Jumlah Individu")
ax.set_title("Perbandingan Kasus Stroke Berdasarkan Gender")
ax.legend(["Tidak Stroke", "Stroke"])

st.pyplot(fig)

st.write(
    """
    Visualisasi ini menunjukkan distribusi kasus stroke berdasarkan gender
    pada dataset yang digunakan. Perbedaan jumlah kasus antara gender
    menggambarkan pola yang muncul pada data, namun tidak menunjukkan
    hubungan sebab-akibat secara langsung.
    """
)

# Catatan Penutup
# ===============
st.info(
    """
    Catatan:
    - Visualisasi pada halaman ini menggunakan data yang telah dibersihkan
    - Halaman ini bersifat eksploratif dan edukatif
    - Tidak digunakan untuk proses pelatihan maupun prediksi model
    """
)