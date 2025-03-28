import pygame
import sys
from juego import Juego
from menu import Menu

class MenuNiveles:#Menu a traves del cual mostramos y el usuario selecciona de la lista de niveles que estan dentro del videojuego
    def __init__(self, pantalla, personaje_seleccionado):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 50)

        self.niveles = ["Nivel 1",
                        "Nivel 2",
                        "Nivel 3",
                        "Nivel 4"]
        self.posiciones = [(200, 200), (520, 200), (840, 200)]
        
        self.seleccion = 0  # Índice del nivel seleccionado

    def dibujar(self):
        """Dibuja los niveles en la pantalla como texto en lugar de imágenes."""
        imagenFondo = pygame.image.load('./Assets/images/Fondos/Fondo1.png')
        imagenFondo = pygame.transform.scale(imagenFondo, (1366, 768))
        self.pantalla.blit(imagenFondo, (0, 0))  # Dibujar la imagen de fondo

        COLUMNAS = 3  # Cantidad de niveles por fila
        ESPACIO_X = 420  # Espacio horizontal entre botones
        ESPACIO_Y = 80   # Espacio vertical entre filas
        INICIO_X = 100   # Posición inicial en X
        INICIO_Y = 100   # Posición inicial en Y

        for i, nivel in enumerate(self.niveles):#Colores y diseño de los cuadros de seleccion de nivel
            fila = i // COLUMNAS
            columna = i % COLUMNAS
            x = INICIO_X + columna * ESPACIO_X
            y = INICIO_Y + fila * ESPACIO_Y

            color_cuadro = (242, 54, 12) if i == self.seleccion else (180, 180, 180)
            pygame.draw.rect(self.pantalla, color_cuadro, (x - 10, y - 10, 200, 60), border_radius=10)

            color_texto = (0, 0, 0)  # Color del texto
            texto = self.fuente.render(nivel, True, color_texto)
            self.pantalla.blit(texto, (x, y))


        # Mostrar mensaje de selección
        mensaje = self.fuente.render("Presiona Enter para elegir", True, (0, 0, 0))
        self.pantalla.blit(mensaje, (450, 550))

    def manejar_eventos(self):
        """Maneja los eventos del teclado para seleccionar un nivel."""
        sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/start.mp3")
        sonidoMoneda.set_volume(0.5)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.seleccion = (self.seleccion - 1) % len(self.niveles)
                elif evento.key == pygame.K_RIGHT:
                    self.seleccion = (self.seleccion + 1) % len(self.niveles)
                elif evento.key == pygame.K_UP:
                    self.seleccion = (self.seleccion - 3) % len(self.niveles)
                elif evento.key == pygame.K_DOWN:
                    self.seleccion = (self.seleccion + 3) % len(self.niveles)
                elif evento.key == pygame.K_RETURN:
                    sonidoMoneda.play()
                elif evento.key == pygame.K_ESCAPE:
                    
                    
                    return self.seleccion+1  # Retorna el nivel seleccionado
                
                

        return None
