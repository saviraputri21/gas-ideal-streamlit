import streamlit as st
# Tambahkan CSS untuk background
st.markdown(
    """
    <style>
    /* Ganti latar belakang halaman */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1581093588401-4bb0b5a0b246?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: red;
    }

    /* Tambahkan latar belakang semi-transparan untuk konten utama */
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 15px;
    }

    /* Ubah warna teks untuk kontras */
    h1, h2, h3, h4, h5, h6, p, label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator","🧾 BREAKDOWN PERHITUNGAN PAGE","👥 Tentang Kami"])

# ================================
# 🏠 HOME PAGE
# ================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.markdown(r"""
    ## Persamaan Gas Ideal
    \[
    **PV = nRT**
    \]
    
    Keterangan
    - P : Tekanan (atm)  
    - V : Volume (L)  
    - n : Jumlah mol  
    - R : 0.0821 L·atm/mol·K  
    - T : Suhu (K)

    Aplikasi ini membantu menghitung salah satu variabel jika tiga lainnya diketahui.
    """)
    st.info("Pilih halaman di sidebar untuk menggunakan kalkulator atau melihat grafik hubungan volume & tekanan.")

# ================================
# 📊 DASHBOARD PAGE
# ================================
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
    Pada suhu tetap, volume berbanding terbalik dengan tekanan.  
    PV = Konstan
    
    P1.V1 = P2.V2
    
    **2. Hukum Charles**  
    Pada tekanan tetap, volume berbanding lurus dengan suhu.  
      VT = Konstan
      
      V1/T1 = V2/T2

    **3. Hukum Gay-Lussac**  
    Pada volume tetap, tekanan berbanding lurus dengan suhu.  
      P/T = Konstan
      
      (P1/T1 = P2/T2)
     
    ---

    ## ⚛️ Sifat-Sifat Gas Ideal

    1. Partikel bergerak secara acak dalam semua arah  
    2. Tidak ada gaya tarik menarik antar molekul  
    3. Ukuran partikel sangat kecil 
    4. Partikel terdistribusi merata dalam ruang  
    5. Tumbukan antar partikel adalah lenting sempurna  
    6. Energi kinetik rata-rata sebanding dengan suhu

    ---

    🔍 Catatan: Tidak ada gas yang 100% ideal di dunia nyata, namun model ini sangat berguna dalam ilmu kimia dan fisika!
    """)
    
# ================================
# 👥 Tentang Kami
# ================================
elif menu == "👥 Tentang Kami":
    st.title("👥 Tentang Kami")
    st.markdown("""
    ### Tim Pengembang Aplikasi Kalkulator Gas Ideal


    Selamat datang di PV-nRTin Aja! 🧪
    
    Sebuah platform kalkulator gas ideal yang dibuat untuk mahasiswa, pelajar, atau pejuang tugas akhir—yang sering berkutat dengan rumus legendaris PV = nRT 😵‍💫
    Di dunia teknik dan sains, perhitungan gas ideal itu penting banget, tapi jujur aja... kadang ribet 😅. 
    
    Nah, di sinilah kami hadir: biar kamu bisa fokus ke konsepnya, dan biarkan sistem kami yang ngurusin hitung-hitungan nya ✨📊
    Nama PV-nRTin Aja kami pilih bukan cuma biar catchy, tapi juga sebagai ajakan:
    💬 nggak usah ribet, tinggal masukin data... terus “PV-nRTin Aja”! 🚀
    
    Dengan tampilan simpel dan nuansa khas anak sains dan teknik, kami ingin bantu kamu belajar dengan cara yang praktis🎯
    
    Karena hidup udah cukup berat...
    
    📌 Jangan biarkan tekanan gas ikut bikin tekanan batin 🤖💨

   Terima kasih atas kunjungan dan kepercayaan Anda menggunakan aplikasi ini.
   Kami berharap aplikasi yang kami kembangkan dapat memberikan kemudahan dalam memahami konsep Hukum Gas Ideal
   serta membantu menghitung gas ideal.
   
   📘**Disusun oleh Kelompok 2**
   
   **Anggota Kelompok:** 
   - Azka Afriyuni Suwito (2360084)
   - Dhelys Kusuma Wardani (2460356)
   - Ismi Aziz(2460393)
   - Mutia Ningrum (2460444)
   - Savira Putri Pramudita (2460514)
   
    """)

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

