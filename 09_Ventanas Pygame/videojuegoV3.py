#VIDEOJUEGO DE ANDAR POR LA CIUDAD...

#1. IMPORTAR LAS LIBRERÍAS NECESARIAS
import pygame
from pygame.locals import *

import sys

#2. INICIO DE LAS FUNCIONES DE LA LIBRERÍA PYGAME
pygame.init()

#3. CREO LA VENTANA DINÁMICA Y VARIABLES
ancho=1000
alto=618
ventanadejuego = pygame.display.set_mode((ancho,alto))
x=0
fondo = pygame.image.load("city2.jpg")
ventanadejuego.blit(fondo, (0,0))

framesporsegundo=108

pygame.display.set_caption("MARIO VISITA LA CIUDAD")
icono=pygame.image.load("mario.jpg")
pygame.display.set_icon(icono)


#4. DEFINIR ESTADOS POSIBLES DEL MUÑECO
quieto=pygame.image.load('mario.jpg')

caminaderecha=[pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg')]

caminaizquierda=[pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg'),
               pygame.image.load('mario.jpg')]

salta=[pygame.image.load('mario.jpg'),
        pygame.image.load('mario.jpg')]

posicionx=500
posiciony=309
anchomario=40
velocidad=20
reloj=pygame.time.Clock()
izquierda=False
derecha=False
salto=False
cuentapasos=0
cuentasalto=0

#5. MOVIMIENTOS DE PERSONAJE Y DE FONDO
def actualizarpantalla():
    global cuentapasos
    global x
    #PARA MOVER EL FONDO
    posicionrelativa = x % fondo.get_rect().width
    ventanadejuego.blit(fondo,(posicionrelativa - fondo.get_rect().width,0))
    if posicionrelativa < ancho:
        ventanadejuego.blit(fondo,(posicionrelativa,0))
    #PARA MOVER EL FONDO HACIA UN LADO O HACIA OTRO UTILIZAMO INCREMENTO O DECREMENTO
    x -= 10
    #CONTADOR DE PASOS
    if cuentapasos + 1 >= 6:
        cuentapasos=0
    #MOVIMIENTO HACIA LA IZQUIERDA
    if izquierda:
        ventanadejuego.blit(caminaizquierda[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1
    #MOVIMIENTO HACIA LA DERECHA
    elif derecha:
        ventanadejuego.blit(caminaderecha[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1 
    #SALTAR
    elif salto + 1 >= 2:
        ventanadejuego.blit(salta[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1
    #QUIETO
    else:
        ventanadejuego.blit(quieto, (int(posicionx), int(posiciony)))      

    pygame.display.update()

#6. BUCLE DE EJECUCIÓN, CIERRE Y FIN.
ejecucion=True

while ejecucion:
    reloj.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            ejecucion=False

    tecla = pygame.key.get_pressed()

    #OK
    if tecla[pygame.K_LEFT] and posicionx > velocidad:
        posicionx -= 10
        izquierda=True
        derecha=False
    #OK  
    elif tecla[pygame.K_RIGHT] and posicionx < 920:
        posicionx += 10
        izquierda=False
        derecha=True
        
    else:
        izquierda=False
        derecha=False
        cuentapasos=0
    #OK
    if tecla[pygame.K_UP] and posiciony > 90:
        posiciony -= 10

    #OK
    if tecla[pygame.K_DOWN] and posiciony < 488:
        posiciony += 10
        
    if not(salto):
        #SE DETIENE
        if tecla[pygame.K_SPACE]:
            salto = False
            izquierda = False
            derecha = False
            cuentapasos=0
        else:
            if cuentasalto >= -10:
                posiciony -= (cuentasalto * abs(cuentasalto)) * 0.25
                cuentasalto -= 1
            else:
                cuentasalto = 10
                salto = False
    actualizarpantalla()


