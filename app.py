import streamlit as st

# Konfigurasi Halaman

st.set_page_config(
    page_title="Stroke Risk Prediction App",
    layout="wide",
)

# Judul Aplikasi
st.title("Stroke Risk Prediction")
st.subheader("A Simple Machine Learning Approach")

st.write(
    """
    Aplikasi ini bertujuan untuk membantu **memprediksi risiko stroke**
    berdasarkan data kesehatan pengguna menggunakan **Machine Learning**.

    ⚠️ **Disclaimer:**  
    Aplikasi ini hanya untuk tujuan edukasi dan **bukan pengganti diagnosis medis**.
    
    """
)

#Sidebar
st.sidebar.title("Navigasi")
st.sidebar.info(
    """
    Gunakan menu di sidebar untuk berpindah halaman:

    - About  
    - Kontak  
    - Machine Learning  
    - Prediction  
    - Visualisasi  
    """
)

# Footer
st.markdown("___")
st.caption("© 2026 | Stroke Risk Prediction App")