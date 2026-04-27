# ==========================================================
# STREAMLIT DASHBOARD - DINAS KOMUNIKASI DAN INFORMATIKA
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# KONFIGURASI HALAMAN
# -------------------------
st.set_page_config(
    page_title="Dashboard Dinas Kominfo Belu",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------
st.title("📡 Dashboard Dinas Komunikasi dan Informatika Kabupaten Belu")
st.markdown("Menampilkan data ASN TIK, DUK, Bantuan Internet, OPD, dan Media")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header("📂 Upload Data Excel")
uploaded_files = st.sidebar.file_uploader(
    "Upload file Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

# -------------------------
# DATA RINGKASAN STATIK
# -------------------------
jumlah_lokasi_bakti = 97
jumlah_opd = 47
jumlah_media = 57

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Lokasi Bantuan Internet", jumlah_lokasi_bakti)

with col2:
    st.metric("Jumlah OPD", jumlah_opd)

with col3:
    st.metric("Media Terdaftar", jumlah_media)

# -------------------------
# TAMPILKAN DATA EXCEL
# -------------------------
if uploaded_files:
    for file in uploaded_files:
        st.subheader(f"📄 Data dari {file.name}")

        df = pd.read_excel(file)

        st.dataframe(df, use_container_width=True)

        st.write(f"Jumlah Baris: {len(df)}")
        st.write(f"Jumlah Kolom: {len(df.columns)}")

        # Visualisasi otomatis jika ada kolom numerik
        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:
            selected_col = st.selectbox(
                f"Pilih kolom numerik untuk grafik ({file.name})",
                numeric_cols,
                key=file.name
            )

            fig = px.bar(
                df,
                x=df.index,
                y=selected_col,
                title=f"Grafik {selected_col} - {file.name}"
            )

            st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Silakan upload file Excel untuk melihat data.")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.caption("Dashboard dibuat dengan Streamlit untuk Dinas Kominfo Kabupaten Belu")
