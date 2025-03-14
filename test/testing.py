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
anchoJugador, alturaJugador = 70, 70  # Actualizado a 70x70
velocidad_y = 0
en_suelo = False
frame_index = 0
animacion_reposo = 0.1  # Tiempo entre frames de la animación
tiempo_desde_ultimo_frame = 0

# Monedas
moneda = 0

# Vidas
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

# Cargar los frames de la animación en una lista
reposo_frames = [
    pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO1.png"),
    pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO2.png"),
    pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO3.png"),
    pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO4.png")
]
# Ajustamos el tamaño de los frames
reposo_frames = [pygame.transform.scale(frame, (70, 70)) for frame in reposo_frames]

# Cargar los frames de la animación de caminar
caminar_frames = [
    pygame.image.load("./Assets/images/Zorrito/Caminar/Personaje Zorro CAMINANDO1.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar/Personaje Zorro CAMINANDO2.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar/Personaje Zorro CAMINANDO3.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar/Personaje Zorro CAMINANDO4.png")
]
# Ajustamos el tamaño de los frames de caminar
caminar_frames = [pygame.transform.scale(frame, (70, 70)) for frame in caminar_frames]

# Cargar los frames de la animación de caminar ATRAS
caminar_atras_frames = [
    pygame.image.load("./Assets/images/Zorrito/Caminar Atras/Zorrito Caminando ATRAS1.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar Atras/Zorrito Caminando ATRAS2.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar Atras/Zorrito Caminando ATRAS3.png"),
    pygame.image.load("./Assets/images/Zorrito/Caminar Atras/Zorrito Caminando ATRAS4.png")
]
# Ajustamos el tamaño de los frames de caminar ATRAS
caminar_atras_frames = [pygame.transform.scale(frame, (70, 70)) for frame in caminar_atras_frames]

# Cargar y ajustar el tamaño de la imagen del jugador
Jugador_Imagen = pygame.image.load("./Assets/images/Zorrito/Caminar/Personaje Zorro CAMINANDO1.png")
Jugador_Imagen = pygame.transform.scale(Jugador_Imagen, (70, 70))  # Ajustado a 70x70

# Cargar imagen de fondo
imagenFondo = pygame.image.load('./Assets/images/Free-Pixel-Art-Cloud-and-Sky-Backgrounds5.jpg')
imagenFondo = pygame.transform.scale(imagenFondo, (ANCHO, ALTO))
# Imagen del portal
Portal = pygame.image.load('./Assets/images/Portal1.png')
Portal = pygame.transform.scale(Portal, (50, 50))
# Imagen de la moneda
Moneda = pygame.image.load('./Assets/images/Moneda.png')
Moneda = pygame.transform.scale(Moneda, (50, 50))
sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/Moneda.wav")
JuegoTerminado = pygame.mixer.Sound("./Assets/sounds/GameEnd.wav")

# Imagen de las Plataformas
Suelo = pygame.image.load('./Assets/images/Suelo.png')
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

# Función para actualizar el frame de la animación
def actualizar_frame_animacion(tiempo_transcurrido, frames):
    global frame_index, tiempo_desde_ultimo_frame
    tiempo_desde_ultimo_frame += tiempo_transcurrido
    if tiempo_desde_ultimo_frame >= animacion_reposo:
        frame_index = (frame_index + 1) % len(frames)
        tiempo_desde_ultimo_frame = 0
        
#Funcion de muerte por caida  lamba
verificar_muerte = lambda y: y > ALTO

# Bucle del juego
corriendo = True
while corriendo:
    tiempo_transcurrido = clock.get_time() / 1500  # Tiempo transcurrido en segundos
    pantalla.blit(imagenFondo, (0, 0))  # Dibujar la imagen de fondo

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
        mirando_atras = True
    elif Controles[pygame.K_RIGHT]:
        mov_x = VelocidadJugador
        mirando_atras = False
    else:
        mirando_atras = None

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
    
    #Cuando el jugador se cae de la pantalla 
    if verificar_muerte(jugador_y):
        vidas -= 1
        jugador_x, jugador_y = 90, 280  # Reiniciar la posición
        velocidad_y = 0
        if vidas <= 0:
            JuegoTerminado.play()
            messagebox.showinfo("Game Over", "Has perdido todas tus vidas.")
            pygame.quit()
            sys.exit()


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
    if Controles[pygame.K_UP] and en_suelo:  # Al dar click en la flecha hacia arriba, el jugador salta
        velocidad_y = FUERZA_SALTO
        en_suelo = False

    # Actualizar y dibujar el jugador
    if mov_x == 0 and en_suelo:  # Si el jugador está en reposo
        actualizar_frame_animacion(tiempo_transcurrido, reposo_frames)
        pantalla.blit(reposo_frames[frame_index], (jugador_x, jugador_y))
    elif mov_x > 0 and en_suelo:  # Si el jugador está caminando
        actualizar_frame_animacion(tiempo_transcurrido, caminar_frames)
        pantalla.blit(caminar_frames[frame_index], (jugador_x, jugador_y))
    elif mov_x < 0 and en_suelo:  # Si el jugador está caminando atras
        actualizar_frame_animacion(tiempo_transcurrido, caminar_atras_frames)
        pantalla.blit(caminar_atras_frames[frame_index], (jugador_x, jugador_y))
    else:
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
                        sonidoMoneda.play()  # Reproducir el sonido
                        moneda += 1
                        conteoMonedas(moneda)

    # Comprobar si toca la meta
    for fila in range(len(nivel)):
        for col in range(len(nivel[fila])):
            if nivel[fila][col] == 2:  # Meta
                meta_rect = pygame.Rect(col * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                if jugador.colliderect(meta_rect):
                    JuegoTerminado.play()
                    messagebox.showinfo("Mensaje", "Felicidades, ¡Has ganado!, Monedas recogidas: " + str(moneda))
                    # Cerrar la ventana principal
                    root.destroy()
                    corriendo = False
    

    pygame.display.flip()
    clock.tick(30)

pygame.quit()