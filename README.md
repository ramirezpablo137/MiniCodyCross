# Mini CodyCross

## Descripción

**Mini CodyCross** es un juego de crucigramas digital desarrollado en Python, inspirado en el clásico juego CodyCross. El objetivo es completar palabras horizontales a partir de pistas y, como desafío adicional, descubrir una palabra oculta formada por la tercera letra de cada palabra horizontal. El juego incluye un menú principal, estadísticas de los mejores puntajes, créditos, tres niveles y persistencia de puntajes. Se desarrolló como proyecto final para la materia **Programación I**.

---

## Características

- **Interfaz gráfica** desarrollada con [Pygame](https://www.pygame.org/).
- **3 niveles** con palabras y pistas únicas.
- **Palabra vertical oculta** como desafío extra en cada nivel.
- **Menú principal** interactivo con opciones de Jugar, Estadísticas, Créditos y Salir.
- **Pantalla de créditos** y **pantalla de estadísticas** (top 10 mejores puntajes).
- **Sistema de puntaje:** +10 por palabra acertada, -5 por error.
- **Persistencia de datos:** niveles y pistas cargados desde `niveles.json`; puntajes guardados en `puntajes.txt`.
- **Modularización:** código organizado en módulos para facilitar el mantenimiento y la ampliación.

---

## Estructura del Proyecto

```
MiniCodyCross/
│
├── main.py                # Archivo principal, gestiona el flujo general y el menú.
├── juego.py               # Lógica y renderizado del juego.
├── ui.py                  # Interfaz de usuario: menús, créditos, estadísticas.
├── niveles.py             # Carga y gestión de los niveles desde JSON.
├── puntuacion.py          # Manejo y ordenamiento de puntajes.
├── constantes.py          # Colores, rutas y parámetros globales.
│
├── niveles.json           # Archivo de niveles y pistas.
├── puntajes.txt           # Archivo de puntajes guardados.
│
└── assets/                # Carpeta con imágenes y sonidos.
    ├── fondo.png
    ├── btn_jugar.png
    ├── btn_estadisticas.png
    ├── btn_creditos.png
    ├── btn_salir.png
    └── click.wav
```

---

## Instalación

1. **Clonar el repositorio**

   ```sh
   git clone https://github.com/ramirezpablo137/MiniCodyCross.git
   cd MiniCodyCross
   ```

2. **Instalar dependencias**

   Es necesario tener Python 3.x y [Pygame](https://www.pygame.org/) instalado.

   ```sh
   pip install requirements.txt
   ```

3. **Verificar recursos**

   Asegúrate de que la carpeta `assets/` tenga todas las imágenes y sonidos requeridos y que los archivos `niveles.json` y `puntajes.txt` existan en el directorio raíz.

---

## Ejecución

Para ejecutar el juego, simplemente corre:

```sh
python main.py
```

---

## Instrucciones de Juego

1. **Menú Principal:**  
   Selecciona "Jugar" para comenzar, "Estadísticas" para ver el top 10, "Créditos" para información del proyecto o "Salir".

2. **Durante el Juego:**  
   - Haz click en la palabra que deseas completar.
   - Escribe letra por letra utilizando el teclado.
   - Presiona Enter para validar la palabra; si es correcta, se marca en verde.
   - Si te equivocas puedes reintentar, pero perderás puntos.
   - Completa todas las palabras para revelar la palabra vertical oculta (formada por la tercera letra de cada palabra horizontal).

3. **Al finalizar:**  
   Ingresa tu nombre para guardar tu puntaje en el ranking.

---

## Formato de archivos

### niveles.json

```json
{
  "niveles": [
    {
      "palabras": ["CAMINO", "ANDAR", "RUTA"],
      "pistas": [
        "Lugar por donde se puede andar o viajar.",
        "Acción de desplazarse a pie.",
        "Vía por la que circulan vehículos."
      ]
    },
    // ...otros niveles
  ]
}
```

### puntajes.txt

Archivo plano donde cada línea tiene el formato:

```
nombre,puntaje
```
Ejemplo:
```
Juan,120
Ana,105
```

---

## Créditos

- **Autores:** Matias Roig y Pablo Ramirez
- **Materia:** Programación I – Tecnicatura Universitaria en Programación
- **Docente:** Martin Alejandro Garcia
- **Año:** 2025

---

## Licencia

Este proyecto es educativo y de código abierto. Puedes modificarlo y distribuirlo citando a los autores originales.

---

## Notas Técnicas

- Se recomienda ejecutar el juego en sistemas donde la fuente `arial.ttf` esté disponible o cambiar la fuente en `constantes.py`.
- Los recursos gráficos deben estar en la carpeta `assets/` y las rutas deben coincidir con las definidas en `constantes.py`.
- El código está completamente modularizado para facilitar mantenimiento y ampliaciones futuras.

---

## ¿Cómo contribuir?

1. Haz un fork del repositorio.
2. Realiza tus cambios o mejoras en una rama nueva.
3. Abre un Pull Request con una descripción clara de tu aporte.

---

¡Esperamos que disfrutes Mini CodyCross!
