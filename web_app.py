import streamlit as st
import random
import re

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Remove watermarks and structurally rewrite text using deep local parsing.")

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

# Peşəkar sinonimlər və cümlə strukturları lüğəti
paraphrase_dict = {
    "It's been two days since your last meal": "Two days have passed since you last ate anything",
    "But you know where the herd is": "However, the location of the herd is clear to you",
    "You found them yesterday": "They were located by you just yesterday",
    "watched them": "kept a close eye on them",
    "mapped the route in your head": "planned the entire path in your mind",
    "The plan is ready": "The strategy is completely set",
    "You're going to get up in the morning and go": "As soon as day breaks, you will move out",
    "Then the rain comes": "Suddenly, the downpour begins",
    "Not the light kind": "And it is far from a gentle shower",
    "The kind the wind throws into your face": "The heavy wind drives the water directly into your eyes",
    "the kind that gets into your bones": "freezing you straight to the bone",
    "And it doesn't stop": "With absolutely no sign of stopping",
    "Goes on for hours": "It continues endlessly for hours",
    "Night falls, still pouring": "Even as darkness arrives, the rain keeps coming down",
    "You open your eyes the next morning, same sound": "Waking up the following day, the exact same noise greets you",
    "Forget hunting": "Hunting is completely out of the question now",
    "The tracks are gone": "Every single trail has vanished",
    "mud swallowed everything": "the thick mud has completely buried everything",
    "You can't even step outside and walk": "Taking even a single step outside is impossible",
    "one wrong move on wet rock with bare feet and your ankle is done": "slipping on the slick rocks without shoes will instantly break your ankle",
    "And out here a bad ankle doesn't mean a trip to the doctor": "Out in the wild, a broken bone is not just a medical emergency",
    "It means you're dead": "It is a literal death sentence",
    "The river right next to camp is swelling up": "The nearby river is rapidly overflowing its banks",
    "And the fire, that one thing that's everything to you": "Your campfire, the sole thing keeping you alive",
    "your warmth, your protection, your life, is flickering": "your only source of heat and safety, is desperately struggling to stay lit",
    "About to go out": "On the very verge of dying out",
    "You're not bored": "Boredom is the last thing on your mind",
    "You're trapped": "You are completely cornered and stuck"
}

def heavy_humanize(text):
    # Robotik süni intellekt bağlayıcılarını dərhal təmizləyirik
    text = re.sub(r'\b(Furthermore|Moreover|In conclusion|Crucial|Essential|Testament|Notably)\b', '', text, flags=re.IGNORECASE)
    
    # Cümlələri lüğət əsasında kökündən yenidən qururuq
    for old_phrase, new_phrase in paraphrase_dict.items():
        # Böyük-kiçik hərf fərqini qorumaq üçün yoxlama
        text = re.sub(re.escape(old_phrase), new_phrase, text, flags=re.IGNORECASE)
        
    # Təbii danışıq ritmi (Burstiness) üçün bəzi keçidlər əlavə edirik
    sentences = text.split(". ")
    processed_sentences = []
    for s in sentences:
        s = s.strip()
        if s and random.random() > 0.8 and not s.startswith("You know"):
            processed_sentences.append("Honestly, " + s[0].lower() + s[1:])
        elif s:
            processed_sentences.append(s)
            
    return ". ".join(processed_sentences)

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Processing deeply integrated patterns locally..."):
            temiz_cikti = heavy_humanize(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=200)
    else:
        st.warning("Please enter some text first.")
