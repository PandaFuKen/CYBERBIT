import pygame
import random

# Configuración básica
ANCHO, ALTO = 800, 600  # Tamaño de la pantalla
TAMANO_CELDA = 40  # Tamaño de las celdas del nivel
VELOCIDAD_JUGADOR = 5  # Velocidad de movimiento del jugador
FPS = 30  # Frame por segundo

# Mapa del nivel: 1 = pared, 0 = espacio libre, 2 = píldora
nivel = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))  # Mostrar pantalla
clock = pygame.time.Clock()

# Jugador (Pac-Man)
jugador_imagen = pygame.image.load("CYBERBIT\Assets\images\Panda.png")  # Asegúrate de tener una imagen de Pac-Man
jugador_rect = jugador_imagen.get_rect()
jugador_rect.x, jugador_rect.y = 120, 100

# Fantasmas
fantasmas = []
for _ in range(3):  # 3 fantasmas
    fantasma_imagen = pygame.image.load("CYBERBIT\Assets\images\Michelle.png")  # Asegúrate de tener una imagen de fantasma
    fantasma_rect = fantasma_imagen.get_rect()
    fantasma_rect.x = random.randint(1, len(nivel[0]) - 2) * TAMANO_CELDA
    fantasma_rect.y = random.randint(1, len(nivel) - 2) * TAMANO_CELDA
    fantasmas.append(fantasma_rect)

# Función para dibujar el nivel
def dibujar_nivel():
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            x, y = col * TAMANO_CELDA, fila * TAMANO_CELDA
            if nivel[fila][col] == 1:  # Pared
                pygame.draw.rect(pantalla, (0, 0, 255), (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Azul para las paredes
            elif nivel[fila][col] == 2:  # Píldora
                pygame.draw.circle(pantalla, (255, 255, 0), (x + TAMANO_CELDA // 2, y + TAMANO_CELDA // 2), 5)

# Función de colisión con paredes
def colisiona(nuevo_rect):
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 1:  # Pared
                pared = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                if nuevo_rect.colliderect(pared):
                    return True
    return False

# Función de colisión con fantasmas
def colisiona_con_fantasmas(rect):
    for fantasma in fantasmas:
        if rect.colliderect(fantasma):
            return True
    return False

# Movimiento de los fantasmas
def mover_fantasmas():
    for fantasma in fantasmas:
        direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
        if direccion == "izquierda" and fantasma.x > 0:  # Comprobar que no se sale de los límites
            fantasma.x -= VELOCIDAD_JUGADOR
        elif direccion == "derecha" and fantasma.x < (len(nivel[0]) - 1) * TAMANO_CELDA:
            fantasma.x += VELOCIDAD_JUGADOR
        elif direccion == "arriba" and fantasma.y > 0:
            fantasma.y -= VELOCIDAD_JUGADOR
        elif direccion == "abajo" and fantasma.y < (len(nivel) - 1) * TAMANO_CELDA:
            fantasma.y += VELOCIDAD_JUGADOR

# Bucle del juego
corriendo = True
while corriendo:
    pantalla.fill((0, 0, 0))  # Fondo negro
    dibujar_nivel()
    pantalla.blit(jugador_imagen, jugador_rect)  # Dibujar la imagen del jugador

    # Dibujar los fantasmas
    for fantasma in fantasmas:
        pantalla.blit(fantasma_imagen, fantasma)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  # Movimiento a la izquierda
        nuevo_rect = jugador_rect.move(-VELOCIDAD_JUGADOR, 0)
        if not colisiona(nuevo_rect):
            jugador_rect.x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT]:  # Movimiento a la derecha
        nuevo_rect = jugador_rect.move(VELOCIDAD_JUGADOR, 0)
        if not colisiona(nuevo_rect):
            jugador_rect.x += VELOCIDAD_JUGADOR
    if teclas[pygame.K_UP]:  # Movimiento hacia arriba
        nuevo_rect = jugador_rect.move(0, -VELOCIDAD_JUGADOR)
        if not colisiona(nuevo_rect):
            jugador_rect.y -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_DOWN]:  # Movimiento hacia abajo
        nuevo_rect = jugador_rect.move(0, VELOCIDAD_JUGADOR)
        if not colisiona(nuevo_rect):
            jugador_rect.y += VELOCIDAD_JUGADOR

    # Colisión con fantasmas
    if colisiona_con_fantasmas(jugador_rect):
        print("¡Te han atrapado!")
        corriendo = False

    # Mover fantasmas
    mover_fantasmas()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
