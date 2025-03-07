import pygame

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 500, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Personaje en 8 bits con movilidad")

# Cargar imagen del personaje
personaje = pygame.image.load("./Assets/images/Panda.png")  # Asegúrate de tener un PNG
personaje = pygame.transform.scale(personaje, (50, 50))  # Ajustar tamaño

# Posición inicial del personaje
x, y = ANCHO // 2, ALTO // 2
velocidad = 5  # Velocidad de movimiento

# Bucle principal
ejecutando = True
while ejecutando:
    pygame.time.delay(30)  # Pequeña pausa para controlar FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()
    x += (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT]) * velocidad
    y += (teclas[pygame.K_DOWN] - teclas[pygame.K_UP]) * velocidad

    # Limitar el movimiento a los bordes de la pantalla
    x = max(0, min(x, ANCHO - 50))
    y = max(0, min(y, ALTO - 50))

    # Dibujar el fondo y el personaje
    pantalla.fill((30, 30, 30))  # Color de fondo
    pantalla.blit(personaje, (x, y))  # Dibujar personaje

    pygame.display.update()  # Actualizar pantalla

pygame.quit()
