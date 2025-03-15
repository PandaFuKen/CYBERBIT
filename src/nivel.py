import pygame
from config import *

class Nivel:
    def __init__(self, nivel):
        self.nivel = nivel
        self.muros = []
        self.monedas = []
        self.meta = None

    def cargar_nivel(self):
        for fila in range(len(self.nivel)):
            for columna in range(len(self.nivel[fila])):
                if self.nivel[fila][columna] == 1:
                    rect = pygame.Rect(columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                    self.muros.append(rect)
                elif self.nivel[fila][columna] == 2:  # Meta
                    self.meta = pygame.Rect(columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA)
                elif self.nivel[fila][columna] == 3:  # Moneda
                    self.monedas.append((columna * TAMANO_CELDA, fila * TAMANO_CELDA))

    def dibujar(self, pantalla, suelo_img, portal_img, moneda_img):
        for muro in self.muros:
            pantalla.blit(suelo_img, muro)
        if self.meta:
            pantalla.blit(portal_img, self.meta)
        for moneda in self.monedas:
            pantalla.blit(moneda_img, moneda)