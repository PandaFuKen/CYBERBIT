import pygame
import sys

class Menu:
    def __init__(self, pantalla):
        pantalla = pygame.display.set_mode((1366, 768))
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 60)
        self.opciones = ["Iniciar Juego", "Salir"]
        self.seleccion = 0

    def dibujar(self):
        imagenFondo = pygame.image.load('./Assets/images/Free-Pixel-Art-Cloud-and-Sky-Backgrounds2.png')
        imagenFondo = pygame.transform.scale(imagenFondo, (1366, 768))
        
        """Dibuja el menú en pantalla"""
        self.pantalla.blit(imagenFondo, (0, 0))  # Dibujar la imagen de fondo
        for i, opcion in enumerate(self.opciones):
            color = (242, 54, 12) if i == self.seleccion else (50, 50, 50)
            texto = self.fuente.render(opcion, True, color)
            self.pantalla.blit(texto, (500, 300 + i * 60))
            #ARREGLAR LOS COLORES DE LOS TEXTOS DEL MENU

    def manejar_eventos(self):
        """Maneja eventos del teclado y retorna la opción seleccionada"""
        sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/select.mp3")
        sonidoMoneda.set_volume(0.5)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    self.seleccion = (self.seleccion + 1) % len(self.opciones)
                elif evento.key == pygame.K_UP:
                    self.seleccion = (self.seleccion - 1) % len(self.opciones)
                elif evento.key == pygame.K_RETURN:
                    sonidoMoneda.play()
                    return self.seleccion  # Retorna la opción seleccionada
        return None