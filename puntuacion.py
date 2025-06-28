from constantes import *

def guardar_puntaje(nombre, puntaje):
    with open(ARCHIVO_PUNTAJES, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{puntaje}\n")

def obtener_top10():
    puntajes = []
    try:
        with open(ARCHIVO_PUNTAJES, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes)==2:
                    nombre, valor = partes
                    puntajes.append((nombre, int(valor)))
        puntajes.sort(key=lambda x: x[1], reverse=True)
    except FileNotFoundError:
        pass
    return puntajes[:10]