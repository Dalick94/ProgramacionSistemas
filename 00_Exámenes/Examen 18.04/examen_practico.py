#1. IMPORTAMOS LIBRERÍAS
import cv2 
import numpy as np
import matplotlib.pyplot as plt


#2. CARGAMOS LA IMAGEN 
img = cv2.imread('radiografia.jpg')

#3. REDIMENSIONAMOS LA IMAGEN
img2 = cv2.resize(img, (250, 350))

#4. DIBUJAMOS UN RECTÁNGULO (SOBREESCRIBIMOS LA IMAGEN)
#EMPIEZA(x,y), ACABA(x,y), COLOR(rgb), GROSOR(2)
cv2.rectangle(img2, (100, 180), (180, 250), (0, 255, 0), 2)
cv2.imshow('IMAGEN 1 (LOCALIZACIÓN DE LESIÓN)', img2)

#GUARDAMOS LA IMAGEN PROCESADA
cv2.imwrite('estudio1.jpg', img2)

#ANÁLISIS DE SILUETA (ESCALA DE GRISES)
escala_de_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_final = cv2.Canny(escala_de_grises, 50, 100)
cv2.imshow('IMAGEN 2 (ESCALA DE GRISES)', img_final)

#GUARDAMOS LA IMAGEN PROCESADA
cv2.imwrite('estudio2.jpg', img_final)
