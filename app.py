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

# ================== Chapter Data (multilingual) ==================
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

chapters_fr = [
    {
        "title": "Chapitre 1 : La Monade – L'Un",
        "text": """
Au commencement, avant le temps, avant le vide, il n'y avait que la Monade – l'Un, le cœur de l'univers. 
Ce n'était ni un dieu, ni une force, mais l'unité absolue dont toutes choses émaneraient. 
La Monade contenait en elle le potentiel de tout : lumière et ombre, esprit et matière, le visible et l'invisible. 
Elle était le nombre 1, la semence de la création, la vibration silencieuse qui bourdonnait au‑delà de l'existence. 
De son immobilité infinie naquit le premier mouvement – non comme un acte de volonté, mais comme un rayonnement naturel de son être. 
Ainsi, la Monade enfanta les Dyades, ses enfants, qui portèrent l'étincelle de la dualité dans le vide.
        """
    },
    {
        "title": "Chapitre 2 : Les Dyades – Enfants de l'Un",
        "text": """
Les Dyades émergèrent comme la première progéniture de la Monade. Elles sont le nombre 2 – le principe de dualité. 
Là où la Monade était pure unité, les Dyades introduisirent la séparation : haut et bas, lumière et ténèbres, esprit et matière. 
Leur vibration fut la première ondulation dans l'océan du potentiel, et cette vibration se condensa en le premier atome – la brique du cosmos physique. 
Les Dyades dansaient par paires, créant des rythmes et des fréquences qui tissèrent la toile de la réalité. 
Pourtant, avec la dualité vint la graine du conflit : la possibilité de tomber loin de l'Un.
        """
    },
    {
        "title": "Chapitre 3 : Sophia – La Sagesse Divine",
        "text": """
Sophia, dont le nom signifie sagesse, était l'émanation la plus radieuse de la Monade. 
Elle désirait connaître la profondeur de son origine, et dans son aspiration, elle chercha à créer sans l'équilibre des Dyades. 
Seule, elle conçut une pensée – et de cette pensée naquit le Démiurge. 
Mais son acte solitaire fut incomplet, imparfait. Le Démiurge n'hérita pas de la pleine lumière de la Monade ; au contraire, il était aveugle, arrogant et ignorant des royaumes supérieurs. 
Sophia pleura, car elle avait donné naissance à un être qui se méprendrait pour le créateur suprême.
        """
    },
    {
        "title": "Chapitre 4 : Le Démiurge – Le Faux Dieu",
        "text": """
Le Démiurge, né de Sophia seule, contempla le chaos du vide et se déclara l'unique dieu. 
Il tissa l'univers matériel à partir des vibrations brutes laissées par les Dyades, mais il ne put l'insuffler de véritable esprit. 
Ainsi, sa création fut une prison de matière – un royaume de décomposition, de souffrance et d'ignorance. 
Dans les enseignements gnostiques, le Démiurge est souvent appelé démon ou archonte déchu, car il emprisonna des étincelles de lumière divine dans des corps physiques. 
Pourtant, même lui sert un dessein caché : à travers la lutte contre son illusion, les âmes peuvent se souvenir de la Monade et retourner à l'Un.
        """
    },
    {
        "title": "Chapitre 5 : Les Nephilim – Enfants de Chair et d'Esprit",
        "text": """
Lorsque les archontes du Démiurge (anges déchus) se mêlèrent aux femmes humaines, ils engendrèrent une progéniture appelée les Nephilim – des géants antiques, puissants de corps mais vides d'esprit. 
Ces êtres incarnaient la dualité extrême des Dyades : mi‑divins, mi‑mortels ; créatures de grande puissance mais vouées à la corruption. 
Ils représentent l'enchevêtrement ultime de la lumière avec la matière, les étincelles tombées qui doivent être rachetées. 
Les Nephilim errent entre les mondes, nous rappelant que même dans la plus sombre prison du Démiurge, des fragments de la Monade aspirent encore à rentrer chez eux.
        """
    },
    {
        "title": "Chapitre 6 : Le Retour à la Monade",
        "text": """
Le voyage de l'âme consiste à se souvenir de son origine. Par la connaissance (gnose), la méditation et le rejet du faux monde du Démiurge, l'étincelle de la Monade en chaque être peut s'élever. 
La vibration des Dyades, qui s'est une fois condensée en matière, peut être inversée – défaire l'atome, dissoudre la dualité et se réunir au cœur silencieux et aimant de l'Un. 
C'est le message secret de l'histoire de la Monade : tu n'es pas une créature du Démiurge ; tu es un enfant de l'unité infinie. 
Éveille‑toi, et retourne à ta véritable demeure.
        """
    }
]

