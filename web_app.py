import streamlit as st
import requests
import re

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Remove watermarks and structurally rewrite text using dual-translation loop.")

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

def translate_text(text, target_lang, source_lang='en'):
    # Pulsuz Google Tərcümə mühərrikinin tam stabil versiyası
    url = "https://googleapis.com"
    params = {
        "client": "gtx",
        "sl": source_lang,
        "tl": target_lang,
        "dt": "t",
        "q": text
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        result = response.json()
        
        # Google-dan gələn cavabın daxilindən mətni dəqiq çıxarırıq
        translated_text = ""
        if result and result[0]:
            for item in result[0]:
                if item[0]:
                    translated_text += item[0]
        return translated_text if translated_text else text
    except:
        return text

def pro_humanize(text):
    # Addım 1: Mətni Alman dilinə çeviririk (Cümlə strukturları avtomatik Alman qrammatikasına uyğun dəyişir)
    intermediate = translate_text(text, target_lang='de', source_lang='en')
    
    # Addım 2: Mətni yenidən İngilis dilinə qaytarırıq (Sözlər və sinonimlər tamamilə yenilənir)
    humanized = translate_text(intermediate, target_lang='en', source_lang='de')
    
    # Addım 3: Robotik keçid sözlərini təmizləyirik
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
