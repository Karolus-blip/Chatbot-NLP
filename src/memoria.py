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