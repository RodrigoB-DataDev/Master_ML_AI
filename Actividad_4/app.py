import streamlit as st
import google.generativeai as genai
import os

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Toolkit",
    page_icon="🧠",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=DM+Mono:wght@300;400&display=swap');

html, body, [class*="css"] { font-family: 'DM Mono', monospace; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; font-weight: 800 !important; }
.stApp { background: #0e0e10; color: #f0ede6; }
.block-container { padding-top: 2rem; max-width: 780px; }
.app-header { text-align: center; margin-bottom: 2.5rem; }
.app-header h1 { font-size: 3rem; letter-spacing: -2px; color: #f0ede6; margin-bottom: 0.2rem; }
.app-header p { color: #888; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; }
div[data-testid="stTabs"] button { font-family: 'Syne', sans-serif !important; font-weight: 600; color: #888 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: #f0ede6 !important; border-bottom: 2px solid #c8f04b !important; }
.stTextArea textarea { background: #18181c !important; border: 1px solid #2a2a30 !important; border-radius: 8px !important; color: #f0ede6 !important; font-family: 'DM Mono', monospace !important; font-size: 0.88rem !important; }
.stButton > button { background: #c8f04b !important; color: #0e0e10 !important; font-family: 'Syne', sans-serif !important; font-weight: 700 !important; border: none !important; border-radius: 6px !important; padding: 0.55rem 1.6rem !important; }
.result-box { background: #18181c; border: 1px solid #2a2a30; border-left: 3px solid #c8f04b; border-radius: 8px; padding: 1.2rem 1.4rem; margin-top: 1rem; font-size: 0.9rem; line-height: 1.7; white-space: pre-wrap; }
.stSelectbox > div > div { background: #18181c !important; border: 1px solid #2a2a30 !important; color: #f0ede6 !important; border-radius: 8px !important; }
label { color: #aaa !important; font-size: 0.78rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; }
</style>
""", unsafe_allow_html=True)

# ── Gemini setup ───────────────────────────────────────────────────────────────
def call_gemini(system: str, user: str) -> str:
    """Configure Gemini and return generated text."""
    api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
    if not api_key:
        st.error("⚠️ No se encontró GEMINI_API_KEY. Añádela en los secrets de Streamlit.")
        st.stop()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"{system}\n\nTexto:\n{user}"
    response = model.generate_content(prompt)
    return response.text


# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <h1>🧠 AI Toolkit</h1>
  <p>Análisis · Resumen · Traducción — powered by Gemini</p>
</div>
""", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["💬 Sentimiento", "📄 Resumen", "🌍 Traducción"])

# ── TAB 1 — Análisis de sentimiento ───────────────────────────────────────────
with tab1:
    st.markdown("### Análisis de Sentimiento")
    st.caption("Detecta el tono emocional de cualquier texto — reseñas, tweets, feedback, etc.")

    example_s = "La película estuvo increíble, los actores hicieron un trabajo excepcional aunque el final me dejó un poco confundido."

    text_s = st.text_area(
        "TEXTO A ANALIZAR",
        placeholder=f"Ejemplo: {example_s}",
        height=160,
        key="s_input",
    )

    c1, c2 = st.columns([1, 3])
    with c1:
        btn_s = st.button("Analizar", key="btn_s")
    with c2:
        if st.button("Usar ejemplo →", key="ex_s"):
            text_s = example_s

    if btn_s:
        if not text_s.strip():
            st.warning("Escribe o pega algún texto primero.")
        else:
            with st.spinner("Analizando sentimiento…"):
                system_s = (
                    "Eres un experto en análisis de sentimientos. "
                    "Analiza el texto y responde SIEMPRE con este formato exacto:\n\n"
                    "SENTIMIENTO GENERAL: [Positivo / Negativo / Neutro / Mixto]\n"
                    "PUNTUACIÓN: [número del 1 al 10]\n"
                    "EMOCIONES DETECTADAS: [lista separada por comas]\n"
                    "EXPLICACIÓN: [2-3 frases explicando el análisis]\n\n"
                    "Responde en el mismo idioma que el texto."
                )
                try:
                    result = call_gemini(system_s, text_s)
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error al llamar a la API: {e}")

# ── TAB 2 — Resumen ────────────────────────────────────────────────────────────
with tab2:
    st.markdown("### Resumidor de Textos")
    st.caption("Condensa artículos, informes o cualquier texto largo en su esencia.")

    example_r = (
        "La inteligencia artificial generativa ha transformado múltiples industrias. "
        "Los modelos de lenguaje grande han demostrado capacidades sorprendentes pero también "
        "plantean desafíos: desinformación, sesgos, impacto en el empleo. Los gobiernos de todo "
        "el mundo trabajan en marcos regulatorios para equilibrar la innovación con la seguridad."
    )

    text_r = st.text_area(
        "TEXTO A RESUMIR",
        placeholder="Pega aquí el texto largo que quieres resumir…",
        height=200,
        key="r_input",
    )

    length = st.selectbox(
        "LONGITUD DEL RESUMEN",
        ["Muy corto (1-2 frases)", "Corto (1 párrafo)", "Medio (3-5 puntos clave)", "Detallado"],
        key="r_len",
    )

    c1, c2 = st.columns([1, 3])
    with c1:
        btn_r = st.button("Resumir", key="btn_r")
    with c2:
        if st.button("Usar ejemplo →", key="ex_r"):
            text_r = example_r

    if btn_r:
        if not text_r.strip():
            st.warning("Escribe o pega algún texto primero.")
        else:
            lmap = {
                "Muy corto (1-2 frases)": "en 1-2 frases máximo",
                "Corto (1 párrafo)": "en un único párrafo conciso",
                "Medio (3-5 puntos clave)": "en 3-5 puntos clave con viñetas",
                "Detallado": "en varios párrafos manteniendo las ideas principales",
            }
            with st.spinner("Generando resumen…"):
                system_r = (
                    f"Eres un experto en síntesis de información. "
                    f"Resume el texto {lmap[length]}. "
                    f"Conserva las ideas más importantes y elimina el relleno. "
                    f"Responde en el mismo idioma que el texto."
                )
                try:
                    result = call_gemini(system_r, text_r)
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error al llamar a la API: {e}")

# ── TAB 3 — Traducción ─────────────────────────────────────────────────────────
with tab3:
    st.markdown("### Traductor Inteligente")
    st.caption("Traduce texto con contexto y naturalidad, no solo palabra por palabra.")

    LANGS = [
        "Inglés", "Español", "Francés", "Alemán", "Italiano", "Portugués",
        "Chino (simplificado)", "Japonés", "Árabe", "Ruso", "Coreano", "Hindi",
    ]

    example_t = "La tecnología avanza más rápido de lo que podemos adaptarnos, pero eso siempre ha sido así a lo largo de la historia."

    text_t = st.text_area(
        "TEXTO A TRADUCIR",
        placeholder="Escribe o pega el texto que quieres traducir…",
        height=160,
        key="t_input",
    )

    ca, cb = st.columns(2)
    with ca:
        src = st.selectbox("IDIOMA ORIGEN", ["Detectar automáticamente"] + LANGS, key="src")
    with cb:
        tgt = st.selectbox("IDIOMA DESTINO", LANGS, index=1, key="tgt")

    tone = st.selectbox(
        "TONO",
        ["Neutro / Natural", "Formal", "Informal / Coloquial", "Técnico"],
        key="tone",
    )

    c1, c2 = st.columns([1, 3])
    with c1:
        btn_t = st.button("Traducir", key="btn_t")
    with c2:
        if st.button("Usar ejemplo →", key="ex_t"):
            text_t = example_t

    if btn_t:
        if not text_t.strip():
            st.warning("Escribe o pega algún texto primero.")
        else:
            src_info = "del idioma que detectes automáticamente" if src == "Detectar automáticamente" else f"del {src}"
            tmap = {
                "Neutro / Natural": "natural y fluido",
                "Formal": "formal y profesional",
                "Informal / Coloquial": "informal y coloquial",
                "Técnico": "técnico y preciso",
            }
            with st.spinner("Traduciendo…"):
                system_t = (
                    f"Eres un traductor profesional. Traduce el texto {src_info} al {tgt}. "
                    f"Usa un tono {tmap[tone]}. "
                    f"Devuelve ÚNICAMENTE la traducción, sin explicaciones ni comentarios. "
                    f"Adapta expresiones idiomáticas para que suenen naturales en el idioma destino."
                )
                try:
                    result = call_gemini(system_t, text_t)
                    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error al llamar a la API: {e}")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#444; font-size:0.75rem; letter-spacing:1px;'>"
    "POWERED BY GEMINI · GOOGLE AI · STREAMLIT"
    "</p>",
    unsafe_allow_html=True,
)
