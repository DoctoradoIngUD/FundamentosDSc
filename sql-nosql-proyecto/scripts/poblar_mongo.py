from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["actividad_db"]
actividades = db["actividades"]

actividades.insert_many([
    {"usuario_id": 1, "accion": "login", "fecha": datetime.now(), "detalles": {"ip": "192.168.0.1"}},
    {"usuario_id": 2, "accion": "editar", "fecha": datetime.now(), "detalles": {"modulo": "artículos"}},
    {"usuario_id": 3, "accion": "leer", "fecha": datetime.now(), "detalles": {"seccion": "noticias"}}
])
