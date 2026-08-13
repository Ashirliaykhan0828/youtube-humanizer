import streamlit as st
import requests

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Remove watermarks and humanize text using Deep-Learning models.")

# ⚠️ Hugging Face tokeninizi bura daxil edin:
HF_TOKEN = "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" 

API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

def ai_humanize(text):
    sentences = text.replace(". ", ".\n").split("\n")
    humanized_sentences = []
    
    for sentence in sentences:
        if len(sentence.strip()) > 5:
            payload = {"inputs": f"paraphrase: {sentence} ", "parameters": {"num_beams": 5, "num_return_sequences": 1}}
            try:
                response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
                result = response.json()
                if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
                    humanized_sentences.append(result[0]['generated_text'])
                elif isinstance(result, dict) and 'generated_text' in result:
                    humanized_sentences.append(result['generated_text'])
                else:
                    humanized_sentences.append(sentence)
            except:
                humanized_sentences.append(sentence)
        else:
            humanized_sentences.append(sentence)
            
    return " ".join(humanized_sentences)

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Professional AI model is rewriting your script..."):
            temiz_cikti = ai_humanize(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=200)
    else:
        st.warning("Please enter some text first.")
