from constantes import *

 
# Este archivo contiene la lógica para guardar y obtener puntajes del juego.
# La función `guardar_puntaje` guarda el nombre del jugador y su puntaje en un archivo de texto.
# La función `obtener_top10` lee el archivo de puntajes y devuelve una lista con los 10 mejores puntajes.
# # Se utiliza un formato simple de "nombre,puntaje" para cada línea del archivo.
## El archivo de puntajes se guarda en `puntajes.txt` y se utiliza para mostrar las estadísticas del juego.


def guardar_puntaje(nombre, puntaje):
    archivo = open(ARCHIVO_PUNTAJES, "a", encoding="utf-8")
    archivo.write(nombre + "," + str(puntaje) + "\n")
    archivo.close()

def obtener_top10():
    puntajes = []
    archivo = open(ARCHIVO_PUNTAJES, "r", encoding="utf-8")
    for linea in archivo:
        # Eliminar el salto de línea manualmente si está al final
        if len(linea) > 0 and linea[-1] == "\n":
            linea = linea[:-1]
        # Buscar la coma manualmente
        coma = -1
        for i in range(len(linea)):
            if linea[i] == ",":
                coma = i
                break
        if coma != -1:
            nombre = linea[:coma]
            valor = linea[coma+1:]
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