#1. IMPORTO LAS LIBRERÍAS NECESARIAS
import pygame
from pygame.locals import *

import sys

#2. INICIO LAS FUNCIONES DE LA LIBRERÍA PYGAME
pygame.init()


#3. CREO UNA VENTANA DINÁMICA
    #OJO, POR DEFECTO UNA VENTANA DINÁMICA SE CREA EN NEGRO.
w=1000
h=618
ventanadejuego = pygame.display.set_mode((w,h))

x=0
fondo2 = pygame.image.load("city2.jpg").convert()
ventanadejuego.blit(fondo2,(0,0))

framesporsegundo=120


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

posicionx=50
posiciony=200
ancho=40
velocidad=10

reloj=pygame.time.Clock()

#SALTO
salto=False
cuentasalto=10

#IZQUIERDA
izquierda=False

#DERECHA
derecha=False

#PASOS
cuentapasos = 0

# PARTE DE MOVIMIENTO
def actualizarpantalla():
    global cuentapasos
    global x
    
    posicionrelativa= x % fondo2.get_rect().width
    ventanadejuego.blit(fondo2,(posicionrelativa - fondo2.get_rect().width,0))
    if posicionrelativa < w:
        ventanadejuego.blit(fondo2,(posicionrelativa,0))
    # SI ES MENOS VA HACIA UN LADO. SI ES + VA HACIO EL CONTRARIO  
    x -= 10
    #CONTADOR DE PASOS
    if cuentapasos + 1 >= 6:
        cuentapasos=0
    #MOVER A LA IZQUIERDA
    if izquierda:
        ventanadejuego.blit(caminaizquierda[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1
    #MOVER A LA DERECHA
    elif derecha:
        ventanadejuego.blit(caminaderecha[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1
    #SALTAR
    elif salto + 1 >= 2:
        cuentapasos=0
        ventanadejuego.blit(salta[cuentapasos // 1], (int(posicionx), int(posiciony)))
        cuentapasos += 1
    else:
        ventanadejuego.blit(quieto, (int(posicionx), int(posiciony)))        

    pygame.display.update()

ejecucion = True

while ejecucion:
    reloj.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            ejecucion = False

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_LEFT] and posicionx > velocidad:
        posicionx = velocidad
        izquierda = True
        derecha = False

    elif tecla[pygame.K_RIGHT] and posicionx < 1000 - velocidad - ancho:
        posicionx += velocidad
        izquierda = False
        derecha = True

    else:
        izquierda = False
        derecha = False
        cuentapasos=0

    if tecla[pygame.KEYUP] and posiciony > 200:
         posiciony -= velocidad

    if tecla[pygame.KEYDOWN] and posiciony < 500:
        posiciony += velocidad

    if not(salto):
        if tecla[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentapasos=0
        else:
            if cuentasalto >= -10:
                posiciony -= (cuentasalto * abs(cuentasalto)) * 0.5
                cuentasalto -= 1
            else:
                cuentasalto = 10
                salto = False
    actualizarpantalla()

  
   #LE PUEDO DAR TÍTULO E ICONO A LA VENTANA DINÁMICA
pygame.display.set_caption("Mi primer juego")
icono=pygame.image.load("mario.jpg")
pygame.display.set_icon(icono)
