import pygame
from niveles import cargar_niveles
from puntuacion import guardar_puntaje
from constantes import *
import ui

def jugar(pantalla):
    niveles = cargar_niveles()
    fuente = pygame.font.Font(FUENTE, 36)
    fuente_palabra = pygame.font.Font(FUENTE, 46)
    clock = pygame.time.Clock()
    puntaje_total = 0
    for n, nivel in enumerate(niveles):
        palabras = nivel["palabras"]
        pistas = nivel["pistas"]
        completadas = [False]*len(palabras)
        letras_usuario = ["" for _ in palabras]
        palabra_seleccionada = None
        jugando_nivel = True

        while jugando_nivel:
            pantalla.blit(ui.assets["fondo"], (0,0))
            # Título de nivel
            t = fuente.render(f"Nivel {n+1}/3", True, COLOR_TEXTO)
            pantalla.blit(t, (390, 30))
            # Puntos
            pantalla.blit(fuente.render(f"Puntos: {puntaje_total}", True, COLOR_TEXTO), (30, 30))
            # Dibuja palabras en horizontal
            cuadros = []
            for i, palabra in enumerate(palabras):
                y = 120 + i*80
                x = (ANCHO_VENTANA - len(palabra)*70) // 2
                for j, letra in enumerate(palabra):
                    rect = pygame.Rect(x + j*70, y, 60, 60)
                    color = COLOR_CUADRO_COMPLETADO if completadas[i] else COLOR_CUADRO
                    pygame.draw.rect(pantalla, color, rect)
                    pygame.draw.rect(pantalla, (0,0,0), rect, 2)
                    letra_a_mostrar = letras_usuario[i][j] if j < len(letras_usuario[i]) else ""
                    txt = fuente_palabra.render(letra_a_mostrar.upper(), True, COLOR_TEXTO)
                    pantalla.blit(txt, (x + j*70 + 15, y+10))
                    if j==0:  # Solo un cuadro por palabra para clickear pista
                        cuadros.append((rect, i))
            # Dibuja palabra vertical oculta
            palabra_vertical = ""
            for palabra in letras_usuario:
                if len(palabra)>1:
                    palabra_vertical += palabra[1].upper()
                else:
                    palabra_vertical += "_"
            t_vertical = fuente.render("Palabra oculta: " + " ".join(palabra_vertical), True, COLOR_SELECCION)
            pantalla.blit(t_vertical, (150, 540))

            # Si hay seleccionada, muestra la pista
            if palabra_seleccionada is not None:
                pista = pistas[palabra_seleccionada]
                pygame.draw.rect(pantalla, (60,60,120), (60, 630, 780, 50))
                t_pista = fuente.render("Pista: " + pista, True, COLOR_SELECCION)
                pantalla.blit(t_pista, (80, 640))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button==1:
                    x, y = evento.pos
                    for rect, i in cuadros:
                        if rect.collidepoint(x, y):
                            palabra_seleccionada = i
                            ui.assets["sonido_click"].play()
                elif evento.type == pygame.KEYDOWN and palabra_seleccionada is not None and not completadas[palabra_seleccionada]:
                    if evento.key == pygame.K_BACKSPACE:
                        letras_usuario[palabra_seleccionada] = letras_usuario[palabra_seleccionada][:-1]
                    elif len(letras_usuario[palabra_seleccionada]) < len(palabras[palabra_seleccionada]):
                        letra = evento.unicode.upper()
                        if letra.isalpha():
                            letras_usuario[palabra_seleccionada] += letra
                    # Validar
                    if len(letras_usuario[palabra_seleccionada]) == len(palabras[palabra_seleccionada]):
                        if letras_usuario[palabra_seleccionada].upper() == palabras[palabra_seleccionada].upper():
                            completadas[palabra_seleccionada]=True
                            puntaje_total += 10
                            palabra_seleccionada = None
                        else:
                            letras_usuario[palabra_seleccionada] = ""
                            puntaje_total = max(0, puntaje_total - 5)
                            ui.mostrar_popup(pantalla, "¡Incorrecto! Intenta de nuevo.")

            if all(completadas):
                jugando_nivel = False
            clock.tick(30)

    # Palabra oculta final
    palabra_vertical = "".join([p[1].upper() if len(p)>1 else "_" for p in letras_usuario])
    nombre = ui.pedir_nombre(pantalla)
    guardar_puntaje(nombre, puntaje_total)
    ui.mostrar_popup(pantalla, f"Puntaje final: {puntaje_total}\nPalabra oculta: {palabra_vertical}")