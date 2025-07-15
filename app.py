import streamlit as st

st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪")

st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
st.markdown("Isi tiga variabel, kosongkan satu (isi 0) untuk dihitung.")

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
        st.error("Kosongkan *tepat satu* variabel dengan nilai 0.")
