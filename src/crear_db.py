import sqlite3

conexion = sqlite3.connect("data/libreria.db")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    categoria TEXT,
    precio REAL,
    stock INTEGER
)
""")

# Insertar algunos libros
libros = [
    ("La Ilíada", "Homero", "Clásicos", 320.0, 8),
    ("La Odisea", "Homero", "Clásicos", 300.0, 10),
    ("El ingenioso hidalgo Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 450.0, 5),
    ("Rayuela", "Julio Cortázar", "Novela", 390.0, 7)
]

cursor.executemany("""
INSERT INTO libros (titulo, autor, categoria, precio, stock)
VALUES (?, ?, ?, ?, ?)
""", libros)

conexion.commit()
conexion.close()

print("Base de datos creada y libros agregados.")

