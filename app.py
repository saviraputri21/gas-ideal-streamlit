import streamlit as st

# ====================================
# 🔧 CSS Custom untuk Background Menarik
# ====================================
st.markdown("""
<style>
/* Background gradient animation */
body {
    background: linear-gradient(-45deg, #89f7fe, #66a6ff, #7EE8FA, #EEC0C6);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Blur transparan di konten */
.css-18e3th9 {
    backdrop-filter: blur(6px);
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 10px;
    padding: 1.5em;
}
</style>
""", unsafe_allow_html=True)

# ====================================
# 🧪 Konfigurasi Halaman
# ====================================
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator", "🧾 Breakdown Perhitungan", "👥 Tentang Kami"])

# ====================================
# 🏠 HOME
# ====================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.markdown(r"""
    ## Persamaan Gas Ideal
    \[
    PV = nRT
    \]

    Keterangan:
    - P : Tekanan (atm)  
    - V : Volume (L)  
    - n : Jumlah mol  
    - R : 0.0821 L·atm/mol·K  
    - T : Suhu (K)

    Aplikasi ini membantu menghitung salah satu variabel jika tiga lainnya diketahui.
    """)

# ====================================
# 📊 DASHBOARD
# ====================================
elif menu == "📊 Dashboard":
    st.title("📚 Penjelasan Gas Ideal")
    st.markdown("""
    ## 🌬️ Apa itu Gas Ideal?

    Gas ideal adalah model teoretis dari gas yang mengikuti persamaan **PV = nRT**, di mana:
    - Partikel gas dianggap tidak memiliki volume
    - Tidak ada gaya tarik-menarik antar partikel
    - Semua tumbukan antar partikel bersifat lenting sempurna

    Model ini digunakan untuk menyederhanakan perhitungan dan memahami sifat-sifat gas secara umum.

    ---

    ## 📏 Hukum-Hukum dalam Gas Ideal

    **1. Hukum Boyle**  
    Volume ∝ 1/Tekanan (pada suhu tetap)  
    \[ P_1 V_1 = P_2 V_2 \]

    **2. Hukum Charles**  
    Volume ∝ Suhu (pada tekanan tetap)  
    \[ \frac{V_1}{T_1} = \frac{V_2}{T_2} \]

    **3. Hukum Gay-Lussac**  
    Tekanan ∝ Suhu (pada volume tetap)  
    \[ \frac{P_1}{T_1} = \frac{P_2}{T_2} \]

    ---

    ## ⚛️ Sifat-Sifat Gas Ideal

    1. Partikel bergerak secara acak
    2. Tidak ada gaya tarik menarik antar molekul
    3. Ukuran partikel sangat kecil
    4. Partikel terdistribusi merata dalam ruang
    5. Tumbukan antar partikel adalah lenting sempurna
    6. Energi kinetik rata-rata sebanding dengan suhu
    """)

# ====================================
# 🧮 KALKULATOR
# ====================================
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("Masukkan **3 variabel** dan kosongkan **1 variabel** dengan mengisi angka 0 (nol).")

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

# ====================================
# 🧾 BREAKDOWN PERHITUNGAN
# ====================================
elif menu == "🧾 Breakdown Perhitungan":
    st.title("🧾 Breakdown Perhitungan Gas Ideal (PV = nRT)")
    st.markdown("Masukkan **3 variabel**, kosongkan **1 variabel** dengan mengisi angka 0. Hasil disertai langkah-langkah perhitungan.")

    P = st.number_input("Tekanan (P) dalam atm", value=0.0, key="bp_P")
    V = st.number_input("Volume (V) dalam liter", value=0.0, key="bp_V")
    n = st.number_input("Jumlah mol (n)", value=0.0, key="bp_n")
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0, key="bp_T")
    R = 0.0821

    if st.button("Tampilkan Breakdown"):
        zero_count = sum([P == 0, V == 0, n == 0, T == 0])
        if zero_count != 1:
            st.error("Kosongkan *tepat satu* variabel (isi dengan 0), dan tiga lainnya harus > 0.")
        else:
            st.subheader("🔍 Langkah-Langkah Perhitungan")

            if P == 0:
                st.latex("PV = nRT")
                st.markdown(f"n = {n}, R = 0.0821, T = {T}, V = {V}")
                st.latex("P = \\frac{nRT}{V}")
                result = (n * R * T) / V
                st.latex(f"P = \\frac{{{n} × {R} × {T}}}{{{V}}} = {result:.3f} \\ atm")
                st.success(f"✅ Tekanan (P) = {result:.3f} atm")

            elif V == 0:
                st.latex("PV = nRT")
                st.markdown(f"n = {n}, R = 0.0821, T = {T}, P = {P}")
                st.latex("V = \\frac{nRT}{P}")
                result = (n * R * T) / P
                st.latex(f"V = \\frac{{{n} × {R} × {T}}}{{{P}}} = {result:.3f} \\ liter")
                st.success(f"✅ Volume (V) = {result:.3f} liter")
            elif n == 0:
                st.latex("PV = nRT")
                st.markdown(f"P = {P}, V = {V}, R = 0.0821, T = {T}")
                st.latex("n = \\frac{PV}{RT}")
                result = (P * V) / (R * T)
                st.latex(f"n = \\frac{{{{{P} × {V}}}}}{{{{{R} × {T}}}}} = {result:.3f} \\ mol")
                st.success(f"✅ Jumlah mol (n) = {result:.3f} mol")
            
