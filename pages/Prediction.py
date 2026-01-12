import streamlit as st
import pandas as pd
import joblib

# Konfigurasi halaman
# ====================
st.set_page_config(page_title="Prediksi Risiko Stroke", layout="centered")

st.title("Prediksi Risiko Stroke")

st.write(
    """
    Halaman ini digunakan untuk melakukan prediksi risiko stroke
    berdasarkan data kesehatan yang dimasukkan oleh pengguna.

    Prediksi yang dihasilkan bersifat edukatif dan tidak menggantikan
    diagnosis medis profesional.
    """
)


# Load model dan scaler (hasil training FINAL)
# ======================================================
MODEL_PATH = "models/final_model.pkl"
SCALER_PATH = "models/scaler.pkl"

rf_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# Input data pengguna
# ===================
st.subheader("Masukkan Data Kesehatan")

age = st.number_input("Usia", min_value=1, max_value=120, value=40)
hypertension = st.selectbox("Hipertensi", ["Tidak", "Ya"])
heart_disease = st.selectbox("Penyakit Jantung", ["Tidak", "Ya"])
avg_glucose_level = st.number_input("Rata-rata Kadar Glukosa", value=100.0)
bmi = st.number_input("BMI", value=25.0)

gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
smoking_status = st.selectbox(
    "Status Merokok",
    ["Tidak Pernah", "Mantan Perokok", "Perokok Aktif"]
)

# Tambahan fitur input
ever_married = st.selectbox("Status Pernikahan", ["Tidak", "Ya"])
work_type = st.selectbox(
    "Jenis Pekerjaan",
    ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
)
residence_type = st.selectbox("Tipe Tempat Tinggal", ["Urban", "Rural"])

# Encoding input (KONSISTEN dengan preprocessing)
# ===============================================
gender_encoded = 1 if gender == "Laki-laki" else 0

hypertension_encoded = 1 if hypertension == "Ya" else 0
heart_disease_encoded = 1 if heart_disease == "Ya" else 0

smoking_mapping = {
    "Tidak Pernah": 0,
    "Mantan Perokok": 1,
    "Perokok Aktif": 2
}
smoking_encoded = smoking_mapping[smoking_status]

# Encoding tambahan fitur
ever_married_encoded = 1 if ever_married == "Ya" else 0

work_type_mapping = {
    "Private": 0,
    "Self-employed": 1,
    "Govt_job": 2,
    "children": 3,
    "Never_worked": 4
}
work_type_encoded = work_type_mapping[work_type]

residence_type_encoded = 1 if residence_type == "Urban" else 0

# Membentuk DataFrame input
# ========================
input_df = pd.DataFrame(
    [[
        age,
        hypertension_encoded,
        heart_disease_encoded,
        avg_glucose_level,
        bmi,
        gender_encoded,
        smoking_encoded,
        ever_married_encoded,
        work_type_encoded,
        residence_type_encoded
    ]],
    columns=[
        "age",
        "hypertension",
        "heart_disease",
        "avg_glucose_level",
        "bmi",
        "gender",
        "smoking_status",
        "ever_married",
        "work_type",
        "Residence_type"
    ]
)


# Scaling fitur numerik (SESUAI TRAINING)
# =======================================

# Ambil nama fitur numerik langsung dari scaler saat training
scaler_features = list(scaler.feature_names_in_)

# Pastikan kolom input sesuai dengan yang diharapkan scaler
input_df[scaler_features] = scaler.transform(
    input_df[scaler_features]
)


# Menyesuaikan urutan fitur dengan model
# ======================================
final_input = input_df[rf_model.feature_names_in_]


# Prediksi
#==========
if st.button("Prediksi Risiko Stroke"):
    prediction = rf_model.predict(final_input)[0]
    probability = rf_model.predict_proba(final_input)[0][1]

    st.subheader("Hasil Prediksi")

    # Tentukan warna berdasarkan hasil prediksi
    if prediction == 1:
        color = "red"
        risk_text = "TINGGI"
    else:
        color = "green"
        risk_text = "RENDAH"

    # Menampilkan hasil prediksi dengan ukuran font besar
    st.markdown(
        f"<h2 style='color:{color};'>Risiko Stroke: {risk_text}</h2>",
        unsafe_allow_html=True
    )

    # Menampilkan probabilitas dengan ukuran font sama
    st.markdown(
        f"<h3 style='color:{color};'>Probabilitas Stroke: {probability:.2%}</h3>",
        unsafe_allow_html=True
    )

    # Catatan edukatif
    st.info(
        """
        Catatan:
        - Prediksi didasarkan pada model Machine Learning
        - Hasil bersifat edukatif
        - Tidak menggantikan konsultasi medis
        """
    )