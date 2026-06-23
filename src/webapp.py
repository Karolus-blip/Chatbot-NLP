from pathlib import Path

import joblib
import streamlit as st

from chatbot import procesar_mensaje

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "intent_classifier.joblib"

@st.cache_resource
def cargar_modelo():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "No se encontró el modelo entrenado. Primero ejecuta: python src/train.py"
        )
    return joblib.load(MODEL_PATH)

def main():
    st.set_page_config(
        page_title="Chatbot NLP de librería",
        page_icon="📚",
        layout="wide"
    )

    st.title("📚 Chatbot NLP de librería")
    st.write(
        "Demostración de clasificación de intención mediante NLP."
    )

    modelo = cargar_modelo()

    # Inicializar memoria de conversación
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Barra lateral de depuración
    with st.sidebar:
        if st.button("🗑️ Limpiar conversación"):
            st.session_state.messages = []
            st.rerun()
        st.header("Información NLP")

        if "ultimo_intent" in st.session_state:
            st.write(
                f"**Intención detectada:** {st.session_state.ultimo_intent}"
            )

            st.write(
                f"**Confianza:** {st.session_state.ultima_confianza:.2f}"
            )

            st.subheader("Top 5 intenciones")

            for etiqueta, probabilidad in st.session_state.ultimo_ranking[:5]:
                st.write(
                    f"- {etiqueta}: {probabilidad:.2f}"
                )

            st.subheader("Entidades detectadas")

            if "ultimas_entidades" in st.session_state:
                if st.session_state.ultimas_entidades:
                    for clave, valor in (
                        st.session_state.ultimas_entidades.items()
                    ):
                        st.write(
                            f"**{clave}:** {valor}"
                        )
                else:
                    st.write(
                        "No se detectaron entidades."
                    )

    # Mostrar historial del chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Caja de entrada tipo ChatGPT
    prompt = st.chat_input(
        "Escribe tu mensaje..."
    )

    if prompt:

        # Mostrar mensaje del usuario
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        resultado = procesar_mensaje(prompt, modelo)

        st.session_state.ultimo_intent = resultado["intent"]
        st.session_state.ultima_confianza = resultado["confianza"]
        st.session_state.ultimo_ranking = resultado["ranking"]
        st.session_state.ultimas_entidades = resultado["entidades"]

        respuesta = resultado["respuesta"]

        # Guardar respuesta
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": respuesta
            }
        )

        st.rerun()


if __name__ == "__main__":
    main()
