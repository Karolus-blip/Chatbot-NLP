from database import obtener_info_completa


def obtener_info_libro(titulo):
    """
    Devuelve una respuesta conversacional con la información
    completa de un libro.
    """

    libro = obtener_info_completa(titulo)

    if libro is None:
        return "Lo siento, no encontré ese libro en el catálogo."

    titulo, autor, categoria, precio, stock, descripcion = libro

    respuesta = (
        f'"{titulo}", de {autor}, pertenece a la categoría {categoria}.\n\n'
        f'{descripcion}\n\n'
        f'Precio: ${precio:.2f}\n'
        f'Existencias: {stock}'
    )

    return respuesta


# -------------------------------------
# Bloque de pruebas
# -------------------------------------

if __name__ == "__main__":

    while True:

        titulo = input("\nEscribe el título del libro (o 'salir'): ")

        if titulo.lower() == "salir":
            break

        print()
        print(obtener_info_libro(titulo))