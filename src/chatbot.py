from pathlib import Path

import random
import joblib

from intent_categories import (
    INTENCIONES_SOCIALES,
    INTENCIONES_FUNCIONALES,
)
from responses import RESPUESTAS
from database import (
        obtener_todos_los_libros,
        buscar_por_autor,
        buscar_por_titulo,
)
from entity_extractor import extraer_entidades
from book_info import obtener_info_libro


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "intent_classifier.joblib"
UMBRAL_CONFIANZA = 0.15


def cargar_modelo():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "No se encontró el modelo entrenado. Primero ejecuta: python src/train.py"
        )
    return joblib.load(MODEL_PATH)


def predecir_intencion(modelo, texto: str):
    probabilidades = modelo.predict_proba([texto])[0]
    clases = modelo.classes_

    mejor_indice = probabilidades.argmax()
    intent = clases[mejor_indice]
    confianza = float(probabilidades[mejor_indice])

    ranking = sorted(
        zip(clases, probabilidades),
        key=lambda item: item[1],
        reverse=True,
    )

    return intent, confianza, ranking


def obtener_respuesta(intent: str, confianza: float, entidades: dict):
   

    respuesta = RESPUESTAS.get(intent, RESPUESTAS["fallback"])

    if isinstance(respuesta, list):
        return random.choice(respuesta)

    return respuesta


def obtener_respuesta_funcional(
    intent: str,
    confianza: float,
    entidades: dict,
):

    print(">>> Dentro de obtener_respuesta_funcional")
    print(f"Intent recibido: {intent}")

    if confianza < UMBRAL_CONFIANZA:
        return random.choice(RESPUESTAS["fallback"])

    if intent == "consultar_info_libro":

     if entidades.get("titulo"):

        return obtener_info_libro(entidades["titulo"])

     return "¿Sobre qué libro te gustaría obtener información?"
   
    if intent == "consultar_precio":

        print(">>> Entré al bloque consultar_precio")
        print(f"Entidades: {entidades}")

        if entidades.get("titulo"):

            print(f"Título detectado: {entidades['titulo']}")

            libro = buscar_por_titulo(entidades["titulo"])

            print(f"Resultado de buscar_por_titulo: {libro}")

            if libro:

                titulo, autor, categoria, precio, stock = libro

                return (
                    f"El precio de '{titulo}' es "
                    f"${precio:.2f}."
                )

            return "No encontré ese libro en el catálogo."

        return (
            "¿De qué libro te gustaría conocer el precio?"
        )

    elif intent == "buscar_por_autor":

        if entidades.get("autor"):

            libros = buscar_por_autor(entidades["autor"])

            if libros:

                lista = "\n".join(
                    f"- {titulo}"
                    for titulo, autor in libros
                )

                return (
                    f"Encontré estos libros de "
                    f"{entidades['autor']}:\n{lista}"
                )

            return "No encontré libros de ese autor."

    elif intent == "info_titulos":
        # Si el usuario pidió libros de un autor
        if entidades.get("autor"):

            libros = buscar_por_autor(entidades["autor"])

            if libros:

                lista = "\n".join(
                    f"- {titulo}"
                    for titulo, autor in libros
                )

                return (
                    f"Encontré estos libros de "
                    f"{entidades['autor']}:\n{lista}"
                )

            return "No encontré libros de ese autor."

        # Si pidió un título específico
        if entidades.get("titulo"):

            libro = buscar_por_titulo(entidades["titulo"])

            if libro:

                titulo, autor, categoria, precio, stock = libro

                return (
                    f"Título: {titulo}\n"
                    f"Autor: {autor}\n"
                    f"Categoría: {categoria}\n"
                    f"Precio: ${precio:.2f}\n"
                    f"Stock: {stock}"
                )

        # Si no especificó autor ni título
        libros = obtener_todos_los_libros()

        if not libros:
            return "Por el momento no hay títulos registrados."

        lista = "\n".join(
            f"- {titulo} ({autor})"
            for titulo, autor in libros
        )

        return (
            "Estos son algunos de nuestros títulos:\n"
            f"{lista}"
        )

    respuesta = RESPUESTAS.get(intent, RESPUESTAS["fallback"])

    if isinstance(respuesta, list):
        return random.choice(respuesta)

    return respuesta

def procesar_mensaje(texto, modelo):

    intent, confianza, ranking = predecir_intencion(modelo, texto)

    entidades = {}
    entidades_validas = {}

    if intent in INTENCIONES_SOCIALES:

        respuesta = obtener_respuesta(
            intent,
            confianza,
            {},
        )

    elif intent in INTENCIONES_FUNCIONALES:

        entidades = extraer_entidades(texto)

        entidades_validas = {
            clave: valor
            for clave, valor in entidades.items()
            if valor is not None
        }

        print(">>> Voy a llamar a obtener_respuesta_funcional")
        print(f"Intent: {intent}")
        print(f"Entidades: {entidades}")

        respuesta = obtener_respuesta_funcional(
            intent,
            confianza,
            entidades,
        )

    else:

        respuesta = random.choice(RESPUESTAS["fallback"])

    return {
        "respuesta": respuesta,
        "intent": intent,
        "confianza": confianza,
        "ranking": ranking,
        "entidades": entidades_validas,
    }


def main():
    modelo = cargar_modelo()

    print("Chatbot de librería listo.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        texto = input("Tú: ").strip()

        if not texto:
            print("Bot: Escribe un mensaje para poder ayudarte.\n")
            continue

        if texto.lower() in {"salir", "exit", "quit"}:
            print("Bot: Hasta luego.")
            break

        resultado = procesar_mensaje(texto, modelo)

        if resultado["entidades"]:
            print(f"Entidades extraídas: {resultado['entidades']}")

        print(f"Intención detectada: {resultado['intent']}")
        print(f"Confianza estimada: {resultado['confianza']:.2f}")

        print("Top 3 intenciones:")
        for etiqueta, probabilidad in resultado["ranking"][:3]:
            print(f"- {etiqueta}: {probabilidad:.2f}")

        print(f"Bot: {resultado['respuesta']}\n")


if __name__ == "__main__":
    main()
