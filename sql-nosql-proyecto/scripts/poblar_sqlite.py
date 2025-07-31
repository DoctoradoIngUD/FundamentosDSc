import sqlite3

conn = sqlite3.connect("sql-nosql-proyecto/data/usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    rol_id INTEGER,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
)
""")

cursor.executemany("INSERT INTO roles (id, nombre) VALUES (?, ?)", [
    (1, "admin"),
    (2, "editor"),
    (3, "lector")
])

cursor.executemany("INSERT INTO usuarios (id, nombre, correo, rol_id) VALUES (?, ?, ?, ?)", [
    (1, "Ana", "ana@example.com", 1),
    (2, "Luis", "luis@example.com", 2),
    (3, "Marta", "marta@example.com", 3)
])

conn.commit()
conn.close()
