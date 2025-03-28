import pygame
import sys
from juego import Juego
from menu import Menu

class MenuPersonajes:#Menu a traves del cual el jugador selecciona el personaje
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 50)
        
        # Cargar imágenes de personajes (coloca tus imágenes en "Assets")
        self.imagenes = [
            pygame.image.load("./Assets/images/Michelle.png"),
            pygame.image.load("./Assets/images/Zorrito.png"),
            pygame.image.load("./Assets/images/Panda.png")
        ]
        
        # Escalar imágenes para que tengan el mismo tamaño
        self.imagenes = [pygame.transform.scale(img, (300, 300)) for img in self.imagenes]
        
        # Posiciones de los cuadros
        self.posiciones = [(200, 200), (520, 200), (840, 200)]
        
        # Índice del personaje seleccionado
        self.seleccion = 0

    def dibujar(self):
        """Dibuja los personajes en la pantalla."""
        imagenFondo = pygame.image.load('./Assets/images/Fondos/Fondo1.png')
        imagenFondo = pygame.transform.scale(imagenFondo, (1366, 768))
        
        self.pantalla.blit(imagenFondo, (0, 0))  # Dibujar la imagen de fondo
        
        for i, (x, y) in enumerate(self.posiciones):
            # Resaltar el personaje seleccionado
            color = (242, 54, 12) if i == self.seleccion else (180, 180, 180)
            pygame.draw.rect(self.pantalla, color, (x-10, y-10, 320, 320), 10)
            self.pantalla.blit(self.imagenes[i], (x, y))

        # Mostrar mensaje de selección
        texto = self.fuente.render("Presiona Enter para elegir", True, (0, 0, 0))
        self.pantalla.blit(texto, (450, 550))

    def manejar_eventos(self):
        """Maneja la selección de personajes."""
        sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/select.mp3")
        sonidoMoneda.set_volume(0.5)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.seleccion = (self.seleccion - 1) % len(self.imagenes)
                elif evento.key == pygame.K_RIGHT:
                    self.seleccion = (self.seleccion + 1) % len(self.imagenes)
                elif evento.key == pygame.K_RETURN:
                    sonidoMoneda.play()
                    return self.seleccion  # Retorna el personaje seleccionado
        return None
