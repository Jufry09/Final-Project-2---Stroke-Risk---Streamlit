# Train Model - Stroke Risk Prediction
# ====================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# Load dataset hasil feature engineering Final
# ============================================

DATA_PATH = "data/stroke_ml_final.csv"
df = pd.read_csv(DATA_PATH)

print("Dataset untuk modeling:")
print(df.head())

# Pisahkan fitur dan target
# =========================
X = df.drop("stroke", axis=1)
y = df["stroke"]

print("\nJumlah fitur:", X.shape[1])
print("Jumlah data:", X.shape[0])

# Train-test split
# ================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\nUkuran data training:", X_train.shape)
print("Ukuran data testing:", X_test.shape)

# Scaling fitur numerik (HANYA training data)
# ==========================================

numerical_columns = [
    "age",
    "bmi",
    "avg_glucose_level"
]

scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

# Training model (baseline)
# ========================

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluasi model
# ==============

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

print("\nClassification report:")
print(classification_report(y_test, y_pred))

print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))

# Training model non-linear (Random Forest)
# =========================================

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
)

rf_model.fit(X_train, y_train)

# Evaluasi Random Forest
# =======================

y_pred_rf = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, y_pred_rf)
print("\nRandom Forest Accuracy:", rf_accuracy)

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Cross-validation (validasi tambahan Random Forest)
# ==================================================

cv_scores = cross_val_score(
    rf_model,
    X_train,
    y_train,
    cv=5,
    scoring="recall"
)

print("\nCross-validation Recall Scores (5-Fold):")
print(cv_scores)

print("\nMean CV Recall:", cv_scores.mean())


# Simpan model dan scaler
# =======================

joblib.dump(rf_model, "models/final_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel Final (Random Forest) dan scaler berhasil disimpan di folder models/")