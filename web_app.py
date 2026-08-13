import streamlit as st
import requests

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Advanced Rewrite Engine (Powered by Gemini 1.5 Flash)")

# 🔑 Sizin təqdim etdiyiniz rəsmi Google Gemini API Açarı koda yerləşdirildi:
GEMINI_API_KEY = "AQ.Ab8RN6KvPV3Slmk57YFJ7DptLTS8JCGbrIc-x4HRqnufVin-0A"

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

def gemini_humanize(text):
    # Nümunə şəkildəki kimi cümlə strukturunu pozmadan mətni insaniləşdirən peşəkar təlimat
    system_instruction = (
        "You are an expert YouTube script writer and professional humanizer. "
        "Your task is to take the provided AI-generated script and rewrite it into a highly engaging, "
        "natural, and human-like storytelling format. "
        "CRITICAL RULES:\n"
        "1. Do NOT change the core meaning, core facts, or timeline of the text.\n"
        "2. Keep the sentence structure and core meaning intact, but completely change the rigid, robotic AI phrasing.\n"
        "3. Enhance the emotional depth and vocabulary to make it sound like a gripping documentary or video essay.\n"
        "4. Absolutely remove all invisible AI mathematical watermarks and statistical patterns.\n"
        "5. Output ONLY the rewritten text, nothing else."
    )
    
    url = f"https://googleapis.com{GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{
                "text": f"{system_instruction}\n\nOriginal Text:\n{text}"
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        result = response.json()
        
        # Gemini API-dən gələn cavabı dəqiq çıxarırıq
        if 'candidates' in result and len(result['candidates']) > 0:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Error: Gemini model processing failed. Please check the response format."
    except Exception as e:
        return f"Connection error. Please try again. Details: {str(e)}"

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Gemini Engine is transforming your script into human storytelling..."):
            temiz_cikti = gemini_humanize(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=300)
    else:
        st.warning("Please enter some text first.")
