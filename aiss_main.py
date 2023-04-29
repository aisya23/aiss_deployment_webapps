import streamlit as st

st.title("APLIKASI PERHITUNGAN NORMALITAS dan KADAR LARUTAN")
st.write("PERHITUNGAN NORMALITAS LARUTAN")

mg = st.number_input('Masukkan bobot zat terlarut (mg)')
FP = st.number_input('Masukkan nilai FP')
Mllarutan = st.number_input('Masukkan volume larutan (Ml)')
BE = st.number_input('masukkan nilai BE')

tombol = st.button('Hitung nilai normalitas')

if tombol:
    nilai_normalitas = mg/(FP*Mllarutan*BE)
    st.success(f'nilai normalitas adalah {nilai_normalitas}')
    
st.write("PERHITUNGAN KADAR LARUTAN DENGAN FP")

volumetitran = st.number_input('Masukkan volume titran (Ml)')
normalitastitran = st.number_input('Masukkan normalitas titran')
BEkadar = st.number_input('Masukkan nilai BE (kadar)')
volumetitrat = st.number_input('Masukkan volume titrat (Ml)')
FPkadar = st.number_input('Masukkan nilai FP (kadar)')
pelengkap = st.number_input('Masukkan angka 10')

tombol = st.button('Hitung nilai kadar (%)')

if tombol:
    nilai_kadar = (volumetitran*normalitastitran*BEkadar)/(volumetitrat*FPkadar*pelengkap)
    st.success(f'nilai kadar(%) adalah {nilai_kadar}%')
    
st.write("PERHITUNGAN KADAR LARUTAN TANPA FP")

xvolumetitran = st.number_input('Masukkan volume titran (Ml)_')
xnormalitastitran = st.number_input('Masukkan normalitas titran_')
xBEkadar = st.number_input('Masukkan nilai BE (kadar)_')
xvolumetitrat = st.number_input('Masukkan volume titrat (Ml)_')
xpelengkap = st.number_input('Masukkan angka 10_')

tombol = st.button('Hitung nilai kadar_ (%)')

if tombol:
    nilai_kadar = (xvolumetitran*xnormalitastitran*xBEkadar)/(xvolumetitrat*xpelengkap)
    st.success(f'nilai kadar(%) adalah {nilai_kadar}%')