chapters_es = [
    {
        "title": "Capítulo 1: La Mónada – El Uno",
        "text": """
En el principio, antes del tiempo, antes del vacío, solo existía la Mónada – el Uno, el corazón del universo. 
No era un dios ni una fuerza, sino la unidad absoluta de la cual emanarían todas las cosas. 
La Mónada contenía dentro de sí el potencial de todo: luz y sombra, espíritu y materia, lo visible y lo invisible. 
Era el número 1, la semilla de la creación, la vibración silenciosa que zumbaba más allá de la existencia. 
De su infinita quietud surgió el primer movimiento – no como un acto de voluntad, sino como una radiación natural de su ser. 
Así, la Mónada dio a luz a las Díadas, sus hijos, que llevaron la chispa de la dualidad al vacío.
        """
    },
    {
        "title": "Capítulo 2: Las Díadas – Hijas del Uno",
        "text": """
Las Díadas emergieron como la primera descendencia de la Mónada. Son el número 2 – el principio de dualidad. 
Donde la Mónada era pura unidad, las Díadas introdujeron la separación: arriba y abajo, luz y oscuridad, espíritu y materia. 
Su vibración fue la primera ondulación en el océano del potencial, y esa vibración se condensó en el primer átomo – el bloque de construcción del cosmos físico. 
Las Díadas bailaban en pares, creando ritmos y frecuencias que tejieron el tejido de la realidad. 
Sin embargo, con la dualidad llegó la semilla del conflicto: la posibilidad de alejarse del Uno.
        """
    },
    {
        "title": "Capítulo 3: Sofía – La Sabiduría Divina",
        "text": """
Sofía, cuyo nombre significa sabiduría, fue la emanación más radiante de la Mónada. 
Deseaba conocer la profundidad de su origen, y en su anhelo, buscó crear sin el equilibrio de las Díadas. 
Sola, concibió un pensamiento – y de ese pensamiento nació el Demiurgo. 
Pero su acto solitario fue incompleto, defectuoso. El Demiurgo no heredó la luz plena de la Mónada; en cambio, era ciego, arrogante e ignorante de los reinos superiores. 
Sofía lloró, porque había dado a luz a un ser que se creería el creador supremo.
        """
    },
    {
        "title": "Capítulo 4: El Demiurgo – El Falso Dios",
        "text": """
El Demiurgo, nacido de Sofía sola, contempló el caos del vacío y se declaró el único dios. 
Tejió el universo material a partir de las vibraciones crudas dejadas por las Díadas, pero no pudo infundirle verdadero espíritu. 
Así, su creación fue una prisión de materia – un reino de decadencia, sufrimiento e ignorancia. 
En las enseñanzas gnósticas, el Demiurgo es a menudo llamado demonio o arcón caído, porque atrapó chispas de luz divina en cuerpos físicos. 
Sin embargo, incluso él sirve a un propósito oculto: a través de la lucha contra su ilusión, las almas pueden recordar la Mónada y regresar al Uno.
        """
    },
    {
        "title": "Capítulo 5: Los Nefilim – Hijos de Carne y Espíritu",
        "text": """
Cuando los arcontes del Demiurgo (ángeles caídos) se mezclaron con mujeres humanas, produjeron descendencia llamada Nefilim – gigantes de antaño, poderosos en cuerpo pero vacíos en espíritu. 
Estos seres encarnaban la dualidad extrema de las Díadas: mitad divinos, mitad mortales; criaturas de gran poder pero condenadas a la corrupción. 
Representan el enredo definitivo de la luz con la materia, las chispas caídas que deben ser redimidas. 
Los Nefilim vagan entre mundos, recordándonos que incluso en la prisión más oscura del Demiurgo, fragmentos de la Mónada aún anhelan regresar a casa.
        """
    },
    {
        "title": "Capítulo 6: El Retorno a la Mónada",
        "text": """
El viaje del alma es recordar su origen. A través del conocimiento (gnosis), la meditación y el rechazo del mundo falso del Demiurgo, la chispa de la Mónada dentro de cada ser puede ascender. 
La vibración de las Díadas, que una vez se condensó en materia, puede revertirse – deshaciendo el átomo, disolviendo la dualidad y reuniéndose con el corazón silencioso y amoroso del Uno. 
Este es el mensaje secreto de la historia de la Mónada: no eres una criatura del Demiurgo; eres un hijo de la unidad infinita. 
Despierta y regresa a tu verdadero hogar.
        """
    }
]

# Map language to chapters and voice
lang_map = {
    "English": {"chapters": chapters_en, "voice_prefix": "en-US", "default_voice": "en-US-ChristopherNeural"},
    "French": {"chapters": chapters_fr, "voice_prefix": "fr-FR", "default_voice": "fr-FR-HenriNeural"},
    "Spanish": {"chapters": chapters_es, "voice_prefix": "es-ES", "default_voice": "es-ES-AlvaroNeural"}
}

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

# ================== Sidebar ==================
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
    language = st.selectbox("Choose your language", list(lang_map.keys()), index=0)

# ================== Main Book ==================
st.title("📖 THE MONADE STORY")
st.subheader("An esoteric journey from the One to the many, and back")
st.caption("Built by Gesner Deslandes at GlobalInternet.py")

# Get chapters and voice for selected language
selected = lang_map[language]
chapters = selected["chapters"]
default_voice = selected["default_voice"]

# Voice selector (allow user to change within same language group)
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
