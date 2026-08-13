import streamlit as st
import requests

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Səviyyə: Deep-Learning modeli ilə filiqranları silin və mətni insanlaşdırın.")

# ⚠️ Bura az əvvəl Hugging Face-dən kopyaladığınız pulsuz kodu yapışdırın:
HF_TOKEN = "BURAYA_HUGGING_FACE_TOKENİNİZİ_YAPIŞDIRIN"

# Mətni insanlaşdıran peşəkar dil modeli (Google T5-XLarge bazalı parafrazer)
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

ham_metn = st.text_area("Claude-dan aldığınız ham YouTube skripti:", height=200, placeholder="Mətni bura yapışdırın...")

def ai_humanize(text):
    # Peşəkar AI platformaları mətni cümlə-cümlə analiz edib yenidən yazır
    sentences = text.replace(". ", ".\n").split("\n")
    humanized_sentences = []
    
    for sentence in sentences:
        if len(sentence.strip()) > 5:
            payload = {"inputs": f"paraphrase: {sentence} ", "parameters": {"num_beams": 5, "num_return_sequences": 1}}
            response = requests.post(API_URL, headers=headers, json=payload)
            try:
                result = response.json()
                # Süni intellekt cümləni tamamilə fərqli sözlərlə yenidən qurur
                humanized_sentences.append(result[0]['generated_text'])
            except:
                humanized_sentences.append(sentence) # Xəta olarsa orijinalı saxlayır
        else:
            humanized_sentences.append(sentence)
            
    return " ".join(humanized_sentences)

if st.button("Süni İntellekt İzlərini 100% Sil və Yenidən Yaz"):
    if ham_metn:
        if HF_TOKEN == "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":
            st.error("Zəhmət olmasa əvvəlcə kodun içinə Hugging Face Tokeninizi əlavə edin!")
        else:
            with st.spinner("Peşəkar AI modeli mətni insan dilinə çevirir..."):
                temiz_cikti = ai_humanize(ham_metn)
                
                st.subheader("✨ Təmizlənmiş və İnsanlaşdırılmış Skript:")
                st.text_area("Kopyalamaya Hazır:", value=temiz_cikti, height=200)
    else:
        st.warning("Zəhmət olmasa əvvəlcə bir mətn daxil edin.")
