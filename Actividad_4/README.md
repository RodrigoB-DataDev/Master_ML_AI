# 🧠 AI Toolkit — Análisis · Resumen · Traducción

App web con IA generativa que integra tres herramientas de procesamiento de texto en una sola interfaz.

## ¿Qué hace?

| Pestaña | Función |
|---|---|
| 💬 Sentimiento | Detecta el tono emocional de cualquier texto: positivo, negativo, mixto, con puntuación y emociones |
| 📄 Resumen | Condensa textos largos en distintos formatos (1 frase, párrafo, puntos clave, detallado) |
| 🌍 Traducción | Traduce entre 12 idiomas con control de tono (formal, informal, técnico, neutro) |

Todas las funciones usan la **API de Anthropic (Claude)** como motor de IA.

## Tecnologías

- [Streamlit](https://streamlit.io/) — interfaz web
- [Anthropic Python SDK](https://github.com/anthropic/anthropic-sdk-python) — acceso a Claude
- Modelo: `claude-opus-4-5`

## Instalación local

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/ai-toolkit.git
cd ai-toolkit

# 2. Instala dependencias
pip install -r requirements.txt

# 3. Configura tu API key
#    Crea el archivo .streamlit/secrets.toml con:
#    ANTHROPIC_API_KEY = "sk-ant-..."

# 4. Ejecuta la app
streamlit run app.py
```

## Configurar la API key en local

Crea el archivo `.streamlit/secrets.toml`:

```toml
ANTHROPIC_API_KEY = "sk-ant-tu-clave-aqui"
```

> ⚠️ **Nunca subas este archivo a GitHub.** Añade `.streamlit/secrets.toml` a tu `.gitignore`.

## Deployment en Streamlit Cloud

1. Sube el repositorio a GitHub (público)
2. Ve a [share.streamlit.io](https://share.streamlit.io) y conecta el repo
3. En **Settings → Secrets**, añade:
   ```
   ANTHROPIC_API_KEY = "sk-ant-tu-clave-aqui"
   ```
4. Haz deploy — la app estará disponible en una URL pública

## Link a la app desplegada

> 🔗 [https://TU_APP.streamlit.app](https://TU_APP.streamlit.app)
> *(actualiza este link tras el deployment)*

## Capturas de pantalla

*(añade capturas aquí tras el deployment)*

## Estructura del proyecto

```
ai-toolkit/
├── app.py              # Código principal de la aplicación
├── requirements.txt    # Dependencias Python
└── README.md           # Este archivo
```
