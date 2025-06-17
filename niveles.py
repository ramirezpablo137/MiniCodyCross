import json

def cargar_niveles(archivo='niveles.json'):
    with open(archivo, encoding='utf-8') as f:
        return json.load(f)