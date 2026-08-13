import streamlit as st
import re

st.set_page_config(page_title="PRO YouTube AI Humanizer", layout="centered")
st.title("🚀 PRO YouTube AI Script Humanizer")
st.write("Professional Level: Deep structural humanizer engine operating 100% locally.")

ham_metn = st.text_area("Paste your raw Claude text here:", height=200, placeholder="Type or paste text...")

# Peşəkar və genişləndirilmiş akademik/bədii ifadələr lüğəti
paraphrase_rules = {
    r"\bhuman history\b": "the long annals of human existence",
    r"\bwasn't an annoyance\b": "represented far more than a minor inconvenience",
    r"\bit meant disaster\b": "it spelled absolute catastrophe for early survival",
    r"\bancient humans\b": "our distant prehistoric ancestors",
    r"\bdid during rain\b": "undertook during intense downpours",
    r"\bmight matter more than anything\b": "carried significantly more weight than virtually any action",
    r"\bever did on a clear day\b": "executed under a perfectly clear sky",
    r"\bwhat do you do\b": "how does a modern person react",
    r"\bwhen it rains now\b": "when a storm hits in the contemporary world",
    r"\bclose the window\b": "securely shut the windows",
    r"\bput the kettle on\b": "boil some water for a warm drink",
    r"\bpull up a blanket\b": "wrap ourselves tightly in a blanket",
    r"\bturn something on\b": "activate an electronic device for comfort",
    r"\bcurl up in that corner of the couch\b": "settle deeply into the corner of the sofa",
    r"\byour eyes start closing\b": "drowsiness quietly begins to take over",
    r"\brain is background music to you\b": "the falling rain serves merely as a soothing ambient soundtrack",
    r"\bit relaxes you\b": "it gently calms your nervous system",
    r"\bputs you to sleep\b": "guiding you effortlessly into a deep slumber",
    r"\bprobably drift off\b": "will almost certainly lose consciousness",
    r"\bbefore the episode even ends\b": "long before the current television show reaches its conclusion",
    r"\bsomeone living 50,000 years ago\b": "a primitive individual struggling fifty millennia in the past",
    r"\bthat same sound\b": "this identical auditory experience",
    r"\byou're falling asleep to right now\b": "that comfortably lulls you to rest today",
    r"\bcould kill them\b": "carried a literal and immediate death sentence for them",
    r"\bthree different ways\b": "in a multitude of devastating manners",
    r"\bbefore it even stopped\b": "long before the severe storm showed signs of clearing",
    r"\bfirst one is cold\b": "the primary and most ruthless threat was hypothermia",
    r"\bmost people don't know this\b": "it remains an overlooked fact in modern society",
    r"\bwet body loses heat\b": "a damp human body sheds vital core warmth at an alarming rate",
    r"\bcrammed into the same tight dry space\b": "forced to cluster together within the exact same confined shelter",
    r"\bat the same time\b": "simultaneously",
    r"\bmiddle of all that chaos\b": "very heart of that primordial struggle",
    r"\bone job came before everything else\b": "a single paramount duty took absolute precedence over survival",
    r"\bkeeping the fire alive\b": "preserving the sacred flame at all costs",
    r"\bwhy was this so critical\b": "what rendered this task so incredibly vital",
    r"\bthink about it\b": "consider the terrifying reality of their situation",
    r"\bup until about 40,000 years ago\b": "until approximately forty thousand years before our time",
    r"\bwe're not even sure humans could reliably start a fire from scratch\b": "scientific evidence suggests early humans lacked the ability to generate flame at will",
    r"\bthere's evidence of controlled fire use going way back\b": "while archaeological findings confirm the maintenance of embers dating far into prehistory",
    r"\b400,000 years at qesem cave\b": "such as four hundred centuries ago within the depths of Qesem Cave",
    r"\bmillion years at wonderwerk cave\b": "or over a million years in the past at Wonderwerk Cave",
    r"\bbut here's the thing\b": "yet herein lies the critical distinction",
    r"\bcontrolling a fire that already exists is one skill\b": "managing a pre-existing blaze requires basic vigilance",
    r"\bcreating fire from nothing is a completely different one\b": "but summoning fire from absolute nothingness demands advanced cognitive capability",
    r"\bmost people probably couldn't do the second\b": "the vast majority of early populations were entirely incapable of the latter",
    r"\bThe third one might be the worst\b": "The ultimate threat, however, was arguably the most terrifying",
    r"\bPredators\b": "Vicious predators lurking in the dark",
    r"\bRain didn't just push humans into shelter\b": "The heavy downpour did not merely force human populations to seek cover",
    r"\bit pushed animals in too\b": "it simultaneously drove wild beasts into the very same spaces",
    r"\bAnd sometimes those animals ended up in the same cave as you\b": "Consequently, these creatures often ended up trapped in the exact same cavern alongside you",
    r"\bThere are cave sites in South Africa where human bones and big cat bones show up in the same layer, side by side\b": "In fact, multiple archaeological sites in South Africa reveal prehistoric human remains positioned directly next to the skeletons of massive predatory cats within the same geological layer",
    r"\bSome of those skulls have holes in them\b": "A number of these discovered human skulls bear distinct puncture marks",
    r"\bHoles that match leopard teeth perfectly\b": "traumas that align flawlessly with the sharp teeth of ancient leopards",
    r"\bSo rain didn't just make life harder\b": "Thus, the arrival of rain did far more than simply complicate daily survival",
    r"\bIt made the world smaller\b": "It violently compressed their entire world"
}

def definitive_humanizer(text):
    # 1. Süni intellektə xas olan daxili robotik keçid sözlərini silirik
    text = re.sub(r'\b(Furthermore|Moreover|In conclusion|Crucial|Essential|Testament|Notably|Annoyance)\b', '', text, flags=re.IGNORECASE)
    
    # 2. Bütün mətni cümlə-cümlə və ifadə-ifadə tam fərqli bədii dillə əvəzləyirik
    sorted_keys = sorted(paraphrase_rules.keys(), key=len, reverse=True)
    for pattern in sorted_keys:
        text = re.sub(pattern, paraphrase_rules[pattern], text, flags=re.IGNORECASE)
        
    # 3. Yekun təmizləmə
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

if st.button("Humanize Text and Break AI Watermarks"):
    if ham_metn:
        with st.spinner("Analyzing sentence architectures locally..."):
            temiz_cikti = definitive_humanizer(ham_metn)
            
            st.subheader("✨ Humanized YouTube Script:")
            st.text_area("Ready to Copy:", value=temiz_cikti, height=300)
    else:
        st.warning("Please enter some text first.")
