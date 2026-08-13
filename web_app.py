import streamlit as st
import requests
import re

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Remove watermarks and structurally rewrite text using dual-translation loop.")

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

def translate_text(text, target_lang, source_lang='en'):
    # Pulsuz və limitsiz beynəlxalq tərcümə mühərriki
    url = f"https://googleapis.com{source_lang}&tl={target_lang}&dt=t&q={requests.utils.quote(text)}"
    try:
        response = requests.get(url, timeout=10)
        result = response.json()
        translated_chunks = [chunk[0] for chunk in result[0] if chunk[0]]
        return "".join(translated_chunks)
    except:
        return text

def pro_humanize(text):
    # Addım 1: Mətni başqa bir dil qrupuna çevirərək daxili AI filiqran ritmini qırırıq
    intermediate = translate_text(text, target_lang='de', source_lang='en') # İngilis -> Alman
    # Addım 2: Mətni yenidən İngilis dilinə qaytarırıq (Cümlə strukturları tamamilə yenidən qurulur)
    humanized = translate_text(intermediate, target_lang='en', source_lang='de') # Alman -> İngilis
    
    # Addım 3: YouTube üçün danışıq dili filtri və robotik sözlərin təmizlənməsi
    humanized = re.sub(r'\b(Furthermore|Moreover|In conclusion|Crucial|Essential|Testament|Notably)\b', '', humanized, flags=re.IGNORECASE)
    return humanized.strip()

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Rewriting sentence architectures and breaking statistical patterns..."):
            temiz_cikti = pro_humanize(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=200)
    else:
        st.warning("Please enter some text first.")
