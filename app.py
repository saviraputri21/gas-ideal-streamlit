import streamlit as st

# ================================
# 🌈 Background biru
# ================================
st.markdown(
    """
    # Warna latar per halaman
if menu == "🏠 Home":
    bg_color = "#A8E6CF"  # hijau pastel
elif menu == "📊 Dashboard":
    bg_color = "#DCE775"  # kuning kehijauan
elif menu == "🧮 Kalkulator":
    bg_color = "#FFF9C4"  # kuning lembut
elif menu == "🧾 Breakdown Perhitungan":
    bg_color = "#FFECB3"  # krem keemasan
elif menu == "👥 Tentang Kami":
    bg_color = "#F8BBD0"  # pink muda
st.markdown(
    f"""
    <style>
st.markdown("""
    <style>
    /* Ubah warna latar belakang keseluruhan */
    .stApp {
        background-color: #E0F2F1; /* Hijau pastel lembut */
    }
    </style>
""", unsafe_allow_html=True)
        background-color: {bg_color};
        background-size: contain;
        background-repeat: repeat;
        background-position: center;
        background-attachment: fixed;
)
    .block-container {{
        background-color: rgba(255, 255, 255, 0.88);
st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #E0F2F1;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
        }}
    
        h1, h2, h3, h4, h5, h6, p, label, .markdown-text-container {{
            color: #000000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
        <style>
        .stApp {
            background-color: #A8E6CF;
            background-size: contain;
            background-repeat: repeat;
            background-position: center;
            background-attachment: fixed;
        }
    
        .block-container {
            background-color: rgba(255, 255, 255, 0.88);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }

        h1, h2, h3, h4, h5, h6, p, label, .markdown-text-container {
            color: #000000; /* black */
        }
        </style>
        """,
        unsafe_allow_html=True
    
# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator", "🧾 Breakdown Perhitungan","👥 Tentang Kami"])
    
# ================================
# 🏠 HOME PAGE
# ================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    # Konten aplikasi
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("### Persamaan Gas Ideal")
    st.markdown("**[ PV = nRT ]**")
    st.markdown("""
    **Keterangan:**
    - **P** : Tekanan (atm)  
    - **V** : Volume (L)  
    - **n** : Jumlah mol  
    - **R** : 0.0821 L·atm/mol·K  
    - **T** : Suhu (K)  
    """)
   
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


    Selamat datang di PV-nRTin Aja! 💻🧪
    
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

# ================================
# 🧾 Breakdown Perhitungan 
# ================================
if menu == "🏠 Home":
    ...
elif menu == "📊 Dashboard":
    ...
elif menu == "🧾 Breakdown Perhitungan":
    st.title("🧾 Breakdown Perhitungan Gas Ideal")
    st.markdown("Masukkan **3 variabel**, kosongkan **1 variabel** dengan angka `0`.")
    
    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821
    
    if st.button("🔍 Tampilkan Proses Perhitungan"):
        kosong = sum([P == 0, V == 0, n == 0, T == 0])

        if kosong != 1:
            st.error("Isi **3 variabel**, kosongkan **1** saja dengan 0!")
        else:
            st.subheader("📘 Langkah-Langkah Perhitungan")
            st.latex("PV = nRT")

        if P == 0:
            st.markdown("### Diketahui:")
            st.write(f"n = {n} mol, R = 0.0821 L·atm/mol·K, T = {T} K, V = {V} L")
            st.markdown("### Langkah:")
            st.latex("P = \\frac{nRT}{V}")
            st.latex(f"P = \\frac{{{n} × 0.0821 × {T}}}{{{V}}}")
            hasil = (n * R * T) / V
            st.success(f"**Tekanan (P)** = {hasil:.3f} atm")

        elif V == 0:
            st.markdown("### Diketahui:")
            st.write(f"n = {n} mol, R = 0.0821, T = {T} K, P = {P} atm")
            st.markdown("### Langkah:")
            st.latex("V = \\frac{nRT}{P}")
            st.latex(f"V = \\frac{{{n} × 0.0821 × {T}}}{{{P}}}")
            hasil = (n * R * T) / P
            st.success(f"**Volume (V)** = {hasil:.3f} liter")

        elif n == 0:
            st.markdown("### Diketahui:")
            st.write(f"P = {P} atm, V = {V} L, R = 0.0821, T = {T} K")
            st.markdown("### Langkah:")
            st.latex("n = \\frac{PV}{RT}")
            st.latex(f"n = \\frac{{{P} × {V}}}{{0.0821 × {T}}}")
            hasil = (P * V) / (R * T)
            st.success(f"**Jumlah mol (n)** = {hasil:.3f} mol")

        elif T == 0:
            st.markdown("### Diketahui:")
            st.write(f"P = {P} atm, V = {V} L, n = {n} mol, R = 0.0821")
            st.markdown("### Langkah:")
            st.latex("T = \\frac{PV}{nR}")
            st.latex(f"T = \\frac{{{P} × {V}}}{{{n} × 0.0821}}")
            hasil = (P * V) / (n * R)
            st.success(f"**Suhu (T)** = {hasil:.2f} K")

        st.caption("Perhitungan berdasarkan persamaan PV = nRT dengan R = 0.0821 L·atm/mol·K")
