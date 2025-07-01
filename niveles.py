import json
from constantes import *
# Este archivo contiene la lógica para cargar los niveles del juego desde un archivo JSON.
# La función `cargar_niveles` lee el archivo `niveles.json` y devuelve una lista de niveles.

def cargar_niveles():
    with open(ARCHIVO_NIVELES, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["niveles"]