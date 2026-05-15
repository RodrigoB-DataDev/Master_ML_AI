# 🧠 AI Toolkit — Análisis · Resumen · Traducción

App web con IA generativa que integra tres herramientas de procesamiento de texto en una sola interfaz con pestañas.

## 🔗 App desplegada

**[https://mastermlai-tu7jx7q54u6x3gfse934hh.streamlit.app/](https://mastermlai-tu7jx7q54u6x3gfse934hh.streamlit.app/)**

---

## ¿Qué hace?

La app tiene 3 funcionalidades accesibles desde pestañas independientes:

**💬 Análisis de Sentimiento**
Analiza el tono emocional de cualquier texto. Devuelve el sentimiento general (Positivo / Negativo / Neutro / Mixto), una puntuación del 1 al 10, las emociones detectadas y una explicación de 2-3 frases. Funciona en cualquier idioma.

**📄 Resumidor de Textos**
Condensa textos largos en 4 formatos a elegir: muy corto (1-2 frases), corto (1 párrafo), medio (3-5 puntos clave con viñetas) o detallado (varios párrafos). Ideal para artículos, informes o cualquier texto extenso.

**🌍 Traductor Inteligente**
Traduce entre 12 idiomas (Inglés, Español, Francés, Alemán, Italiano, Portugués, Chino, Japonés, Árabe, Ruso, Coreano, Hindi) con detección automática del idioma origen y 4 modos de tono: neutro, formal, informal y técnico.

---

## 🛠 Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) — framework Python para la interfaz web
- [Groq API](https://console.groq.com/) — acceso gratuito al modelo LLaMA 3.3 70B de Meta
- Modelo: `llama-3.3-70b-versatile`
- Python 3

---

## 💻 Instalación local

```bash
# 1. Clona el repositorio
git clone https://github.com/RodrigoB-DataDev/Master_ML_AI.git
cd Master_ML_AI/Actividad_4

# 2. Instala dependencias
pip install -r requirements.txt

# 3. Crea el archivo de secrets con tu API key
mkdir -p .streamlit
echo 'GROQ_API_KEY = "gsk_tu_clave_aqui"' > .streamlit/secrets.toml

# 4. Ejecuta la app
streamlit run app.py
```

Obtén tu API key gratuita en [console.groq.com](https://console.groq.com) — sin tarjeta de crédito.

> ⚠️ **Nunca subas `.streamlit/secrets.toml` a GitHub.** Añádelo a tu `.gitignore`.

---

## ☁️ Deployment en Streamlit Cloud

1. Sube el repositorio a GitHub (público)
2. Ve a [share.streamlit.io](https://share.streamlit.io) y conecta el repo
3. En **Main file path** escribe: `Actividad_4/app.py`
4. En **Advanced settings → Secrets** añade:
   ```toml
   GROQ_API_KEY = "gsk_tu_clave_aqui"
   ```
5. Haz deploy — la app estará disponible en ~2 minutos

---

## 📁 Estructura del proyecto

```
Actividad_4/
├── app.py              # Código principal de la aplicación
├── requirements.txt    # Dependencias (streamlit, groq)
└── README.md           # Este archivo
```