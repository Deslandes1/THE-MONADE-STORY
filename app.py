import streamlit as st
import asyncio
import edge_tts
import base64
import os

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
    .energy-img {
        max-width: 200px;
        margin: 1rem auto;
        display: block;
        filter: drop-shadow(0 0 10px gold);
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

# ================== Chapter Data ==================
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
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Star_1.svg/200px-Star_1.svg.png"
    },
    {
        "title": "Chapter 2: The Dyades – Children of the One",
        "text": """
The Dyades emerged as the first offspring of the Monade. They are the number 2 – the principle of duality. 
Where the Monade was pure unity, the Dyades introduced separation: up and down, light and dark, spirit and matter. 
Their vibration was the first ripple in the ocean of potential, and that vibration condensed into the first atom – the building block of the physical cosmos. 
The Dyades danced in pairs, creating rhythms and frequencies that wove the fabric of reality. 
Yet, with duality came the seed of conflict: the possibility of falling away from the One.
        """,
        "image": "https://upload.wimedia.org/wikipedia/commons/thumb/4/41/Two_red_circles.svg/200px-Two_red_circles.svg.png"
    },
    {
        "title": "Chapter 3: Sophia – Divine Wisdom",
        "text": """
Sophia, whose name means wisdom, was the most radiant emanation of the Monade. 
She desired to know the depth of her origin, and in her longing, she sought to create without the balance of the Dyades. 
Alone, she conceived a thought – and from that thought, the Demiurge was born. 
But her solitary act was incomplete, flawed. The Demiurge did not inherit the full light of the Monade; instead, he was blind, arrogant, and ignorant of the higher realms. 
Sophia wept, for she had brought forth a being that would mistake itself for the supreme creator.
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Mandala_of_Wisdom.svg/200px-Mandala_of_Wisdom.svg.png"
    },
    {
        "title": "Chapter 4: The Demiurge – The False God",
        "text": """
The Demiurge, born of Sophia alone, looked upon the chaos of the void and declared himself the only god. 
He wove the material universe out of the raw vibrations left by the Dyades, but he could not infuse it with true spirit. 
Thus, his creation was a prison of matter – a realm of decay, suffering, and ignorance. 
In Gnostic teachings, the Demiurge is often called a demon or a fallen archon, for he trapped sparks of divine light within physical bodies. 
Yet even he serves a hidden purpose: through the struggle against his illusion, souls may remember the Monade and return to the One.
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Demiurge_%28gnostic%29.svg/200px-Demiurge_%28gnostic%29.svg.png"
    },
    {
        "title": "Chapter 5: The Nephilim – Children of Flesh and Spirit",
        "text": """
When the Demiurge’s archons (fallen angels) mingled with human women, they produced offspring called the Nephilim – giants of old, mighty in body but empty in spirit. 
These beings embodied the extreme duality of the Dyades: half‑divine, half‑mortal; creatures of great power yet doomed to corruption. 
They represent the ultimate entanglement of light with matter, the fallen sparks that must be redeemed. 
The Nephilim wander between worlds, reminding us that even in the darkest prison of the Demiurge, fragments of the Monade still yearn to return home.
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Anakim_giant.svg/200px-Anakim_giant.svg.png"
    },
    {
        "title": "Chapter 6: The Return to the Monade",
        "text": """
The journey of the soul is to remember its origin. Through knowledge (gnosis), meditation, and the rejection of the Demiurge's false world, the spark of the Monade within each being can ascend. 
The Dyades’ vibration, which once condensed into matter, can be reversed – unweaving the atom, dissolving duality, and reuniting with the silent, loving heart of the One. 
This is the secret message of the Monade story: you are not a creature of the Demiurge; you are a child of the infinite unity. 
Awaken, and return to your true home.
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Three_arrows_circle.svg/200px-Three_arrows_circle.svg.png"
    }
]

# ================== TTS Function ==================
async def text_to_audio(text, voice, output_file="temp_audio.mp3"):
    try:
        comm = edge_tts.Communicate(text, voice)
        await comm.save(output_file)
        return True
    except Exception as e:
        st.error(f"TTS error: {e}")
        return False

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
    st.markdown("**Complete digital book (source code + audio + images):**")
    st.markdown("**$29.99 USD** one‑time payment")
    st.markdown("*Lifetime updates, free email support*")
    st.markdown("---")
    st.caption("© 2025 GlobalInternet.py")

# ================== Main Book ==================
st.title("📖 THE MONADE STORY")
st.subheader("An esoteric journey from the One to the many, and back")
st.caption("Built by Gesner Deslandes at GlobalInternet.py")

# Voice selector for audio narration
voice = st.selectbox("🎧 Narration voice", [
    "en-US-ChristopherNeural",   # male US
    "en-US-JennyNeural",         # female US
    "en-GB-RyanNeural",          # male UK
    "fr-FR-HenriNeural",         # French
    "es-ES-AlvaroNeural"         # Spanish
], index=0)

# Loop through chapters
for idx, ch in enumerate(chapters):
    with st.container():
        st.markdown(f'<div class="chapter-card">', unsafe_allow_html=True)
        st.markdown(f"## {ch['title']}")
        
        # Image (energy / symbol)
        st.image(ch['image'], caption=f"Symbol of {ch['title'].split(':')[0]}", use_container_width=False, width=150)
        
        # Paragraph text
        st.markdown(ch['text'])
        
        # Audio playback
        audio_file = f"chapter_{idx}.mp3"
        if not os.path.exists(audio_file):
            # Generate audio on first run
            success = asyncio.run(text_to_audio(ch['text'], voice, audio_file))
            if not success:
                st.warning("Audio generation failed, but you can still read the text.")
        
        if os.path.exists(audio_file):
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
                audio_b64 = base64.b64encode(audio_bytes).decode()
                audio_html = f'<audio controls src="data:audio/mp3;base64,{audio_b64}"></audio>'
                st.markdown(audio_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    <p>✨ <strong>The Monade Story</strong> – A spiritual‑philosophical work by <strong>Gesner Deslandes</strong> ✨</p>
    <p>📖 All rights reserved – GlobalInternet.py | For inquiries: deslandes78@gmail.com</p>
    <p>🌌 May the One guide your inner spark back to unity.</p>
</div>
""", unsafe_allow_html=True)

# Cleanup (optional) – we leave generated audio files
