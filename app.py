import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator"])

# ================================
# 🏠 HOME PAGE
# ================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.markdown(r"""
    ## Persamaan Gas Ideal
    \[
    PV = nRT
    \]

    - **P**: Tekanan (atm)  
    - **V**: Volume (L)  
    - **n**: Jumlah mol  
    - **R**: 0.0821 L·atm/mol·K  
    - **T**: Suhu (K)

    Aplikasi ini membantu menghitung salah satu variabel jika tiga lainnya diketahui.
    """)
    st.info("Pilih halaman di sidebar untuk menggunakan kalkulator atau melihat grafik hubungan volume & tekanan.")

# ================================
# 📊 DASHBOARD PAGE
# ================================
elif menu == "📊 Dashboard":
    st.title("📊 Dashboard: Hukum Boyle (P ∝ 1/V)")
    st.markdown("Menunjukkan hubungan **tekanan** dan **volume** saat **jumlah mol** dan **suhu tetap**.")

    # Data simulasi hukum Boyle
    data = pd.DataFrame({
        "Volume (L)": [1, 2, 3, 4, 5],
        "Tekanan (atm)": [5, 2.5, 1.67, 1.25, 1.0]
    })

    fig, ax = plt.subplots()
    ax.plot(data["Volume (L)"], data["Tekanan (atm)"], marker='o', color='teal')
    ax.set_xlabel("Volume (L)")
    ax.set_ylabel("Tekanan (atm)")
    ax.set_title("Grafik Tekanan vs Volume (Boyle's Law)")
    st.pyplot(fig)

    st.info("Tekanan menurun saat volume bertambah, sesuai hukum Boyle.")

# ================================
# 🧮 KALKULATOR PAGE
# ================================
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("Masukkan **3 variabel** dan kosongkan **1 variabel** dengan mengisi angka 0 (nol).")

    # Input user
    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821

    if st.button("Hitung"):
        if P == 0 and V > 0 and n > 0 and T > 0:
            P = (n * R * T) / V
            st.success(f"Tekanan (P) = {P:.3f} atm")
        elif V == 0 and P > 0 and n > 0 and T > 0:
            V = (n * R * T) / P
            st.success(f"Volume (V) = {V:.3f} liter")
        elif n == 0 and P > 0 and V > 0 and T > 0:
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol (n) = {n:.3f} mol")
        elif T == 0 and P > 0 and V > 0 and n > 0:
            T = (P * V) / (n * R)
            st.success(f"Suhu (T) = {T:.2f} K")
        else:
            st.error("Isi *tepat satu* variabel dengan 0 dan sisanya dengan nilai valid (> 0).")

    st.caption("Menggunakan konstanta gas R = 0.0821 L·atm/mol·K")
