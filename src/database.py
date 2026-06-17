import sqlite3

RUTA_DB = "data/libreria.db"

def obtener_precio_por_titulo(titulo):

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT precio
        FROM libros
        WHERE LOWER(titulo) LIKE LOWER(?)
    """, (f"%{titulo}%",))

    resultado = cursor.fetchone()

    conexion.close()

    return resultado

def buscar_por_autor(autor):

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, autor
        FROM libros
        WHERE LOWER(autor) LIKE LOWER(?)
    """, (f"%{autor}%",))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados

def buscar_por_titulo(titulo):

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, autor, categoria, precio, stock
        FROM libros
        WHERE LOWER(titulo) LIKE LOWER(?)
    """, (f"%{titulo}%",))

    resultado = cursor.fetchone()

    conexion.close()

    return resultado

def buscar_por_categoria(categoria):

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, autor
        FROM libros
        WHERE LOWER(categoria) LIKE LOWER(?)
    """, (f"%{categoria}%",))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


def obtener_todos_los_libros():
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, autor
        FROM libros
    """)

    resultados = cursor.fetchall()

    conexion.close()

    return resultados