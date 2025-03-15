import pygame

class Animaciones:
    def __init__(self, frames, frame_index=0, tiempo_desde_ultimo_frame=0, animacion_reposo=0.1):
        self.frames = frames
        self.frame_index = frame_index
        self.tiempo_desde_ultimo_frame = tiempo_desde_ultimo_frame
        self.animacion_reposo = animacion_reposo

    def actualizar(self, tiempo_transcurrido):
        self.tiempo_desde_ultimo_frame += tiempo_transcurrido
        if self.tiempo_desde_ultimo_frame >= self.animacion_reposo:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.tiempo_desde_ultimo_frame = 0

    def obtener_frame_actual(self):
        return self.frames[self.frame_index]