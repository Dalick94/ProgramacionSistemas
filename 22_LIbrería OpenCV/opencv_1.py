#1. IMPORTAMOS LIBRERÍAS
import cv2 
import numpy as np
import matplotlib.pyplot as plt

#2. CARGAMOS LA IMAGEN
img = cv2.imread('person_of_interest.jpg')

#3. FUNCIONES BÁSICAS
    #IMAGEN CON MATRIZ DE PÍXELES RGB
print(img)
    #PARA EJECUTAR LA APERTURA DE UNA IMAGEN
cv2.imshow('IMAGEN 1 (TAMAÑO BASE)', img)
    #REDIMENSIONADO DE UNA IMAGEN
img2 = cv2.resize(img, (500,500))
cv2.imshow('IMAGEN 2 (REDIMENSIONADA)', img2)
    #PARA HACER PROCESO DE COMPROBACIÓN Y ESPERA
img3 = cv2.resize(img2, (250, 250))
cv2.imshow('IMAGEN 3 (REDIMENSIONADO Y A LA ESPERA)', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
    #GUARDAR LA IMAGEN PROCESADA
cv2.imwrite('pieza1_ok.jpg', img3)
    #LA FUNCIÓN UMBRAL OSCURECE LA IMAGEN
img4 = cv2.imread('pieza1_ok.jpg', 0)
ret, tresh = cv2.threshold(img4, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('IMAGEN CON UMBRAL A NEGRO', img4)
