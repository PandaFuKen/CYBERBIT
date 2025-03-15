import pygame

class Sonidos:
    def __init__(self):
        self.sonidoMoneda = pygame.mixer.Sound("./Assets/sounds/Moneda.wav")
        self.JuegoTerminado = pygame.mixer.Sound("./Assets/sounds/GameEnd.wav")

    def reproducir_moneda(self):
        self.sonidoMoneda.play()

    def reproducir_juego_terminado(self):
        self.JuegoTerminado.play()