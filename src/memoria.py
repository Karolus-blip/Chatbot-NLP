import sqlite3
import json

DB = "data/conversaciones.db"


def guardar_conversacion(
    mensaje_usuario,
    respuesta_bot,
    intencion,
    confianza,
    entidades,
):

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO conversaciones (
            mensaje_usuario,
            respuesta_bot,
            intencion,
            confianza,
            entidades
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            mensaje_usuario,
            respuesta_bot,
            intencion,
            confianza,
            json.dumps(entidades, ensure_ascii=False),
        ),
    )

    conexion.commit()
    conexion.close()


def obtener_ultimas_conversaciones(limite=5):
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            mensaje_usuario,
            respuesta_bot,
            intencion,
            entidades,
            fecha
        FROM conversaciones
        ORDER BY id DESC
        LIMIT ?
        """,
        (limite,),
    )

    conversaciones = cursor.fetchall()

    conexion.close()

    return list(reversed(conversaciones))

def buscar_ultima_entidad(tipo="titulo", limite=10):

    conversaciones = obtener_ultimas_conversaciones(limite)

    for _, _, _, entidades_json, _ in reversed(conversaciones):
        print ("JSON encontrado:", entidades_json)
        if not entidades_json:
            continue

        entidades = json.loads(entidades_json)
        print("Entidades cargadas:", entidades)

        if entidades.get(tipo):
            print("Entidad encontrada:", entidades[tipo])
            return entidades[tipo]

    return None

if __name__ == "__main__":

    print(obtener_ultimas_conversaciones())

    print(
        "Último título:",
        buscar_ultima_entidad("titulo")
    )

def obtener_ultima_intencion():

    conversaciones = obtener_ultimas_conversaciones(1)

    if not conversaciones:
        return None

    _, _, intencion, _, _ = conversaciones[-1]

    return intencion

if __name__ == "__main__":

    print("Últimas conversaciones:")
    print(obtener_ultimas_conversaciones())

    print("\nÚltima intención:")
    print(obtener_ultima_intencion())