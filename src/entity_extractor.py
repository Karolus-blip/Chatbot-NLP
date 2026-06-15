from database import obtener_todos_los_libros


def extraer_entidades(texto):

    texto = texto.lower()

    entidades = {
        "titulo": None,
        "autor": None,
    }

    libros = obtener_todos_los_libros()

    for titulo, autor in libros:

        # Buscar título completo
        if titulo.lower() in texto:
            entidades["titulo"] = titulo

        # Buscar autor completo
        if autor.lower() in texto:
            entidades["autor"] = autor
            continue

        # Buscar por cada palabra significativa del autor
        for palabra in autor.lower().split():

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