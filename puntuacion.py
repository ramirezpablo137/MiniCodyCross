from constantes import *

def guardar_puntaje(nombre, puntaje):
    archivo = open(ARCHIVO_PUNTAJES, "a", encoding="utf-8")
    archivo.write(nombre + "," + str(puntaje) + "\n")
    archivo.close()

def obtener_top10():
    puntajes = []
    archivo = open(ARCHIVO_PUNTAJES, "r", encoding="utf-8")
    for linea in archivo:
        partes = linea.strip().split(",")
        if len(partes) == 2:
            nombre = partes[0]
            valor = partes[1]
            es_numero = True
            for caracter in valor:
                if caracter < "0" or caracter > "9":
                    es_numero = False
            if es_numero:
                puntajes.append([nombre, int(valor)])
    archivo.close()
    # Bubble sort de mayor a menor
    n = len(puntajes)
    for i in range(n-1):
        for j in range(n-1-i):
            if puntajes[j][1] < puntajes[j+1][1]:
                aux = puntajes[j]
                puntajes[j] = puntajes[j+1]
                puntajes[j+1] = aux
    return puntajes[:10]