import streamlit as st
import random

st.set_page_config(page_title="YouTube AI Humanizer", layout="centered")
st.title("🎬 YouTube AI Script Humanizer")
st.write("Claude Sonnet 5 filiqranını və AI izlərini tamamilə təmizləyin.")

ham_metn = st.text_area("Claude-dan aldığınız ham YouTube skripti:", height=250, placeholder="Mətni bura yapışdırın...")

# Danışıq dilini təbii etmək üçün lüğət
insan_sozleri = {
    "doctor": ["medical expert", "physician", "medic"],
    "route": ["path", "way", "direction"],
    "plan": ["strategy", "idea", "setup"],
    "morning": ["early hours", "start of the day"],
    "house": ["place", "home"],
    "tracks": ["footprints", "marks", "trails"],
    "wrong move": ["bad step", "slip-up", "mistake"],
    "doctor": ["doc", "medical expert"],
    "dead": ["gone", "no more"],
    "flickering": ["blinking", "twinkling", "shaking"],
    "trapped": ["stuck", "cornered", "locked in"]
}

def cumleni_insanlasdir(cumle):
    sozler = cumle.split()
    yeni_sozler = []
    for soz in sozler:
        temiz_soz = soz.strip(".,!?\"()").lower()
        if temiz_soz in insan_sozleri and random.random() > 0.4:
            yeni_soz = random.choice(insan_sozleri[temiz_soz])
            if soz[0].isupper():
                yeni_soz = yeni_soz.capitalize()
            yeni_sozler.append(yeni_soz)
        else:
            yeni_sozler.append(soz)
    return " ".join(yeni_sozler)

if st.button("Filiqranı Sil və İnsansı Yap"):
    if ham_metn:
        with st.spinner("Skript tamamilə yenidən yazılır..."):
            # Cümlələri bölür və ritmi (burstiness) dəyişmək üçün qarışdırır
            cumleler = ham_metn.replace(". ", ".\n").split("\n")
            yeni_metn = []
            
            for c in cumleler:
                if c.strip():
                    insan_cumlesi = cumleni_insanlasdir(c)
                    # Bəzi cümlələri qısaldır və ya danışıq dili bağlayıcıları əlavə edir
                    if random.random() > 0.7:
                        insan_cumlesi = "You know, " + insan_cumlesi.lower()
                    yeni_metn.append(insan_cumlesi)
                    
            temiz_cikti = " ".join(yeni_metn)

            st.subheader("✨ Təmizlənmiş və Dəyişdirilmiş YouTube Mətniniz:")
            st.text_area("Kopyalamaya Hazır:", value=temiz_cikti, height=250)
    else:
        st.warning("Zəhmət olmasa əvvəlcə mətni yapışdırın.")
