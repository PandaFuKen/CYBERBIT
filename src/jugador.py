import pygame
from config import *

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 70
        self.alto = 70
        self.velocidad_y = 0
        self.en_suelo = False
        self.frame_index = 0
        self.tiempo_desde_ultimo_frame = 0
        self.animacion_reposo = 0.1

        # Cargar imágenes de animación
        self.reposo_frames = [
            pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO1.png"),
            pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO2.png"),
            pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO3.png"),
            pygame.image.load("./Assets/images/Zorrito/Reposo/Personaje Zorro ANIMADO4.png")
        ]
        self.reposo_frames = [pygame.transform.scale(frame, (self.ancho, self.alto)) for frame in self.reposo_frames]

    def actualizar_frame_animacion(self, tiempo_transcurrido, frames):
        self.tiempo_desde_ultimo_frame += tiempo_transcurrido
        if self.tiempo_desde_ultimo_frame >= self.animacion_reposo:
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.tiempo_desde_ultimo_frame = 0

    def dibujar(self, pantalla):
        pantalla.blit(self.reposo_frames[self.frame_index], (self.x, self.y))

    def mover(self, mov_x, muros):
        self.x += mov_x
        jugador_rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        for muro in muros:
            if jugador_rect.colliderect(muro):
                if mov_x > 0:  # Moviendo a la derecha
                    self.x = muro.left - self.ancho
                elif mov_x < 0:  # Moviendo a la izquierda
                    self.x = muro.right

    def aplicar_gravedad(self, muros):
        self.velocidad_y += gravedad
        self.y += self.velocidad_y
        jugador_rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

        self.en_suelo = False
        for muro in muros:
            if jugador_rect.colliderect(muro):
                if self.velocidad_y > 0:  # Si está cayendo
                    self.y = muro.top - self.alto
                    self.velocidad_y = 0
                    self.en_suelo = True
                elif self.velocidad_y < 0:  # Si golpea el techo
                    self.y = muro.bottom
                    self.velocidad_y = 0

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = FUERZA_SALTO
            self.en_suelo = False