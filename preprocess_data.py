import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load raw dataset
# ===================
raw_data_path = "data/2. Healthcare Dataset Stroke.csv"
df_raw = pd.read_csv(raw_data_path)

print("Data awal:")
print(df_raw.head())
print("\nInfo dataset awal:")
print(df_raw.info())

# Data Description & Initial Checks
# =================================

print("\nDeskripsi statistik fitur numerik:")
print(df_raw.describe())

# Identifikasi fitur numerik dan kategorikal
numerical_features = df_raw.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = df_raw.select_dtypes(include=["object"]).columns.tolist()

print("\nDaftar fitur numerik:")
print(numerical_features)

print("\nDaftar fitur kategorikal:")
print(categorical_features)

# Cek missing value per kolom
print("\nJumlah missing value per kolom:")
print(df_raw.isnull().sum())

# Cek duplikasi data
duplicate_count_raw = df_raw.duplicated().sum()
print("\nJumlah data duplikat pada dataset awal:")
print(duplicate_count_raw)

if duplicate_count_raw > 0:
    print("\nContoh data duplikat:")
    print(df_raw[df_raw.duplicated(keep=False)].head())
else:
    print("\nTidak ditemukan data duplikat pada dataset awal.")

# 2. BASIC DATA CLEANING (UNTUK EDA)
# ==================================
df_clean = df_raw.copy()

# Drop kolom ID
if "id" in df_clean.columns:
    df_clean = df_clean.drop(columns=["id"])

# Isi missing value BMI dengan median
if df_clean["bmi"].isnull().sum() > 0:
    median_bmi = df_clean["bmi"].median()
    df_clean["bmi"] = df_clean["bmi"].fillna(median_bmi)

print("\nInfo dataset setelah cleaning (untuk EDA):")
print(df_clean.info())

# Simpan dataset CLEAN (untuk EDA & visualisasi)
clean_data_path = "data/stroke_cleaned.csv"
df_clean.to_csv(clean_data_path, index=False)

print(f"\nDataset CLEAN untuk EDA tersimpan di: {clean_data_path}")

# 3. FEATURE ENGINEERING (UNTUK MACHINE LEARNING)
# ===============================================
df_fe = df_clean.copy()

# NOTE:
# Feature engineering FINAL dimulai dari dataset CLEAN (stroke_cleaned),
# bukan dari dataset raw atau feature engineering sementara.

categorical_columns = [
    "gender",
    "ever_married",
    "work_type",
    "Residence_type",
    "smoking_status"
]

label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df_fe[col] = le.fit_transform(df_fe[col])
    label_encoders[col] = le

# memisahkan fitur (X) dan target (y)
# Scaling akan dilakukan di tahap modeling (train_model.py)
# untuk menghindari data leakage

X = df_fe.drop(columns=["stroke"])
y = df_fe["stroke"]

print("\nInfo dataset setelah feature engineering (untuk ML):")
print(df_fe.info())

# Simpan dataset FINAL untuk machine learning
ml_final_path = "data/stroke_ml_final.csv"
df_fe.to_csv(ml_final_path, index=False)

print(f"\nDataset FINAL untuk ML tersimpan di: {ml_final_path}")
print("\nPreprocessing FINAL selesai: data siap untuk training model")