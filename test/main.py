import pygame
import sys
from menu import Menu
from menuPersonajes import MenuPersonajes
from juego import Juego
from menuNiveles import MenuNiveles

class AnimacionTransicion:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.frames = []
        self.duracion_frame = 50
        self.frame_actual = 0
        self.activa = False
        self.tiempo_ultimo_frame = 0
        
        # Lambda corregida para cargar frames
        self.cargar_frame = lambda i: (
            pygame.transform.scale(
                pygame.image.load(f'Assets/images/Fondos/Fondo animado/fondoAnimado{i}.png').convert_alpha(),
                (1366, 768)
            ) if pygame.image.get_extended() else
            pygame.Surface((1366, 768))
        )
        
        self.cargar_frames()
    
    def cargar_frames(self):
        try:
            self.frames = [self.cargar_frame(i) for i in range(1, 12)]
        except Exception as e:
            print(f"Error cargando frames: {e}")
            # Frame de respaldo negro si hay error
            self.frames = [pygame.Surface((1366, 768)) for _ in range(1, 12)]
            for frame in self.frames:
                frame.fill((0, 0, 0))
    
    def iniciar(self):
        self.activa = True
        self.frame_actual = 0
        self.tiempo_ultimo_frame = pygame.time.get_ticks()
        
    def actualizar(self):
        if not self.activa:
            return False
            
        # Lambda para actualizar frame
        actualizar = lambda: (
            self.frame_actual + 1,
            pygame.time.get_ticks()
        )
        
        if pygame.time.get_ticks() - self.tiempo_ultimo_frame > self.duracion_frame:
            self.frame_actual, self.tiempo_ultimo_frame = actualizar()
            
        return self.frame_actual < len(self.frames)
    
    def dibujar(self):
        if self.activa and self.frame_actual < len(self.frames):
            self.pantalla.blit(self.frames[self.frame_actual], (0, 0))

# Lambda para inicialización de pygame
inicializar_pygame = lambda: (
    pygame.init(),
    pygame.display.set_caption("Menú Principal"),
    pygame.display.set_mode((1366, 768))
)

# Lambda para manejar transición entre menús
manejar_transicion = lambda animacion, transicionando: (
    animacion.iniciar(),
    True
) if not transicionando else (None, transicionando)

# Lambda para crear instancias de menú
crear_menu = lambda pantalla, clase: clase(pantalla)

# Lambda para bucle principal de menú
bucle_menu = lambda menu: (
    menu.manejar_eventos(),
    menu.dibujar(),
    pygame.display.flip()
)

# Inicialización principal
inicializar_pygame()
pantalla = pygame.display.get_surface()
animacion = AnimacionTransicion(pantalla)
reloj = pygame.time.Clock()

# Fase 1: Menú Principal
menu_principal = crear_menu(pantalla, Menu)
transicionando = False

while True:
    reloj.tick(60)
    
    if not transicionando:
        opcion = menu_principal.manejar_eventos()
        if opcion is not None:
            if opcion == 0:  # Iniciar Juego
                _, transicionando = manejar_transicion(animacion, transicionando)
            elif opcion == 1:  # Salir
                pygame.quit()
                sys.exit()
    
    if not transicionando:
        menu_principal.dibujar()
    else:
        if not animacion.actualizar():
            break
        animacion.dibujar()
    
    pygame.display.flip()

# Fase 2: Menú de Personajes
menu_personajes = crear_menu(pantalla, MenuPersonajes)
personaje_seleccionado = None

while personaje_seleccionado is None:
    resultado = menu_personajes.manejar_eventos()
    menu_personajes.dibujar()
    pygame.display.flip()
    if resultado is not None:
        personaje_seleccionado = resultado

print(f"Personaje seleccionado: {personaje_seleccionado}")

# Fase 3: Menú de Niveles
menu_niveles = MenuNiveles(pantalla, personaje_seleccionado)
nivel_seleccionado = None

while nivel_seleccionado is None:
    resultado = menu_niveles.manejar_eventos()
    menu_niveles.dibujar()
    pygame.display.flip()
    if resultado is not None:
        nivel_seleccionado = resultado

print(f"Nivel seleccionado: {nivel_seleccionado}")

# Fase 4: Iniciar el juego
Juego.Nivel(personaje_seleccionado, nivel_seleccionado)