# Chatbot NLP para Librería

Asistente conversacional desarrollado en Python para la consulta de un catálogo de libros mediante lenguaje natural.

Este proyecto utiliza técnicas clásicas de Procesamiento de Lenguaje Natural (NLP) para interpretar consultas de los usuarios, identificar intenciones, extraer entidades relevantes y recuperar información desde una base de datos.

Más que un chatbot aislado, este repositorio documenta una evolución progresiva desde sistemas basados en reglas hacia arquitecturas conversacionales apoyadas en aprendizaje automático y procesamiento lingüístico.

---

## Objetivos del proyecto

El proyecto nació como una continuación de un chatbot construido exclusivamente mediante reglas condicionales en Python.

La primera versión respondía a partir de estructuras `if/else` y coincidencias explícitas de texto. En esta nueva etapa, el chatbot es capaz de generalizar a partir de ejemplos de entrenamiento, identificar patrones lingüísticos y recuperar información de forma dinámica.

El objetivo principal es comprender los fundamentos técnicos de los sistemas conversacionales modernos mediante la implementación práctica de componentes de NLP.

---

## Características

* Clasificación de intenciones mediante TF-IDF y scikit-learn.
* Extracción de entidades (autores y títulos).
* Consultas dinámicas a una base de datos SQLite.
* Memoria conversacional básica entre turnos.
* Separación entre frontend y backend.
* Interfaz web conversacional desarrollada con Streamlit.
* Arquitectura modular y extensible.

---

## Tecnologías utilizadas

* Python
* scikit-learn
* Streamlit
* SQLite
* Joblib
* Pandas

---

## Arquitectura general

Usuario

↓

Interfaz Streamlit

↓

Clasificación de intención

↓

Extracción de entidades

↓

Memoria conversacional

↓

Consulta a base de datos SQLite

↓

Respuesta dinámica

---

## Ejemplo de funcionamiento

### Consulta de libros por autor

Usuario:

> ¿Qué libros tienen de Homero?

Proceso interno:

1. Clasificación de intención

```text
info_titulos
```

2. Extracción de entidades

```text
autor = Homero
```

3. Consulta a la base de datos

```sql
SELECT titulo
FROM libros
WHERE autor = 'Homero';
```

4. Respuesta generada

```text
Encontré estos libros de Homero:

- Ilíada
- Odisea
```

---

## Estado actual

Actualmente el sistema es capaz de:

* Identificar la intención principal de una consulta.
* Detectar autores y títulos mencionados por el usuario.
* Recuperar información desde una base de datos SQLite.
* Mantener contexto básico entre preguntas consecutivas.
* Mostrar información de depuración NLP mediante una interfaz web.
* Gestionar consultas funcionales y sociales.

---

## Estructura del proyecto

```text
chatbot-nlp-libreria/
│
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
│   ├── memoria.py
│   ├── responses.py
│   ├── train.py
│   ├── visualize_vectors.py
│   └── webapp.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Karolus-blip/chatbot-nlp-libreria.git
```

Entrar al directorio del proyecto:

```bash
cd chatbot-nlp-libreria
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Entrenar el modelo:

```bash
python src/train.py
```

Ejecutar el chatbot desde consola:

```bash
python src/chatbot.py
```

Ejecutar la interfaz web:

```bash
streamlit run src/webapp.py
```

---

## Próximas mejoras

* Incorporar nuevas entidades (editorial, género, ISBN).
* Mejorar la gestión de contexto conversacional.
* Implementar búsqueda semántica mediante embeddings.
* Añadir recomendaciones de libros.
* Exponer funcionalidades mediante una API REST.
* Desplegar la aplicación en la nube.

---

## Aprendizajes

Este proyecto ha servido como espacio de experimentación para comprender conceptos fundamentales de:

* Procesamiento de Lenguaje Natural.
* Clasificación de texto.
* Extracción de entidades.
* Diseño conversacional.
* Gestión de contexto.
* Integración entre NLP y bases de datos.

Más que un producto terminado, este repositorio representa una etapa dentro de un proceso continuo de aprendizaje y desarrollo en sistemas conversacionales.
