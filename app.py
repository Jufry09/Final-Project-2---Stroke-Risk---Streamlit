import streamlit as st
from PIL import Image

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

    **Disclaimer:**  
    Aplikasi ini hanya untuk tujuan edukasi dan **bukan pengganti diagnosis medis**.
    
    """
)

# Menampilkan gambar lokal
image = Image.open("images/stroke.jpg")  # Ganti path sesuai lokasi gambar
st.image(image, caption="Ilustrasi Stroke", width=1000)


#Sidebar
st.sidebar.title("Navigasi")
st.sidebar.info(
    """
    Gunakan menu di sidebar untuk berpindah halaman:

    - About  
    - Contact
    - Dashboard  
    - Machine Learning  
    - Prediction  
    - Visualisasi  
    """
)

# Footer
st.markdown("___")
st.caption("© 2026 | Stroke Risk Prediction App")