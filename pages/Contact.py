import streamlit as st


# Judul halaman
# =============
st.title("Kontak & Informasi Pengembang")

# Informasi pengembang
# ====================
st.write(
    """
    **Pengembang:**  
    Jufri Mahardi

    **Email:**  
    jmahardi007@gmail.com

    **LinkedIn:**  
    [www.linkedin.com/in/jufri-mahardi](https://www.linkedin.com/in/jufri-mahardi)

    **GitHub:**  
    [https://github.com/Jufry09](https://github.com/Jufry09)
    """
)

# Catatan tentang aplikasi
# ========================
st.subheader("Catatan Aplikasi")
st.write(
    """
    Aplikasi ini dibuat untuk keperluan pembelajaran dan portofolio.  
    Tujuan utamanya adalah membantu pengguna memahami risiko stroke 
    berdasarkan data kesehatan melalui analisis Machine Learning.

    Harap dicatat bahwa aplikasi ini **bukan alat diagnosis medis**. 
    Segala hasil prediksi hanya bersifat edukasi dan informasi tambahan.
    """
)

# Cara menghubungi
# ================
st.subheader("Cara Menghubungi")
st.write(
    """
    Jika Anda memiliki pertanyaan, saran, atau ingin berdiskusi mengenai proyek ini,  
    silakan menghubungi saya melalui email atau melalui LinkedIn.  
    Saya terbuka untuk kolaborasi dan masukan terkait proyek Machine Learning ini.
    """
)