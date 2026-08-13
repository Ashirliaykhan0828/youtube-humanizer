import streamlit as st
import requests

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Advanced Rewrite Engine (Powered by Gemini 1.5 Flash)")

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

def gemini_humanize(text):
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
    
    url = "https://googleapis.com"
    headers = {"Content-Type": "application/json"}
    
    # ⚠️ Google Gemini API-nin rəsmi tələb etdiyi tam və qüsursuz məlumat strukturu (Payload):
    payload = {
        "contents": [{
            "parts": [{
                "text": system_instruction + "\n\nOriginal Text:\n" + text
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        result = response.json()
        
        # Google-dan gələn cavabı rəsmi struktura uyğun olaraq daxildən oxuyuruq
        if 'candidates' in result and len(result['candidates']) > 0:
            content = result['candidates'][0]['content']
            if 'parts' in content and len(content['parts']) > 0:
                return content['parts'][0]['text']
        
        if 'error' in result:
            return "API Error: " + str(result['error']['message'])
            
        return "Error: Google Gemini returned an unexpected data structure. Response: " + str(result)
    except Exception as e:
        return "Connection error to Google Server. Details: " + str(e)

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Gemini Cloud Engine is transforming your script into human storytelling..."):
            temiz_cikti = gemini_humanize(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=300)
    else:
        st.warning("Please enter some text first.")
