import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar navigasi
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator"]
)

# ================================
# 🏠 HALAMAN HOME
# ================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.markdown("""
    ### Persamaan Gas Ideal
    \[
    PV = nRT
    \]

    - **P**: Tekanan (atm)  
    - **V**: Volume (L)  
    - **n**: Jumlah mol  
    - **R**: 0.0821 L·atm/mol·K  
    - **T**: Suhu (K)

    Aplikasi ini dapat menghitung salah satu variabel jika tiga lainnya diketahui.
    """)
    st.info("Gunakan menu di sebelah kiri untuk membuka kalkulator atau melihat grafik.")

# ================================
# 📊 HALAMAN DASHBOARD
# ================================
elif menu == "📊 Dashboard":
    st.title("📊 Dashboard Gas Ideal")
    st.markdown("Contoh visualisasi **Hukum Boyle** (P berbanding terbalik dengan V saat n & T konstan).")

    data = pd.DataFrame({
        "Volume (L)": [1, 2, 3, 4, 5],
        "Tekanan (atm)": [5, 2.5, 1.67, 1.25, 1.0]
    })

    fig, ax = plt.subplots()
    ax.plot(data["Volume (L)"], data["Tekanan (atm)"], marker='o', color='teal')
    ax.set_xlabel("Volume (L)")
    ax.set_ylabel("Tekanan (atm)")
    ax.set_title("Tekanan vs Volume (Hukum Boyle)")

    st.pyplot(fig)
    st.info("Semakin besar volume, semakin kecil tekanan (dengan n dan T tetap).")

# ================================
# 🧮 HALAMAN KALKULATOR
# ================================
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("Isi tiga variabel dan kosongkan satu dengan 0 untuk menghitung.")

    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821  # Konstanta gas

    if st.button("Hitung"):
        if P == 0 and V and n and T:
            P = (n * R * T) / V
            st.success(f"Tekanan (P) = {P:.2f} atm")
        elif V == 0 and P and n and T:
            V = (n * R * T) / P
            st.success(f"Volume (V) = {V:.2f} L")
        elif n == 0 and P and V and T:
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol (n) = {n:.2f} mol")
        elif T == 0 and P and V and n:
            T = (P * V) / (n * R)
            st.success(f"Suhu (T) = {T:.2f} K")
        else:
            st.error("Tolong kosongkan **satu variabel saja** (isi 0), bukan semuanya.")
