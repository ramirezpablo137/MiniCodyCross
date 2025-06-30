import pygame
from niveles import cargar_niveles
from puntuacion import guardar_puntaje
from constantes import *
import ui

def a_mayuscula(letra):
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for i in range(len(minusculas)):
        if letra == minusculas[i]:
            return mayusculas[i]
    return letra

def comparar_palabras(p1, p2):
    if len(p1) != len(p2):
        return False
    for i in range(len(p1)):
        l1 = a_mayuscula(p1[i])
        l2 = a_mayuscula(p2[i])
        if l1 != l2:
            return False
    return True

def obtener_palabra_vertical(letras_usuario):
    palabra_vertical = ""
    for palabra in letras_usuario:
        if len(palabra) > 2:
            letra = palabra[2]
            letra = a_mayuscula(letra)
            palabra_vertical += letra
        else:
            palabra_vertical += "_"
    return palabra_vertical

def jugar(pantalla):
    niveles = cargar_niveles()
    fuente = pygame.font.Font(FUENTE, 36)
    fuente_palabra = pygame.font.Font(FUENTE, 46)
    clock = pygame.time.Clock()
    puntaje_total = 0
    palabras_ocultas = []  # Para mostrar todas al final
    for n in range(len(niveles)):
        nivel = niveles[n]
        palabras = nivel["palabras"]
        pistas = nivel["pistas"]
        completadas = [False] * len(palabras)
        letras_usuario = ["" for _ in palabras]
        palabra_seleccionada = None
        jugando_nivel = True

        while jugando_nivel:
            pantalla.blit(ui.assets["fondo"], (0,0))
            t = fuente.render("Nivel " + str(n+1) + "/3", True, COLOR_TEXTO)
            pantalla.blit(t, (390, 30))
            pantalla.blit(fuente.render("Puntos: " + str(puntaje_total), True, COLOR_TEXTO), (30, 30))
            cuadros = []
            for i in range(len(palabras)):
                palabra = palabras[i]
                y = 120 + i*80
                x = (ANCHO_VENTANA - len(palabra)*70) // 2
                for j in range(len(palabra)):
                    rect = pygame.Rect(x + j*70, y, 60, 60)
                    color = COLOR_CUADRO_COMPLETADO if completadas[i] else COLOR_CUADRO
                    pygame.draw.rect(pantalla, color, rect)
                    pygame.draw.rect(pantalla, (0,0,0), rect, 2)
                    letra_a_mostrar = ""
                    if j < len(letras_usuario[i]):
                        letra_a_mostrar = letras_usuario[i][j]
                    txt = fuente_palabra.render(letra_a_mostrar, True, COLOR_TEXTO)
                    pantalla.blit(txt, (x + j*70 + 15, y+10))
                    if j == 0:
                        cuadros.append([rect, i])
            # Palabra vertical oculta (tercera letra)
            palabra_vertical = obtener_palabra_vertical(letras_usuario)
            t_vertical = fuente.render("Palabra oculta: ", True, COLOR_SELECCION)
            pantalla.blit(t_vertical, (150, 540))
            for idx in range(len(palabra_vertical)):
                letra = palabra_vertical[idx]
                letra_txt = fuente.render(letra, True, COLOR_SELECCION)
                pantalla.blit(letra_txt, (400 + idx*40, 540))

            if palabra_seleccionada is not None:
                pista = pistas[palabra_seleccionada]
                pygame.draw.rect(pantalla, (60,60,120), (60, 630, 780, 50))
                t_pista = fuente.render("Pista: " + pista, True, COLOR_SELECCION)
                pantalla.blit(t_pista, (80, 640))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    x, y = evento.pos
                    for k in range(len(cuadros)):
                        rect = cuadros[k][0]
                        i = cuadros[k][1]
                        if rect.collidepoint(x, y):
                            palabra_seleccionada = i
                            ui.assets["sonido_click"].play()
                elif evento.type == pygame.KEYDOWN and palabra_seleccionada is not None and not completadas[palabra_seleccionada]:
                    if evento.key == pygame.K_BACKSPACE:
                        letras_usuario[palabra_seleccionada] = letras_usuario[palabra_seleccionada][:-1]
                    elif len(letras_usuario[palabra_seleccionada]) < len(palabras[palabra_seleccionada]):
                        letra = evento.unicode
                        if ("a" <= letra <= "z") or ("A" <= letra <= "Z") or (letra in "ñÑ"):
                            letra = a_mayuscula(letra)
                            letras_usuario[palabra_seleccionada] += letra
                    # Validar
                    pal1 = letras_usuario[palabra_seleccionada]
                    pal2 = palabras[palabra_seleccionada]
                    if len(pal1) == len(pal2):
                        if comparar_palabras(pal1, pal2):
                            completadas[palabra_seleccionada] = True
                            puntaje_total += 10
                            palabra_seleccionada = None
                        else:
                            letras_usuario[palabra_seleccionada] = ""
                            puntaje_total = max(0, puntaje_total - 5)
                            ui.mostrar_popup(pantalla, "¡Incorrecto! Intenta de nuevo.")
            if all(completadas):
                jugando_nivel = False
            clock.tick(30)
        # Palabra vertical del nivel listo para mostrar al final
        palabra_vertical = obtener_palabra_vertical(letras_usuario)
        palabras_ocultas.append(palabra_vertical)
        # Si querés mostrarla después de cada nivel, descomentá:
        # ui.mostrar_popup(pantalla, "Palabra oculta: " + palabra_vertical)

    # Ahora sí, después de los 3 niveles, pedir el nombre y mostrar el puntaje y palabras ocultas.
    nombre = ui.pedir_nombre(pantalla)
    guardar_puntaje(nombre, puntaje_total)
    mensaje = "Puntaje final: " + str(puntaje_total)
    for i, oculta in enumerate(palabras_ocultas):
        mensaje += "\nNivel " + str(i+1) + ": " + oculta
    ui.mostrar_popup(pantalla, mensaje)