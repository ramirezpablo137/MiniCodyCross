import pygame
import sys
import ui
import juego
from constantes import *

# Este archivo es el punto de entrada del juego, donde se inicializa Pygame,
# se carga la música y se muestra el menú principal.


def main():
    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Mini CodyCross")
    ui.cargar_assets()
    pygame.mixer.music.load(RUTA_MUSICA)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while True:
        opcion = ui.menu_principal(pantalla)
        if opcion == "jugar":
            juego.jugar(pantalla)
        elif opcion == "estadisticas":
            ui.menu_estadisticas(pantalla)
        elif opcion == "creditos":
            ui.menu_creditos(pantalla)
        elif opcion == "salir":
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()