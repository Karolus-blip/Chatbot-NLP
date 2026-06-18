import sqlite3
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_DB = BASE_DIR / "data" / "libreria.db"
RUTA_CATALOGO = BASE_DIR / "data" / "catalogo.csv"

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    categoria TEXT,
    precio REAL,
    stock INTEGER,
    descripcion TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM libros")
cantidad = cursor.fetchone()[0]

with open(RUTA_CATALOGO, encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    libros = []
    for fila in lector:
        libros.append(
            (
                fila["titulo"],
                fila["autor"],
                fila["categoria"],
                float(fila["precio"]),
                int(fila["stock"]),
                fila["descripcion"]
            )
        )

if cantidad == 0:

    cursor.executemany("""
    INSERT INTO libros (titulo, autor, categoria, precio, stock, descripcion)
    VALUES (?, ?, ?, ?, ?, ?)
    """, libros)

    print("Libros agregados correctamente.")

else:

    print("La base de datos ya contiene libros. No se agregaron nuevos registros.")

conexion.commit()
conexion.close()



