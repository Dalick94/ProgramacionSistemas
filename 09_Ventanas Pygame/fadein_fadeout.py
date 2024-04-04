#1. IMPORTAMOS LIBRERÍAS NECESARIAS
import pygame

#2. CREAR UN OBJETO DE PYGAME (VENTANA NO ESTÁTICA)

ventana=pygame.display.set_mode((1000,800))

def estadoinicial(width, height):
    contenedor1=pygame.Surface((width, height))
    contenedor1.fill((0,0,0))
    for alpha in range(0,100):
        contenedor1.set_alpha(alpha)
        actualizarventana()
        ventana.blit(contenedor1, (0,0))
        pygame.display.update()
        pygame.time.delay(100)
        
def actualizarventana():
    ventana.fill((255,255,255))
    pygame.draw.rect(ventana,(255,0,0),(200,300,200,200), 0)

ejecucion = True

while ejecucion:
    actualizarventana()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            estadoinicial(1000, 800)
    pygame.display.update()
