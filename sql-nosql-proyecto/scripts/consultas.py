import sqlite3
from pymongo import MongoClient
import pandas as pd

# SQL
conn = sqlite3.connect("sql-nosql-proyecto/data/usuarios.db")
usuarios = pd.read_sql_query("""
SELECT u.id, u.nombre, u.correo, r.nombre AS rol
FROM usuarios u
JOIN roles r ON u.rol_id = r.id
""", conn)

# NoSQL
client = MongoClient("mongodb://localhost:27017/")
db = client["actividad_db"]
actividades = pd.DataFrame(list(db["actividades"].find()))

# Integración
actividades = actividades.merge(usuarios, left_on="usuario_id", right_on="id")
print(actividades[["id", "nombre", "rol", "accion", "fecha", "detalles"]])