def gas_ideal_calculator():
    R = 0.0821  # atm·L/mol·K (bisa ditambah opsi satuan lain)
    print("=== KALKULATOR GAS IDEAL (PV = nRT) ===")
    print("Masukkan nilai, ketik 'x' untuk variabel yang ingin dicari.")

    # Input dari user
    P = input("Tekanan (P) dalam atm: ")
    V = input("Volume (V) dalam liter: ")
    n = input("Mol (n): ")
    T = input("Suhu (T) dalam Celsius: ")

    # Ubah suhu ke Kelvin
    if T != 'x':
        T = float(T) + 273.15

    # Hitung berdasarkan variabel yang hilang
    if P == 'x':
        V = float(V)
        n = float(n)
        P = (n * R * T) / V
        print(f"Tekanan (P) = {P:.3f} atm")

    elif V == 'x':
        P = float(P)
        n = float(n)
        V = (n * R * T) / P
        print(f"Volume (V) = {V:.3f} liter")

    elif n == 'x':
        P = float(P)
        V = float(V)
        n = (P * V) / (R * T)
        print(f"Mol (n) = {n:.3f} mol")

    elif T == 'x':
        P = float(P)
        V = float(V)
        n = float(n)
        T = (P * V) / (n * R)
        print(f"Suhu (T) = {T - 273.15:.2f} °C (atau {T:.2f} K)")

    else:
        print("Semua variabel terisi. Tidak ada yang perlu dihitung.")

# Jalankan kalkulator
gas_ideal_calculator()

# ================================
# 🧾 BREAKDOWN PERHITUNGAN PAGE
# ================================
menu = st.sidebar.selectbox(...)
if menu == "🏠 Home":
    ...
elif menu == "📊 Dashboard":
    ...
elif menu == "🧾 Breakdown Perhitungan":
    ...
elif menu == "🧾 Breakdown Perhitungan":
    st.title("🧾 Breakdown Perhitungan")
    st.markdown("Masukkan **3 variabel** dan kosongkan **1 variabel** dengan mengisi angka 0 (nol). Sistem akan menampilkan langkah perhitungannya.")

    # Input user
    P = st.number_input("Tekanan (P) dalam atm", value=0.0, key="bp_P")
    V = st.number_input("Volume (V) dalam liter", value=0.0, key="bp_V")
    n = st.number_input("Jumlah mol (n)", value=0.0, key="bp_n")
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0, key="bp_T")
    R = 0.0821

    if st.button("Tampilkan Breakdown"):
        zero_count = sum([P == 0, V == 0, n == 0, T == 0])
        if zero_count != 1:
            st.error("Tolong kosongkan tepat satu variabel (isi dengan 0), dan isi 3 variabel lainnya dengan nilai > 0.")
        else:
            st.subheader("🔍 Langkah-Langkah Perhitungan")

            if P == 0:
                st.latex("PV = nRT")
                st.markdown(f"""
                Nilai yang diketahui:
                - n = {n} mol  
                - R = 0.0821 L·atm/mol·K  
                - T = {T} K  
                - V = {V} L  
                """)
                st.latex("P = \\frac{{nRT}}{{V}}")
                P = (n * R * T) / V
                st.latex(f"P = \\frac{{{n} × {R} × {T}}}{{{V}}} = {P:.3f} \\ atm")
                st.success(f"✅ Tekanan (P) = {P:.3f} atm")

            elif V == 0:
                st.latex("PV = nRT")
                st.markdown(f"""
                Nilai yang diketahui:
                - n = {n} mol  
                - R = 0.0821 L·atm/mol·K  
                - T = {T} K  
                - P = {P} atm  
                """)
                st.latex("V = \\frac{{nRT}}{{P}}")
                V = (n * R * T) / P
                st.latex(f"V = \\frac{{{n} × {R} × {T}}}{{{P}}} = {V:.3f} \\ liter")
                st.success(f"✅ Volume (V) = {V:.3f} liter")

            elif n == 0:
                st.latex("PV = nRT")
                st.markdown(f"""
                Nilai yang diketahui:
                - P = {P} atm  
                - V = {V} L  
                - R = 0.0821 L·atm/mol·K  
                - T = {T} K  
                """)
                st.latex("n = \\frac{{PV}}{{RT}}")
                n = (P * V) / (R * T)
                st.latex(f"n = \\frac{{{P} × {V}}}{{{R} × {T}}} = {n:.3f} \\ mol")
                st.success(f"✅ Jumlah mol (n) = {n:.3f} mol")

            elif T == 0:
                st.latex("PV = nRT")
                st.markdown(f"""
                Nilai yang diketahui:
                - P = {P} atm  
                - V = {V} L  
                - n = {n} mol  
                - R = 0.0821 L·atm/mol·K  
                """)
                st.latex("T = \\frac{{PV}}{{nR}}")
                T = (P * V) / (n * R)
                st.latex(f"T = \\frac{{{P} × {V}}}{{{n} × {R}}} = {T:.2f} \\ K")
                st.success(f"✅ Suhu (T) = {T:.2f} K")

    st.caption("Breakdown ditampilkan berdasarkan persamaan PV = nRT dengan konstanta R = 0.0821 L·atm/mol·K")
