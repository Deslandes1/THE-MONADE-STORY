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
</style>
""", unsafe_allow_html=True)

# ================== Chapter Data (no images) ==================
chapters = [
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
    {
        "title": "Chapter 2: The Dyades – Children of the One",
        "text": """
The Dyades emerged as the first offspring of the Monade. They are the number 2 – the principle of duality. 
Where the Monade was pure unity, the Dyades introduced separation: up and down, light and dark, spirit and matter. 
Their vibration was the first ripple in the ocean of potential, and that vibration condensed into the first atom – the building block of the physical cosmos. 
The Dyades danced in pairs, creating rhythms and frequencies that wove the fabric of reality. 
Yet, with duality came the seed of conflict: the possibility of falling away from the One.
        """
    },
    {
        "title": "Chapter 3: Sophia – Divine Wisdom",
        "text": """
Sophia, whose name means wisdom, was the most radiant emanation of the Monade. 
She desired to know the depth of her origin, and in her longing, she sought to create without the balance of the Dyades. 
Alone, she conceived a thought – and from that thought, the Demiurge was born. 
But her solitary act was incomplete, flawed. The Demiurge did not inherit the full light of the Monade; instead, he was blind, arrogant, and ignorant of the higher realms. 
Sophia wept, for she had brought forth a being that would mistake itself for the supreme creator.
        """
    },
    {
        "title": "Chapter 4: The Demiurge – The False God",
        "text": """
The Demiurge, born of Sophia alone, looked upon the chaos of the void and declared himself the only god. 
He wove the material universe out of the raw vibrations left by the Dyades, but he could not infuse it with true spirit. 
Thus, his creation was a prison of matter – a realm of decay, suffering, and ignorance. 
In Gnostic teachings, the Demiurge is often called a demon or a fallen archon, for he trapped sparks of divine light within physical bodies. 
Yet even he serves a hidden purpose: through the struggle against his illusion, souls may remember the Monade and return to the One.
        """
    },
    {
        "title": "Chapter 5: The Nephilim – Children of Flesh and Spirit",
        "text": """
When the Demiurge’s archons (fallen angels) mingled with human women, they produced offspring called the Nephilim – giants of old, mighty in body but empty in spirit. 
These beings embodied the extreme duality of the Dyades: half‑divine, half‑mortal; creatures of great power yet doomed to corruption. 
They represent the ultimate entanglement of light with matter, the fallen sparks that must be redeemed. 
The Nephilim wander between worlds, reminding us that even in the darkest prison of the Demiurge, fragments of the Monade still yearn to return home.
        """
    },
    {
        "title": "Chapter 6: The Return to the Monade",
        "text": """
The journey of the soul is to remember its origin. Through knowledge (gnosis), meditation, and the rejection of the Demiurge's false world, the spark of the Monade within each being can ascend. 
The Dyades’ vibration, which once condensed into matter, can be reversed – unweaving the atom, dissolving duality, and reuniting with the silent, loving heart of the One. 
This is the secret message of the Monade story: you are not a creature of the Demiurge; you are a child of the infinite unity. 
Awaken, and return to your true home.
        """
    }
]

# ================== Cached Audio Generation ==================
@st.cache_data(show_spinner=False)
def get_audio_bytes(text, voice):
    """Generate audio using edge-tts and return bytes (cached per text+voice)."""
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    # Run the async function in a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(_generate())
    loop.close()
    return result

# ================== Sidebar Contact & Price ==================
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

# ================== Main Book ==================
st.title("📖 THE MONADE STORY")
st.subheader("An esoteric journey from the One to the many, and back")
st.caption("Built by Gesner Deslandes at GlobalInternet.py")

# Voice selector for audio narration
voice = st.selectbox(
    "🎧 Narration voice",
    [
        "en-US-ChristopherNeural",   # male US
        "en-US-JennyNeural",         # female US
        "en-GB-RyanNeural",          # male UK
        "fr-FR-HenriNeural",         # French
        "es-ES-AlvaroNeural"         # Spanish
    ],
    index=0
)

# Display chapters
for ch in chapters:
    with st.container():
        st.markdown(f'<div class="chapter-card">', unsafe_allow_html=True)
        st.markdown(f"## {ch['title']}")
        st.markdown(ch['text'])
        
        # Generate and play audio
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
