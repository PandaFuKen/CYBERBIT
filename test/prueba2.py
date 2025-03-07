import pygame

# Configuración básica
ANCHO, ALTO = 800, 400 # Tamaño de la pantalla
TAMANO_CELDA = 40 # Tamaño de las celdas del nivel
GRAVEDAD = 1 # Gravedad del juego
VELOCIDAD_X = 5 # Velocidad de movimiento lateral
FUERZA_SALTO = -15 # Fuerza del salto

# Mapa del nivel (1 = suelo/plataforma, 0 = espacio vacío, 2 = meta)
nivel = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 1], # La meta (2) al final
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],   
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Mostrar pantalla
clock = pygame.time.Clock()

# Jugador (cambiar rectángulo por imagen)
jugador_imagen = pygame.image.load("./Assets/images/Panda.png")  # Cargar imagen del jugador
jugador_rect = jugador_imagen.get_rect()
jugador_rect.x, jugador_rect.y = 100, 300
vel_y = 0
en_suelo = False

# Función para dibujar el nivel
def dibujar_nivel():
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            x, y = col * TAMANO_CELDA, fila * TAMANO_CELDA
            if nivel[fila][col] == 1:
                pygame.draw.rect(pantalla, (100, 50, 0), (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujar tamaño de cuadro del mapa
            elif nivel[fila][col] == 2:  # Meta
                pygame.draw.rect(pantalla, (255, 255, 0), (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Meta en amarillo

# Función de colisión con plataformas
def colisiona(nuevo_rect):
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 1:
                pared = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                if nuevo_rect.colliderect(pared):
                    return True
    return False

# Bucle del juego
corriendo = True
while corriendo:
    pantalla.fill((50, 50, 50))  # Fondo gris oscuro
    dibujar_nivel()
    pantalla.blit(jugador_imagen, jugador_rect)  # Dibujar la imagen del jugador

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento lateral
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  # Movimiento a la izquierda
        nuevo_rect = jugador_rect.move(-VELOCIDAD_X, 0)
        if not colisiona(nuevo_rect):
            jugador_rect.x -= VELOCIDAD_X
    if teclas[pygame.K_RIGHT]:  # Movimiento a la derecha
        nuevo_rect = jugador_rect.move(VELOCIDAD_X, 0)
        if not colisiona(nuevo_rect):
            jugador_rect.x += VELOCIDAD_X

    # Salto
    if teclas[pygame.K_UP] and en_suelo:
        vel_y = FUERZA_SALTO
        en_suelo = False

    # Aplicar gravedad
    vel_y += GRAVEDAD
    nuevo_rect = jugador_rect.move(0, vel_y)

    if not colisiona(nuevo_rect):
        jugador_rect.y += vel_y
    else:
        vel_y = 0
        en_suelo = True

    # Comprobar si toca la meta
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 2:  # Meta
                meta_rect = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                if jugador_rect.colliderect(meta_rect):
                    print("¡Has ganado!")
                    corriendo = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
