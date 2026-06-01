import streamlit as st
import asyncio
import edge_tts

# ================== Page Config ==================
st.set_page_config(
    page_title="The Monade Story – Esoteric Wisdom Book",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================== Styling ==================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #f0e6d0;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #ffd966;
    }
    .chapter-card {
        background: rgba(0,0,0,0.6);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-left: 5px solid #ffaa44;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background: rgba(0,0,0,0.5);
        border-radius: 15px;
    }
    .stButton button {
        background-color: #ffaa44;
        color: #1e1e2a;
        font-weight: bold;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
    }
    .avatar-img {
        border-radius: 50%;
        width: 80px;
        height: 80px;
        object-fit: cover;
        border: 2px solid #ffaa44;
        box-shadow: 0 0 15px rgba(255,170,68,0.5);
    }
</style>
""", unsafe_allow_html=True)

# ================== Chapter Data (multilingual) ==================
# ... (same as previous version, no changes) ...
# I'm keeping the full chapter data but to save space I'll only show the first one.
# In your actual file, keep the complete chapters_en, chapters_fr, chapters_es as before.

chapters_en = [
    {
        "title": "Chapter 1: The Monade – The One",
        "text": """
In the beginning, before time, before the void, there was only the Monade – the One, the heart of the universe. 
It was not a god, nor a force, but the absolute unity from which all things would emanate. 
The Monade contained within itself the potential of everything: light and shadow, spirit and matter, the seen and the unseen. 
It was the number 1, the seed of creation, the silent vibration that hummed beyond existence. 
From its infinite stillness, the first movement arose – not as an act of will, but as a natural radiation of its being. 
Thus, the Monade gave birth to the Dyades, its children, who carried the spark of duality into the void.
        """
    },
    # ... include all other chapters (2-6) as before ...
]

# Similarly chapters_fr and chapters_es (keep full content from previous version)

# ================== Cached Audio Generation ==================
@st.cache_data(show_spinner=False)
def get_audio_bytes(text, voice):
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(_generate())
    loop.close()
    return result

# ================== Sidebar (unchanged) ==================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/circled.png", width=80)
    st.markdown("## GlobalInternet.py")
    st.markdown("**Gesner Deslandes**, Engineer-in-Chief")
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("📱 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**Complete digital book (source code + audio + updates):**")
    st.markdown("**$29.99 USD** one‑time payment")
    st.markdown("*Lifetime updates, free email support*")
    st.markdown("---")
    st.caption("© 2025 GlobalInternet.py")
    
    # Language selection
    st.markdown("### 🌐 Language")
    language = st.selectbox("Choose your language", ["English", "French", "Spanish"], index=0)

# ================== Main Book with Avatar ==================
# Use two columns: title on left, picture on right
col1, col2 = st.columns([3, 1])
with col1:
    st.title("📖 THE MONADE STORY")
with col2:
    # Use raw GitHub URL for the image
    avatar_url = "https://raw.githubusercontent.com/Deslandes1/THE-MONADE-STORY/main/Gesner%20Deslandes.png"
    st.markdown(f'<img src="{avatar_url}" class="avatar-img" style="float:right;">', unsafe_allow_html=True)

st.subheader("An esoteric journey from the One to the many, and back")
st.caption("Built by Gesner Deslandes at GlobalInternet.py")

# Map language to chapters and voice
lang_map = {
    "English": {"chapters": chapters_en, "voice_prefix": "en-US", "default_voice": "en-US-ChristopherNeural"},
    "French": {"chapters": chapters_fr, "voice_prefix": "fr-FR", "default_voice": "fr-FR-HenriNeural"},
    "Spanish": {"chapters": chapters_es, "voice_prefix": "es-ES", "default_voice": "es-ES-AlvaroNeural"}
}

selected = lang_map[language]
chapters = selected["chapters"]
default_voice = selected["default_voice"]

# Voice selector
available_voices = {
    "English": ["en-US-ChristopherNeural", "en-US-JennyNeural", "en-GB-RyanNeural"],
    "French": ["fr-FR-HenriNeural", "fr-FR-DeniseNeural"],
    "Spanish": ["es-ES-AlvaroNeural", "es-ES-ElviraNeural"]
}
voice_options = available_voices.get(language, [default_voice])
voice = st.selectbox("🎧 Narration voice", voice_options, index=0)

# Display chapters
for ch in chapters:
    with st.container():
        st.markdown(f'<div class="chapter-card">', unsafe_allow_html=True)
        st.markdown(f"## {ch['title']}")
        st.markdown(ch['text'])
        with st.spinner("Generating audio..."):
            audio_bytes = get_audio_bytes(ch['text'], voice)
            st.audio(audio_bytes, format="audio/mp3")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    <p>✨ <strong>The Monade Story</strong> – A spiritual‑philosophical work by <strong>Gesner Deslandes</strong> ✨</p>
    <p>📖 All rights reserved – GlobalInternet.py | For inquiries: deslandes78@gmail.com</p>
    <p>🌌 May the One guide your inner spark back to unity.</p>
</div>
""", unsafe_allow_html=True)
