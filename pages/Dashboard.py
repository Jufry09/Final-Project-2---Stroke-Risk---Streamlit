import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset CLEAN
# ==================
DATA_PATH = "data/stroke_cleaned.csv"
df = pd.read_csv(DATA_PATH)

# Dashboard Filters
# ==================
st.sidebar.subheader("Filter Data")

selected_gender = st.sidebar.selectbox(
    "Gender",
    options=["All", "Male", "Female"]
)

selected_hypertension = st.sidebar.selectbox(
    "Hipertensi",
    options=["All", "Yes", "No"]
)

filtered_df = df.copy()

if selected_gender != "All":
    if filtered_df["gender"].dtype == object:
        filtered_df = filtered_df[filtered_df["gender"] == selected_gender]
    else:
        gender_map = {"Male": 1, "Female": 0}
        filtered_df = filtered_df[filtered_df["gender"] == gender_map[selected_gender]]

if selected_hypertension != "All":
    if filtered_df["hypertension"].dtype == object:
        filtered_df = filtered_df[filtered_df["hypertension"] == selected_hypertension]
    else:
        hyper_map = {"Yes": 1, "No": 0}
        filtered_df = filtered_df[filtered_df["hypertension"] == hyper_map[selected_hypertension]]


st.markdown(
    """
    <style>
    .kpi-card {
        background-color: #2d3748;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
    }
    .kpi-title {
        font-size: 14px;
        color: #9ca3af;
    }
    .kpi-value {
        font-size: 28px;
        font-weight: bold;
        margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader("Ringkasan Utama Data")

total_data = len(filtered_df)
total_stroke = filtered_df["stroke"].sum()
stroke_percentage = (total_stroke / total_data) * 100 if total_data > 0 else 0
avg_age_stroke = (
    filtered_df[filtered_df["stroke"] == 1]["age"].mean()
    if total_stroke > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Data</div>
            <div class="kpi-value">{total_data}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Kasus Stroke</div>
            <div class="kpi-value">{total_stroke}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Persentase Stroke</div>
            <div class="kpi-value">{stroke_percentage:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Rata-rata Usia (Stroke)</div>
            <div class="kpi-value">{avg_age_stroke:.1f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

if total_data == 0:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
    st.stop()

# Donut chart section update
fig, ax = plt.subplots(facecolor="#1f2933")
ax.set_facecolor("#1f2933")

# Assuming some data and labels for the pie chart
labels = ['Stroke', 'No Stroke']
sizes = [total_stroke, total_data - total_stroke]
colors = ['#ff9999','#66b3ff']

wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

# Draw circle for donut shape
centre_circle = plt.Circle((0,0),0.70,fc='#1f2933')
fig.gca().add_artist(centre_circle)

for text in ax.texts:
    text.set_color("white")

ax.title.set_color("white")

plt.tight_layout()
st.pyplot(fig)
