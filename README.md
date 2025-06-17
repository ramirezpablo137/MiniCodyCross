# Mini CodyCross

Juego educativo tipo crucigrama, desarrollado en Python con Pygame.

---

## 📁 Estructura del Proyecto

- `main.py` — punto de entrada, ciclo principal y navegación de menú.
- `ui.py` — interfaz de usuario (menús, créditos, estadísticas).
- `juego.py` — lógica central del juego.
- `niveles.py` — carga de niveles desde JSON.
- `puntuacion.py` — manejo de puntajes y estadísticas.
- `niveles.json` — niveles y palabras con pistas.
- `puntajes.txt` — archivo para los puntajes.
- `requirements.txt` — dependencias (por ahora: pygame).
- `assets/` — imágenes y sonidos.

---

## 🚦 Bitácora de desarrollo (actualizá con cada avance)

- **[2025-06-17]**
  - Estructura modular creada.
  - `requirements.txt` con pygame.
  - `niveles.json` con tres niveles de ejemplo y formato acordado.
  - Función en `niveles.py` para leer niveles desde JSON.
- **[PRÓXIMO AVANCE]**
  - Modularización de menú principal en `ui.py`.
  - Integración del ciclo principal en `main.py`.
  - Desarrollo inicial de la lógica de juego en `juego.py`.

---

## 🧩 ¿Cómo se cargan los niveles?

- El archivo `niveles.json` contiene una lista de niveles.  
  Cada nivel tiene una lista de palabras y pistas, así:

```json
[
  {
    "nivel": 1,
    "palabras": [
      {"palabra": "PERRO", "pista": "Animal que ladra"},
      {"palabra": "GATO", "pista": "Animal que maúlla"}
      // ...
    ]
  }
  // más niveles
]
```

- Para cargar los niveles, usamos la función en `niveles.py`:

```python
import json

def cargar_niveles(archivo='niveles.json'):
    with open(archivo, encoding='utf-8') as f:
        return json.load(f)
```



## 📝 ¿Cómo actualizar este README?

Cada vez que avances:
1. Agregá una entrada en la bitácora con la fecha y el detalle.
2. Marcá en la lista de próximos pasos lo que terminaste.
3. Si agregás un archivo o módulo, sumalo a la estructura del proyecto con una breve descripción.
4. Si cambiás el formato de un archivo (ej: el JSON de niveles), documentá el nuevo formato con un ejemplo.

---

## 📌 Próximos pasos (ir marcando)

- [x] Estructura modular creada
- [x] Archivo de dependencias
- [x] Primeros niveles y función de carga
- [ ] Menú principal funcional
- [ ] Modularización total de la interfaz
- [ ] Lógica de juego y validación de palabras
- [ ] Guardado y visualización de puntajes

---

## 👥 Autores

- Pablo Ramirez
- Matias Roig

---

## ✉️ Contacto

- Tecnicatura universitaria en programacion, Programacion I, 2025.
---

> **Consejo:**  
> Actualizá este README cada vez que avances o modifiques algo importante.  
> Es clave para la defensa y el trabajo en equipo.
