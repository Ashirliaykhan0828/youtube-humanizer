import streamlit as st
import subprocess

st.set_page_config(page_title="YouTube AI Humanizer", layout="centered")
st.title("🎬 YouTube AI Script Humanizer")
st.write("Mac üçün xüsusi: Claude Sonnet 5 filiqranını və AI izlərini tamamilə təmizləyin.")

ham_metn = st.text_area("Claude-dan aldığınız ham YouTube skripti:", height=250, placeholder="Mətni bura yapışdırın...")

if st.button("Filiqranı Sil və İnsansı Yap"):
    if ham_metn:
        with st.spinner("Skript emal olunur..."):
            process = subprocess.Popen(['python3', 'humanize.py', '--mode', 'rewrite'], 
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            temiz_cikti, _ = process.communicate(input=ham_metn)
            
            st.subheader("✨ Təmizlənmiş YouTube Metniniz:")
            st.text_area("Kopyalamaya Hazır:", value=temiz_cikti, height=250)
    else:
        st.warning("Zəhmət olmasa əvvəlcə mətni yapışdırın.")
