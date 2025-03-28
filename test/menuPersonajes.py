import pygame
import sys
from juego import Juego
from menu import Menu

class MenuPersonajes:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente = pygame.font.Font(None, 50)
        self.fuente_titulo = pygame.font.Font(None, 70)
        
        # Lambda para cargar y escalar imágenes
        cargar_imagen = lambda path: pygame.transform.scale(pygame.image.load(path), (300, 300))
        
        # Cargar imágenes usando lambda
        self.imagenes_muerte = [
            cargar_imagen("./Assets/images/Rana/Muerte/Personaje Rana MUERTE3.png"),
            cargar_imagen("./Assets/images/Zorro/Muerte/Personaje Zorro MUERTE3.png"),
            cargar_imagen("./Assets/images/Panda/Muerte/Personaje Panda MUERTE3.png")
        ]
        
        self.imagenes_seleccion = [
            cargar_imagen("./Assets/images/Michelle.png"),
            cargar_imagen("./Assets/images/Zorrito.png"),
            cargar_imagen("./Assets/images/Panda.png")
        ]
        
        # Posiciones de los cuadros
        self.posiciones = [(200, 200), (520, 200), (840, 200)]
        self.seleccion = 0
        
        # Animación de entrada
        self.animacion_entrada = self.AnimacionEntrada(pantalla)
        self.animando = True
        
        # Lambda para determinar color de borde
        self.color_borde = lambda i: (237, 54, 140) if i == self.seleccion else (180, 180, 180)
        
        # Lambda para obtener imagen según selección
        self.obtener_imagen = lambda i: self.imagenes_seleccion[i] if i == self.seleccion else self.imagenes_muerte[i]
        
        # Mapeo de teclas a acciones (con lambdas)
        self.acciones_teclado = {
            pygame.K_LEFT: lambda: (self.seleccion - 1) % len(self.imagenes_muerte),
            pygame.K_RIGHT: lambda: (self.seleccion + 1) % len(self.imagenes_muerte),
            pygame.K_RETURN: lambda: self.seleccion
        }

    class AnimacionEntrada:
        def __init__(self, pantalla):
            self.pantalla = pantalla
            self.frames = []
            self.cargar_frames()
            self.duracion_frame = 100
            self.frame_actual = 0
            self.activa = True
            self.tiempo_ultimo_frame = pygame.time.get_ticks()
            
        def cargar_frames(self):
            # Lambda para cargar frames con manejo de errores
            cargar_frame = lambda i: (
                pygame.transform.scale(
                    pygame.image.load(f'Assets/images/Fondos/Fondo animado/fondoAnimado{i}.png').convert_alpha(), 
                    (1366, 768)
            ))
            
            for i in range(13, 28):
                try:
                    self.frames.append(cargar_frame(i))
                except:
                    backup = pygame.transform.scale(
                        pygame.image.load('./Assets/images/Fondos/Fondo animado/fondoAnimado28.png'), 
                        (1366, 768))
                    self.frames.append(backup)
        
        def actualizar(self):
            if not self.activa:
                return False
                
            # Lambda para actualizar frame
            actualizar_frame = lambda: (
                self.frame_actual + 1,
                pygame.time.get_ticks()
            )
            
            if pygame.time.get_ticks() - self.tiempo_ultimo_frame > self.duracion_frame:
                self.frame_actual, self.tiempo_ultimo_frame = actualizar_frame()
                
            return self.frame_actual < len(self.frames)
        
        def dibujar(self):
            if self.activa and self.frame_actual < len(self.frames):
                self.pantalla.blit(self.frames[self.frame_actual], (0, 0))

    def dibujar(self):
        """Dibuja los personajes en la pantalla usando lambdas"""
        if self.animando:
            if self.animacion_entrada.actualizar():
                self.animacion_entrada.dibujar()
                return
            else:
                self.animando = False
        
        # Lambda para cargar y dibujar fondo
        dibujar_fondo = lambda: (
            self.pantalla.blit(
                pygame.transform.scale(
                    pygame.image.load('./Assets/images/Fondos/Fondo animado/fondoAnimado28.png'), 
                    (1366, 768)), 
                (0, 0)))
        dibujar_fondo()
        
        # Dibujar título
        titulo = self.fuente_titulo.render("Selecciona un personaje", True, (255, 255, 255))
        self.pantalla.blit(titulo, (450, 80))

        # Lambda para dibujar cada personaje
        dibujar_personaje = lambda i, pos: (
            pygame.draw.rect(self.pantalla, self.color_borde(i), (pos[0]-10, pos[1]-10, 320, 320), 10),
            self.pantalla.blit(self.obtener_imagen(i), pos)
        )
        
        for i, pos in enumerate(self.posiciones):
            dibujar_personaje(i, pos)

        # Mostrar mensaje
        texto = self.fuente.render("Presiona Enter para elegir", True, (255, 255, 255))
        self.pantalla.blit(texto, (480, 550))

    def manejar_eventos(self):
        """Maneja la selección de personajes con lambdas"""
        if self.animando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            return None
        
        sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/select.mp3")
        sonidoMoneda.set_volume(0.5)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                accion = self.acciones_teclado.get(evento.key)
                if accion:
                    if evento.key == pygame.K_RETURN:
                        sonidoMoneda.play()
                        return accion()  # Retorna selección
                    self.seleccion = accion()
        
        return None