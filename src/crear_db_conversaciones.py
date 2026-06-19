import sqlite3

conexion = sqlite3.connect("data/conversaciones.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensaje_usuario TEXT NOT NULL,
    respuesta_bot TEXT NOT NULL,
    intencion TEXT,
    confianza REAL,
    entidades TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conexion.commit()
conexion.close()

print("Base de datos de conversaciones creada correctamente.")