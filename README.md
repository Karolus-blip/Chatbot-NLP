# Chatbot NLP para Librería

Evolución de un chatbot basado en reglas hacia un chatbot con Procesamiento de Lenguaje Natural

Este proyecto representa la segunda etapa de un proceso de aprendizaje en el desarrollo de asistentes conversacionales.

La primera versión del chatbot (Chatbot-Intro) fue construida utilizando lógica condicional en Python, donde cada respuesta dependía de reglas definidas manualmente (if/else y coincidencias explícitas de texto).

En esta nueva versión, el enfoque cambia completamente: el chatbot utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para interpretar las consultas del usuario, clasificar su intención y extraer información relevante antes de generar una respuesta.

El objetivo del proyecto no es únicamente crear un chatbot funcional, sino explorar la transición desde un sistema basado en reglas hacia un sistema capaz de generalizar a partir de ejemplos de entrenamiento.

---

## Características

-Clasificación de intenciones mediante scikit-learn y TF-IDF.
-Extracción de entidades (título y autor).
-Consulta de una base de datos SQLite de libros.
-Respuestas diferenciadas para intenciones sociales y funcionales.
-Arquitectura modular que facilita la incorporación de nuevas funcionalidades.
-Interfaz de consola y preparación para interfaz web con Streamlit.

---

## ¿Qué NO hace este bot?

Para mantener el proyecto sencillo y didáctico:

- no usa modelos generativos ni LLMs
- no mantiene memoria de conversación
- no sigue flujos complejos
- no consulta bases de datos reales
- no procesa pagos ni pedidos de verdad

Es un ejercicio educativo para entender la lógica base de un chatbot clásico.

---

## Tecnologías utilizadas

Python 3
scikit-learn
pandas
SQLite
joblib
Streamlit

## ¿Cómo funciona?

Cuando una persona escribe algo como:

> “Quiero saber dónde va mi pedido”

el sistema hace esto:

### Paso A. Clasificar la intención

El modelo mira el texto y calcula cuál intención parece más probable.

Por ejemplo, podría producir algo así:

- rastrear_pedido: 0.81
- cancelar_pedido: 0.09
- nuevo_pedido: 0.05
- otras: menos probables

Después se queda con la más probable: `rastrear_pedido`.

### Paso B. Elegir una respuesta humana

Una vez que el sistema decidió la intención, busca una respuesta predefinida. Por ejemplo:

> “Con gusto te ayudo a rastrear tu pedido. Comparte tu número de pedido para revisarlo.”

Esa respuesta **no salió del modelo**. La escribió una persona.

---
## Estructura del proyecto

chatbot-nlp-librería/
│
├── .venv/
├── data/
├── models/
├── src/
│   ├── chatbot.py
│   ├── consultar_db.py
│   ├── crear_db.py
│   ├── database.py
│   ├── entity_extractor.py
│   ├── evaluate.py
│   ├── intent_categories.py
│   ├── probar_database.py
│   ├── responses.py
│   ├── train.py
│   ├── visualize_vectors.py
│   └── webapp.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## Instalación

Instalación

Clona el repositorio:

git clone https://github.com/Karolus-blip/chatbot-nlp-libreria.git

Instala las dependencias:

pip install -r requirements.txt

## Ejecución

Entrenar el modelo:

python src/train.py

Ejecutar el chatbot desde la terminal:

python src/chatbot.py

Ejecutar la interfaz web:

streamlit run src/webapp.py

## Próximas mejoras

-Ampliar el conjunto de intenciones y ejemplos de entrenamiento.
-Incorporar nuevas entidades (editorial, género, ISBN).
-Implementar contexto conversacional entre turnos.
-Integrar modelos basados en embeddings.
-Desplegar el chatbot mediante una API y una interfaz web.

## Reflexión

Más que un chatbot terminado, este repositorio documenta una evolución técnica: pasar de un asistente construido exclusivamente con reglas escritas a mano a un sistema que aprende patrones lingüísticos a partir de datos.

Ese cambio de paradigma ha permitido comprender mejor cómo funcionan los sistemas conversacionales modernos y sentar las bases para proyectos más complejos en NLP y diseño conversacional.
