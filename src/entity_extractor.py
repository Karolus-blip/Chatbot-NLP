from database import obtener_todos_los_libros

import unicodedata


PALABRAS_IGNORADAS = {
    "el",
    "la",
    "los",
    "las",
    "de",
    "del",
    "y",
    "en",
    "un",
    "una"
}


def normalizar_texto(texto):

    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        c
        for c in texto
        if unicodedata.category(c) != "Mn"
    )

    return texto


def coincide(texto, valor):

    texto = normalizar_texto(texto)
    valor = normalizar_texto(valor)

    # Coincidencia completa
    if valor in texto:
        return True

    palabras = valor.split()

    coincidencias = 0

    for palabra in palabras:

        if palabra in PALABRAS_IGNORADAS:
            continue

        if len(palabra) <= 2:
            continue

        if palabra in texto:
            coincidencias += 1

    # Debe coincidir al menos una palabra significativa
    return coincidencias > 0


def extraer_entidades(texto):

    texto = normalizar_texto(texto)

    entidades = {
        "titulo": None,
        "autor": None,
    }

    libros = obtener_todos_los_libros()

    mejor_titulo = None
    mejor_puntaje = 0

    for titulo, autor in libros:

        titulo_normalizado = normalizar_texto(titulo)

        puntaje = 0

        for palabra in titulo_normalizado.split():

            if palabra in PALABRAS_IGNORADAS:
                continue

            if len(palabra) <= 2:
                continue

            if palabra in texto:
                puntaje += 1

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_titulo = titulo

        if coincide(texto, autor):
            entidades["autor"] = autor

    entidades["titulo"] = mejor_titulo

    return entidades