import pygame
from constantes import *

# Este archivo contiene la lógica de la interfaz de usuario del juego, incluyendo la carga de assets,
# la creación de botones, los menús principales, de estadísticas y créditos, y la interacción
# con el usuario a través de eventos de teclado y ratón.


assets = {}

def cargar_assets():
    global assets
    assets["fondo"] = pygame.image.load(RUTA_FONDO)
    assets["btn_jugar"] = pygame.image.load(RUTA_BTN_JUGAR)
    assets["btn_estadisticas"] = pygame.image.load(RUTA_BTN_ESTADISTICAS)
    assets["btn_creditos"] = pygame.image.load(RUTA_BTN_CREDITOS)
    assets["btn_salir"] = pygame.image.load(RUTA_BTN_SALIR)
    assets["sonido_click"] = pygame.mixer.Sound(RUTA_CLICK)

def boton_imagen(pantalla, img, pos):
    rect = img.get_rect(topleft=pos)
    pantalla.blit(img, pos)
    return rect

def menu_principal(pantalla):
    clock = pygame.time.Clock()
    while True:
        pantalla.blit(assets["fondo"], (0,0))
        btns = []
        btns.append(("jugar", boton_imagen(pantalla, assets["btn_jugar"], (350, 200))))
        btns.append(("estadisticas", boton_imagen(pantalla, assets["btn_estadisticas"], (350, 300))))
        btns.append(("creditos", boton_imagen(pantalla, assets["btn_creditos"], (350, 400))))
        btns.append(("salir", boton_imagen(pantalla, assets["btn_salir"], (350, 500))))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = evento.pos
                for nombre, rect in btns:
                    if rect.collidepoint(x, y):
                        assets["sonido_click"].play()
                        return nombre
        clock.tick(60)

def menu_creditos(pantalla):
    clock = pygame.time.Clock()
    fuente = pygame.font.Font(FUENTE, 32)
    pantalla.blit(assets["fondo"], (0,0))
    lineas = [
        "Mini CodyCross",
        "Desarrollado por: Matias roig y Pablo Ramirez",
        "Materia: Programación I - 1º Cuatrimestre",
        "Docente: Martin alejandro garcia",
        "Fecha: 30-06-2024",
        "División: 116",
        "Carrera: Tecnicatura universitaria en Programación",
        "",
        "Presiona cualquier tecla para volver..."
    ]
    for i, texto in enumerate(lineas):
        pantalla.blit(fuente.render(texto, True, COLOR_TEXTO), (100, 100 + i*40))
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN or evento.type == pygame.QUIT or (evento.type == pygame.MOUSEBUTTONDOWN):
                esperando = False
        clock.tick(30)

def menu_estadisticas(pantalla):
    from puntuacion import obtener_top10
    fuente = pygame.font.Font(FUENTE, 36)
    clock = pygame.time.Clock()
    pantalla.blit(assets["fondo"], (0,0))
    top = obtener_top10()
    pantalla.blit(fuente.render("Top 10 Mejores Puntajes", True, COLOR_TEXTO), (270, 100))
    for i, (nombre, puntaje) in enumerate(top):
        linea = f"{i+1}. {nombre} ........ {puntaje}"
        pantalla.blit(fuente.render(linea, True, COLOR_TEXTO), (260, 160 + i*40))
    pantalla.blit(fuente.render("Presiona cualquier tecla para volver...", True, COLOR_TEXTO), (160, 600))
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN or evento.type == pygame.QUIT or (evento.type == pygame.MOUSEBUTTONDOWN):
                esperando = False
        clock.tick(30)

def mostrar_popup(pantalla, mensaje):
    fuente = pygame.font.Font(FUENTE, 36)
    pygame.draw.rect(pantalla, (0,0,0), (200, 250, 500, 120))
    pygame.draw.rect(pantalla, (255,255,0), (200, 250, 500, 120), 4)
    texto = fuente.render(mensaje, True, (255,255,255))
    pantalla.blit(texto, (220, 290))
    pygame.display.flip()
    esperando = True
    clock = pygame.time.Clock()
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.QUIT:
                esperando = False
        clock.tick(30)

def pedir_nombre(pantalla):
    fuente = pygame.font.Font(FUENTE, 40)
    nombre = ""
    clock = pygame.time.Clock()
    activo = True
    while activo:
        pantalla.blit(assets["fondo"], (0,0))
        t1 = fuente.render("¡FELICITACIONES!", True, COLOR_TEXTO)
        t2 = fuente.render("Ingresa tu nombre para guardar el puntaje:", True, COLOR_TEXTO)
        pantalla.blit(t1, (250, 200))
        pantalla.blit(t2, (100, 260))
        pygame.draw.rect(pantalla, (255,255,255), (220, 340, 460, 60), 2)
        t_nombre = fuente.render(nombre, True, COLOR_SELECCION)
        pantalla.blit(t_nombre, (240, 350))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if len(nombre)>0:
                        return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre)<20 and evento.unicode.isalnum():
                        nombre += evento.unicode
            elif evento.type == pygame.QUIT:
                return "Jugador"
        clock.tick(30)
    return nombre if nombre else "Jugador"