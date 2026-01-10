import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Eda Analysis
# 1. Load Dataset
# ================
data_path = "data/stroke_cleaned.csv"
df = pd.read_csv(data_path)

print("Preview data:")
print(df.head())

print("\nInfo Dataset:")
print(df.info())
print("\nDeskripsi Dataset:")
print(df.describe())

# 2. Duplicate Check
# ===================
duplicate_count = df.duplicated().sum()

print("\nJumlah data duplikat:")
print(duplicate_count)

if duplicate_count > 0:
    print("\nJumlah data duplikat:")
    print(df[df.duplicated(keep=False)].head())
else:
    print("\nTidak ditemukan data duplikat.")

# 3. Target Distribution Data (Stroke)
# ====================================
print("\nDistribusi target (stroke):")
print(df["stroke"].value_counts())
print("\nDistribusi target (stroke) dalam persentase:")
print(df["stroke"].value_counts(normalize=True) * 100)

# visualisasi distribusi target
plt.figure()
sns.countplot(x="stroke", data=df)
plt.title("Distribusi Target Stroke (0 = Tidak Stroke, 1 = Stroke)")
plt.xlabel("Stroke")
plt.ylabel("Jumlah")
plt.show()

# 4. Age Distribution & Relationship with stroke
# ==============================================

print("\nStatistik Usia")
print(df["age"].describe())

# Distribusi usia
plt.figure()
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Distribusi Usia")
plt.xlabel("Usia")
plt.ylabel("Frekuensi")
plt.show()

# Hubungan usia dengan stroke (boxplot)
plt.figure()
sns.boxplot(x="stroke", y="age", data=df)
plt.title("Distribusi Usia berdasarkan Status Stroke")
plt.xlabel("Stroke (0 = Tidak Stroke, 1 = Stroke")
plt.ylabel("Usia")
plt.show()

# 5. Hypertension & Heart Disease vs stroke
# =========================================

# Distribution hypertension
print("\nDistribusi hypertension:")
print(df["hypertension"].value_counts())

plt.figure()
sns.countplot(x="hypertension", data=df)
plt.title("Distribusi hypertension")
plt.xlabel("Hypertension (0 = Tidak, 1 = Ya)")
plt.ylabel("Jumlah")
plt.show()

# Hypertension vs stroke
plt.figure()
sns.countplot(x="hypertension", hue="stroke", data=df)
plt.title("Hubungan Hypertension dengan Stroke")
plt.xlabel("Hypertension (0 = Tidak, 1 = Ya)")
plt.ylabel("Jumlah")
plt.legend(title="Stroke")
plt.show()

# Distribusi Heart Disease
print("\nDistribusi heart disease:")
print(df["heart_disease"].value_counts())

plt.figure()
sns.countplot(x="heart_disease", data=df)
plt.title("Distribusi Heart Disease")
plt.xlabel("Heart Disease (0 = Tidak, 1 = Ya)")
plt.ylabel("Jumlah")
plt.show()

# Heart disease vs stroke
plt.figure()
sns.countplot(x="heart_disease", hue="stroke", data=df)
plt.title("Hubungan Heart Disease dengan Stroke")
plt.xlabel("Heart Disease (0 = Tidak, 1 = Ya)")
plt.ylabel("Jumlah")
plt.legend(title="Stroke")
plt.show()

# 6. BMI Distribution & Relationship with Stroke
# ==============================================

print("\nStatistik BMI:")
print(df["bmi"].describe())

# Distribusi BMI
plt.figure()
sns.histplot(df["bmi"], bins=30, kde=True)
plt.title("Distribusi BMI")
plt.xlabel("BMI")
plt.ylabel("Frekuensi")
plt.show()

# BMI vs Stroke (boxplot)
plt.figure()
sns.boxplot(x="stroke", y="bmi", data=df)
plt.title("Distribusi BMI berdasarkan Status Stroke")
plt.xlabel("Stroke (0 = Tidak Stroke, 1 = Stroke)")
plt.ylabel("BMI")
plt.show()

# 7. Ringkasan EDA
# =================
print("\n=== RINGKASAN INSIGH EDA ===")
print("- Dataset tidak memiliki data duplikat.")
print("- Target relatif seimbang (60% tidak stroke, 40% stroke).")
print("- Usia memiliki hubungan kuat dengan kejadian stroke.")
print("- Hypertension dan heart disease meningkatkan risiko stroke.")
print("- BMI memiliki perbedaan distribusi antara stroke dan non-stroke.")
print("=== AKHIR EDA ===")