import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from jugador import Jugador
from nivel import Nivel
from config import *  # Importa todo desde config.py, incluido el mapa del nivel

# Inicializar pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Cargar imágenes
imagenFondo = pygame.image.load('./Assets/images/Free-Pixel-Art-Cloud-and-Sky-Backgrounds5.jpg')
imagenFondo = pygame.transform.scale(imagenFondo, (ANCHO, ALTO))
Portal = pygame.image.load('./Assets/images/Portal1.png')
Portal = pygame.transform.scale(Portal, (50, 50))
Moneda = pygame.image.load('./Assets/images/Moneda.png')
Moneda = pygame.transform.scale(Moneda, (50, 50))
Suelo = pygame.image.load('./Assets/images/Suelo.png')
Suelo = pygame.transform.scale(Suelo, (50, 50))

# Crear jugador y nivel
jugador = Jugador(90, 280)
nivel = Nivel(nivel)  # Usa la matriz del nivel desde config.py
nivel.cargar_nivel()

# Bucle del juego
corriendo = True
while corriendo:
    tiempo_transcurrido = clock.get_time() / 1500
    pantalla.blit(imagenFondo, (0, 0))

    # Dibujar nivel
    nivel.dibujar(pantalla, Suelo, Portal, Moneda)

    # Dibujar jugador
    jugador.dibujar(pantalla)

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()