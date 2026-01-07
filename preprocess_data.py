import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load Dataset mentah
# ======================
raw_data_path = "data/2. Healthcare Dataset Stroke.csv"

df = pd.read_csv(raw_data_path)

print("Data awal:")
print(df.head())
print("\nInfo dataset:")
print(df.info())

# 2. Data Cleaning
# ================
df = df.drop(columns=["id"])
print("\nInfo dataset setelah drop kolom id:")
print(df.info())

# Memeriksa missing value
print("\nMemeriksa missing values:")
print(df.isnull().sum())

# Mengatasi missing Values di kolom BMI dengan mengisi median
if df["bmi"].isnull().sum() > 0:
    median_bmi = df["bmi"].median()
    df["bmi"] = df["bmi"].fillna(median_bmi)

# Meriksa kembali missing values
print("\nSetelah mengatasi missing values:")
print(df.isnull().sum())

# 3. Feature Engineering
# ======================
# encode kolom kategorikal menjadi numerik
categorical_columns = [
    "gender",
    "ever_married",
    "work_type",
    "Residence_type",
    "smoking_status"
]

label_encoder = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoder[col] = le

print(df.info())
print(df.head(100))

# 4. Simpan dataset hasil cleaning
# ================================
cleaned_data_path = "data/stroke_cleaned.csv"
df.to_csv(cleaned_data_path, index=False)

print("\nData cleaning dan Feature Engineering selesai")
print(f"Dataset tersimpan di: {cleaned_data_path}")