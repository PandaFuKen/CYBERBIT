import pygame
import sys
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azulCielo = (12, 183, 242)
azul = (0, 0, 255)
amarillo = (255, 255, 0)
naranja = (255, 165, 0)
rosa = (255, 192, 203)
morado = (128, 0, 128)
cafe = (139, 69, 19)
gris = (128, 128, 128)

# Configuración del juego
ANCHO, ALTO = 800, 600
TAMANO_CELDA = 40
gravedad = 1
VelocidadJugador = 7
FUERZA_SALTO = -16  # Fuerza del salto

# Jugador
jugador_x, jugador_y = 90, 280
anchoJugador, alturaJugador = 30, 30
velocidad_y = 0
en_suelo = False

# Monedas
moneda = 0

#Vidas
vidas = 3

# Mapa del nivel
nivel = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 3, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Cargar imagen del jugador
Jugador_Imagen = pygame.image.load("CYBERBIT/Assets/images/Zorrito.png")
Jugador_Imagen = pygame.transform.scale(Jugador_Imagen, (anchoJugador, alturaJugador))  # Ajustar tamaño
# Cargar imagen de fondo
imagenFondo = pygame.image.load('CYBERBIT/Assets/images/Free-Pixel-Art-Cloud-and-Sky-Backgrounds5.jpg')
imagenFondo = pygame.transform.scale(imagenFondo, (ANCHO, ALTO))
#Imagen del portal
Portal = pygame.image.load('CYBERBIT/Assets/images/Portal1.png')
Portal = pygame.transform.scale(Portal, (50, 50))
#Imagen de la moneda
Moneda = pygame.image.load('CYBERBIT/Assets/images/Moneda.png')
Moneda = pygame.transform.scale(Moneda, (50, 50))
sonidoMoneda = pygame.mixer.Sound("CYBERBIT/Assets/sounds/Moneda.wav")
JuegoTerminado = pygame.mixer.Sound("CYBERBIT/Assets/sounds/GameEnd.wav")

#Imagen de las Plataformas
Suelo = pygame.image.load('CYBERBIT/Assets/images/Suelo.png')
Suelo = pygame.transform.scale(Suelo, (50, 50))

# Función para contar las monedas
def conteoMonedas(monedas):
    font = pygame.font.Font(None, 32)
    text = font.render("Monedas: " + str(moneda), True, blanco)
    text_rect = text.get_rect(center=(60, 10))
    pantalla.blit(text, text_rect)
    
def conteoVidas(vidas):
    font = pygame.font.Font(None, 32)
    text = font.render("Vidas: " + str(vidas), True, blanco)
    text_rect = text.get_rect(center=(60, 50))
    pantalla.blit(text, text_rect)

# Bucle del juego
corriendo = True
while corriendo:
    #pantalla.fill(azulCielo)
    # Dibujar la imagen de fondo
    pantalla.blit(imagenFondo, (0, 0))
    
    # Dibujar el contador de monedas y de vidas
    conteoVidas(vidas)
    conteoMonedas(moneda)

    # Dibujar el mapa
    muros = []
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):
            if nivel[fila][columna] == 1:
                rect = pygame.Rect(columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                pantalla.blit(Suelo, (columna * TAMANO_CELDA, fila * TAMANO_CELDA))
                muros.append(rect)
            if nivel[fila][columna] == 2:  # Meta
                pantalla.blit(Portal, (columna * TAMANO_CELDA, fila * TAMANO_CELDA))
            
    monedas = []
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 3:  # Identificamos la moneda en el mapa
                monedas.append((col * TAMANO_CELDA, fila * TAMANO_CELDA))
                pantalla.blit(Moneda, (col * TAMANO_CELDA, fila * TAMANO_CELDA))


    # Obtener controles
    Controles = pygame.key.get_pressed()
    mov_x = 0
    if Controles[pygame.K_LEFT]:
        mov_x = -VelocidadJugador
    if Controles[pygame.K_RIGHT]:
        mov_x = VelocidadJugador

    # Aplicar movimiento en X y verificar colisiones
    jugador_x += mov_x
    jugador = pygame.Rect(jugador_x, jugador_y, anchoJugador, alturaJugador)

    for muro in muros:
        if jugador.colliderect(muro):
            if mov_x > 0:  # Moviendo a la derecha
                jugador_x = muro.left - anchoJugador
            elif mov_x < 0:  # Moviendo a la izquierda
                jugador_x = muro.right

    # Aplicar gravedad
    velocidad_y += gravedad

    # Mover en Y y verificar colisiones
    jugador_y += velocidad_y
    jugador = pygame.Rect(jugador_x, jugador_y, anchoJugador, alturaJugador)

    en_suelo = False
    for muro in muros:
        if jugador.colliderect(muro):
            if velocidad_y > 0:  # Si está cayendo
                jugador_y = muro.top - alturaJugador
                velocidad_y = 0
                en_suelo = True
            elif velocidad_y < 0:  # Si golpea el techo
                jugador_y = muro.bottom
                velocidad_y = 0

    # Salto
    if Controles[pygame.K_UP] and en_suelo:#Al dar click en la flecha hacia arriba, el jugador salta
        velocidad_y = FUERZA_SALTO
        en_suelo = False

    # Dibujar al jugador en la nueva posición
    pantalla.blit(Jugador_Imagen, (jugador_x, jugador_y))

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Comprobar si el jugador toca una moneda
        for fila in range(len(nivel)):
            for col in range(len(nivel[fila])):
                if nivel[fila][col] == 3:  # Si hay una moneda
                    moneda_rect = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                    if jugador.colliderect(moneda_rect):
                        nivel[fila][col] = 0  # Cambiar el valor a 0 para eliminar la moneda del mapa
                        # Reproducir el sonido
                        sonidoMoneda.play()
                        # Esperar a que termine el sonido
                        #pygame.time.wait(int(sonidoMoneda.get_length() * 1000))
                        moneda += 1
                        conteoMonedas(moneda)


    # Comprobar si toca la meta
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 2:  # Meta
                meta_rect = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                if jugador.colliderect(meta_rect):
                    JuegoTerminado.play()
                    messagebox.showinfo("Mensaje","Felicidades, ¡Has ganado!, Monedas recogidas: " + str(moneda))
                    # Cerrar la ventana principal
                    root.destroy()
                    corriendo = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()