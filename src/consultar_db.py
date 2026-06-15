import sqlite3

conexion = sqlite3.connect("data/libreria.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM libros")

for libro in cursor.fetchall():
    print(libro)

conexion.close()