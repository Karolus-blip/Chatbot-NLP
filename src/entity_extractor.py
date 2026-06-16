from database import obtener_todos_los_libros

import unicodedata


def extraer_entidades(texto):

    texto = normalizar_texto(texto)

    entidades = {
        "titulo": None,
        "autor": None,
    }

    libros = obtener_todos_los_libros()

    for titulo, autor in libros:

        # Buscar título completo
        if normalizar_texto(titulo) in texto:
            entidades["titulo"] = titulo

        # Buscar autor completo
        if normalizar_texto(autor) in texto:
            entidades["autor"] = autor
            continue

        # Buscar por cada palabra significativa del autor
        for palabra in normalizar_texto(autor).split():

            if len(palabra) <= 2:
                continue

            if palabra in texto:
                entidades["autor"] = autor
                break

    return entidades

def coincide(texto, valor):

    texto = texto.lower()
    valor = valor.lower()

    if valor in texto:
        return True

    for palabra in valor.split():

        if len(palabra) > 2 and palabra in texto:
            return True

    return False

def normalizar_texto(texto):

    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter 
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto