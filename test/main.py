import pygame
import sys
from menu import Menu
from menuPersonajes import MenuPersonajes
from juego import Juego
from menuNiveles import MenuNiveles

pygame.init()#Clase principal a traves de la cual se inicia el juego
pantalla = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Menú Principal")

# Fase 1: Menú Principal
menu_principal = Menu(pantalla)
while True:
    opcion = menu_principal.manejar_eventos()
    if opcion is not None:
        if opcion == 0:  # Iniciar Juego → Pasamos al menú de personajes
            break
        elif opcion == 1:  # Salir
            pygame.quit()
            sys.exit()

    menu_principal.dibujar()
    pygame.display.flip()

# Fase 2: Menú de Personajes
menu_personajes = MenuPersonajes(pantalla)
personaje_seleccionado = None
while personaje_seleccionado is None:
    personaje_seleccionado = menu_personajes.manejar_eventos()
    menu_personajes.dibujar()
    pygame.display.flip()

print(f"Personaje seleccionado: {personaje_seleccionado}")

# Fase 3: Menú de Niveles
menu_niveles = MenuNiveles(pantalla, personaje_seleccionado)
nivel_seleccionado = None
while nivel_seleccionado is None:
    nivel_seleccionado = menu_niveles.manejar_eventos()
    menu_niveles.dibujar()
    pygame.display.flip()

print(f"Nivel seleccionado: {nivel_seleccionado}")


# Fase 4: Iniciar el juego con el personaje y el nivel seleccionados
Juego.Nivel(personaje_seleccionado,nivel_seleccionado)
