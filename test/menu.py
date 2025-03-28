import pygame
import sys

class Menu:
    def __init__(self, pantalla):
        pantalla = pygame.display.set_mode((1366, 768))
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 60)
        self.opciones = ["START", "EXIT"]
        self.seleccion = 0
        
        # Lambda para colores de texto
        self.color_texto = lambda i: (208, 81, 250) if i == self.seleccion else (50, 50, 50)
        
        # Lambda para renderizar texto
        self.renderizar_texto = lambda texto, color: self.fuente.render(texto, True, color)
        
        # Mapeo de teclas a acciones (usando lambdas)
        self.acciones_teclado = {
            pygame.K_DOWN: lambda: (self.seleccion + 1) % len(self.opciones),
            pygame.K_UP: lambda: (self.seleccion - 1) % len(self.opciones),
            pygame.K_RETURN: lambda: self.seleccion
        }

    def dibujar(self):
        """Dibuja el menú en pantalla usando lambdas para simplificar"""
        # Cargar fondo
        imagenFondo = pygame.image.load('./Assets/images/Fondos/FondoInicio.png')
        imagenFondo = pygame.transform.scale(imagenFondo, (1366, 768))
        self.pantalla.blit(imagenFondo, (0, 0))
        
        # Dibujar opciones usando lambdas
        dibujar_opcion = lambda opcion, i: (
            self.pantalla.blit(
                self.renderizar_texto(opcion, self.color_texto(i)),
                (500, 300 + i * 60)
            ))
        
        for i, opcion in enumerate(self.opciones):
            dibujar_opcion(opcion, i)

    def manejar_eventos(self):
        """Maneja eventos del teclado usando lambdas"""
        sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/select.mp3")
        sonidoMoneda.set_volume(0.5)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                # Manejo de teclas con lambda
                accion = self.acciones_teclado.get(evento.key)
                if accion:
                    if evento.key == pygame.K_RETURN:
                        sonidoMoneda.play()
                        return accion()  # Retorna la selección actual
                    self.seleccion = accion()
                
        return None