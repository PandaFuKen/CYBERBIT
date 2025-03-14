import pygame
import sys
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Colores
blanco = (255, 255, 255)

# Configuración del juego
ANCHO, ALTO = 800, 600
TAMANO_CELDA = 40
gravedad = 1
VelocidadJugador = 7
FUERZA_SALTO = -16  # Fuerza del salto

# Jugador
jugador_x, jugador_y = 90, 280
anchoJugador, alturaJugador = 70, 70
velocidad_y = 0
en_suelo = False
vidas = 3

# Mapa del nivel
nivel = [
    [0] * 20,
    [0] * 20,
    [0] * 20,
    [0] * 20,
    [0] * 20,
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0] * 20,
    [0] * 20,
    [0] * 20,
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
]

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Cargar imágenes
Suelo = pygame.Surface((TAMANO_CELDA, TAMANO_CELDA))
Suelo.fill((139, 69, 19))  # Color marrón para el suelo

# Cargar sonido
JuegoTerminado = pygame.mixer.Sound("./Assets/sounds/GameEnd.wav")

# Función para contar vidas
def conteoVidas(vidas):
    font = pygame.font.Font(None, 32)
    text = font.render("Vidas: " + str(vidas), True, blanco)
    pantalla.blit(text, (10, 10))

# Función lambda para verificar si el jugador ha caído
verificar_muerte_por_caida = lambda y: y > ALTO

# Bucle del juego
corriendo = True
while corriendo:
    pantalla.fill((12, 183, 242))  # Fondo azul cielo
    conteoVidas(vidas)

    # Dibujar el mapa
    muros = []
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):
            if nivel[fila][columna] == 1:
                rect = pygame.Rect(columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                pantalla.blit(Suelo, (columna * TAMANO_CELDA, fila * TAMANO_CELDA))
                muros.append(rect)

    # Obtener controles
    Controles = pygame.key.get_pressed()
    mov_x = 0
    if Controles[pygame.K_LEFT]:
        mov_x = -VelocidadJugador
    elif Controles[pygame.K_RIGHT]:
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
    if Controles[pygame.K_UP] and en_suelo:
        velocidad_y = FUERZA_SALTO
        en_suelo = False

    # Verificar si el jugador ha caído fuera del nivel
    if verificar_muerte_por_caida(jugador_y):
        vidas -= 1
        jugador_x, jugador_y = 90, 280  # Reiniciar posición
        velocidad_y = 0
        if vidas <= 0:
            JuegoTerminado.play()
            messagebox.showinfo("Game Over", "Has perdido todas tus vidas.")
            pygame.quit()
            sys.exit()

    # Dibujar al jugador
    pygame.draw.rect(pantalla, (255, 0, 0), (jugador_x, jugador_y, anchoJugador, alturaJugador))  # Rojo

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
