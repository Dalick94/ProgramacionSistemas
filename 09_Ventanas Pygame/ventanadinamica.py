#1. IMPORTAR LIBRERÍAS NECESARIAS
import pygame
from pygame.locals import *

import sys

#2. LA FUNCIÓN INIT() NOS PERMITE INFORMAR AL SISTEMA QUE VA A HABER DINAMISMO
pygame.init()

#3. CREO UNA PALETA DE COLORES
blanco=(255,255,255)
negro=(0,0,0)

rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

color1=(199,66,37)
color2=(97,205,53)

#4. CREAMOS LA VENTANA DINÁMICA
    #OJO, POR DEFECTO EL SISTEMA LA PONE EN FONDO NEGRO
ventanadejuego = pygame.display.set_mode((600,600))
    #COLOR DE FONDO
#ventanadejuego.fill(blanco)
#ventanadejuego.fill(negro)
#ventanadejuego.fill(rojo)
ventanadejuego.fill(verde)
#ventanadejuego.fill(azul)
#ventanadejuego.fill(color1)
#ventanadejuego.fill(color2)

#5. DIBUJAR FORMAS EN UNA VENTANA DINÁMICA
    #5A. LINEA (DESTINO, COLOR, (VALORES X E Y INICIALES), (VALORES X E Y FINALES), GROSOR )
linea = pygame.draw.line(ventanadejuego, rojo, (50,50), (600,600), 5)
print(linea)

    #5B. RECTÁNGULO (DESTINO, COLOR, (TUPLA DE PUNTO INICIAL X E Y, ANCHO Y ALTO))
rectangulo = pygame.draw.rect(ventanadejuego, color2, (150,200,250,275))
print(rectangulo)

    #5C. CÍRCULOS (DESTINO, COLOR, (TUPLA DE POSICIÓN X E Y DEL CENTRO), RADIO, RELLENO)
circulo = pygame.draw.circle(ventanadejuego, color1, (300,300), 80, 10)
print(circulo)

    #5D. ELIPSES (DESTINO, COLOR, (TUPLA DE CENTRO X E Y, ANCHO Y ALTO))
elipse = pygame.draw.ellipse(ventanadejuego, negro, (200,100,300,166), 10)
print(elipse)

    #5E. POLIGONOS (DESTINO, COLOR,
puntos=[(100,300),(200,500),(100,500),(250,350),(400,600)]
poligono = pygame.draw.polygon(ventanadejuego, negro, puntos, 7)
print(poligono)

#6. BUCLE DE CIERRE Y ACTUALIZACIÓN
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
