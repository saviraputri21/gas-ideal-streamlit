import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator dan Breakdown Perhitungan","👥 Tentang Kami"])

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
# "🧮 Kalkulator dan Breakdown Perhitungan
# ================================
elif menu == "📉 Breakdown Perhitungan":
    st.title("📉 Breakdown Perhitungan Gas Ideal")
    st.markdown("Masukkan **3 variabel** dan pilih variabel yang ingin dihitung. Kami akan menunjukkan proses perhitungannya secara langkah-demi-langkah.")
    
    option = st.selectbox("Variabel yang akan dihitung", ["Tekanan (P)", "Volume (V)", "Jumlah mol (n)", "Suhu (T)"])
    
    # Input sesuai pilihan
    if option != "Tekanan (P)":
        P = st.number_input("Tekanan (P) dalam atm", min_value=0.001, format="%.4f")
    if option != "Volume (V)":
        V = st.number_input("Volume (V) dalam liter", min_value=0.001, format="%.4f")
    if option != "Jumlah mol (n)":
        n = st.number_input("Jumlah mol (n)", min_value=0.001, format="%.4f")
    if option != "Suhu (T)":
        T = st.number_input("Suhu (T) dalam Kelvin", min_value=0.001, format="%.4f")

    R = 0.0821

    if st.button("Tampilkan Breakdown"):
        st.markdown("### 🧾 Langkah-langkah Perhitungan:")

        if option == "Tekanan (P)":
            st.latex("P = \\frac{nRT}{V}")
            st.write(f"1. Masukkan nilai: P = ({n} mol) x ({R} L·atm/mol·K) x ({T} K) / ({V} L)")
            hasil = (n * R * T) / V
            st.write(f"2. Hitung: P = {n * R * T:.4f} / {V} = **{hasil:.4f} atm**")

        elif option == "Volume (V)":
            st.latex("V = \\frac{nRT}{P}")
            st.write(f"1. Masukkan nilai: V = ({n} mol) x ({R} L·atm/mol·K) x ({T} K) / ({P} atm)")
            hasil = (n * R * T) / P
            st.write(f"2. Hitung: V = {n * R * T:.4f} / {P} = **{hasil:.4f} L**")

        elif option == "Jumlah mol (n)":
            st.latex("n = \\frac{PV}{RT}")
            st.write(f"1. Masukkan nilai: n = ({P} atm) x ({V} L) / ({R} L·atm/mol·K x {T} K)")
            hasil = (P * V) / (R * T)
            st.write(f"2. Hitung: n = {P * V:.4f} / {R * T:.4f} = **{hasil:.4f} mol**")

        elif option == "Suhu (T)":
            st.latex("T = \\frac{PV}{nR}")
            st.write(f"1. Masukkan nilai: T = ({P} atm) x ({V} L) / ({n} mol x {R} L·atm/mol·K)")
            hasil = (P * V) / (n * R)
            st.write(f"2. Hitung: T = {P * V:.4f} / {n * R:.4f} = **{hasil:.2f} K**")

        st.success("✅ Perhitungan berhasil ditampilkan.")
        st.caption("Konstanta gas R = 0.0821 L·atm/mol·K")
