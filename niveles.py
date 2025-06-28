import json
from constantes import *

def cargar_niveles():
    with open(ARCHIVO_NIVELES, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["niveles"]