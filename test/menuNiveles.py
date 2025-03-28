import pygame
import sys

class MenuNiveles:
    def __init__(self, pantalla, personaje_seleccionado):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 50)
        self.fuente_titulo = pygame.font.Font(None, 70)
        self.niveles = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4"]
        self.seleccion = 0
        self.personaje_seleccionado = personaje_seleccionado
        
        # Configuración de diseño
        self.config = {
            'columnas': 2,
            'espacio_x': 400,
            'espacio_y': 150,
            'ancho_boton': 300,
            'alto_boton': 100,
            'inicio_x': 350,
            'inicio_y': 200
        }
        
        # Lambda para renderizar texto
        self.render_texto = lambda texto, color: self.fuente.render(texto, True, color)
        
        # Lambda para color del botón
        self.color_boton = lambda i: (252, 254, 78) if i == self.seleccion else (100, 100, 100)

    def dibujar(self):
        """Dibuja el menú de niveles en pantalla"""
        # Cargar y dibujar fondo
        fondo = pygame.transform.scale(
            pygame.image.load('./Assets/images/Fondos/Fondo animado/fondoAnimado28.png'),
            (1366, 768)
        )
        self.pantalla.blit(fondo, (0, 0))
        
        # Dibujar título
        titulo = self.fuente_titulo.render("Selecciona un Nivel", True, (255, 255, 255))
        self.pantalla.blit(titulo, (450, 80))


        # Dibujar botones de niveles
        for i, nivel in enumerate(self.niveles):
            x = self.config['inicio_x'] + (i % self.config['columnas']) * self.config['espacio_x']
            y = self.config['inicio_y'] + (i // self.config['columnas']) * self.config['espacio_y']
            rect = pygame.Rect(x, y, self.config['ancho_boton'], self.config['alto_boton'])
            
            # Dibujar botón
            pygame.draw.rect(self.pantalla, self.color_boton(i), rect, border_radius=15)
            
            # Borde selección
            if i == self.seleccion:
                pygame.draw.rect(self.pantalla, (255, 255, 255), rect, 3, border_radius=15)
            
            # Texto centrado
            texto = self.render_texto(nivel, (255, 255, 255))
            texto_rect = texto.get_rect(center=rect.center)
            self.pantalla.blit(texto, texto_rect)

        # Mensajes inferiores
        mensajes = [
            ("Presiona Enter para seleccionar", 550),
            ("Usa las flechas para navegar", 600)
        ]
        
        for texto, y in mensajes:
            self.pantalla.blit(self.render_texto(texto, (255, 255, 255)), (440, y))

    def manejar_eventos(self):
        """Maneja los eventos del teclado"""
        sonido = pygame.mixer.Sound("./Assets/sounds/start.mp3")
        sonido.set_volume(0.5)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.seleccion = max(0, self.seleccion - 1)
                elif evento.key == pygame.K_RIGHT:
                    self.seleccion = min(len(self.niveles)-1, self.seleccion + 1)
                elif evento.key == pygame.K_UP:
                    self.seleccion = max(0, self.seleccion - self.config['columnas'])
                elif evento.key == pygame.K_DOWN:
                    self.seleccion = min(len(self.niveles)-1, self.seleccion + self.config['columnas'])
                elif evento.key == pygame.K_RETURN:
                    sonido.play()
                    return self.seleccion + 1  # Retorna 1-4
                elif evento.key == pygame.K_ESCAPE:
                    return -1  # Para volver atrás
        
        return None