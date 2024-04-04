#1. IMPORTO LAS LIBRERÍAS NECESARIAS
import pygame
from pygame.locals import *

import sys

#2. INICIO LAS FUNCIONES DE LA LIBRERÍA PYGAME
pygame.init()

ancho=1000
alto=618
framesporsegundo=600
reloj=pygame.time.Clock()
x=0

#3. CREO UNA VENTANA DINÁMICA
    #OJO, POR DEFECTO UNA VENTANA DINÁMICA SE CREA EN NEGRO.
ventanadejuego = pygame.display.set_mode((ancho,alto))
    
    #IMAGEN DE FONDO
fondo1 = pygame.image.load("city2.jpg")
ventanadejuego.blit(fondo1, (0,0))

    #PARA PONER TÍTULO A UNA VENTANA DINÁMICA
pygame.display.set_caption("Mi primera ventana dinámica")

    #PARA PONER ICONO A LA VENTANA
#icono = pygame.image.load("mario.jpg")
pygame.display.set_icon(pygame.image.load("mario.jpg"))
    

#4. LA VENTANA SE ESTÁ ACTUALIZANDO HASTA QUE PULSO BOTÓN ROJO
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    posicionrelativa = x % fondo1.get_rect().width
    ventanadejuego.blit(fondo1, (posicionrelativa - fondo1.get_rect().width, 0))
    x += 1
    pygame.display.update()
    reloj.tick(framesporsegundo)
