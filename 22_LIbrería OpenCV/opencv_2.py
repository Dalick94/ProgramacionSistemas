#1. IMPORTAMOS LIBRERÍAS
import cv2
import numpy as np
import matplotlib.pyplot as plt

#2. CARGAMOS LA IMAGEN Y LA MOSTRAMOS
img = cv2.imread('pieza1nok.jpg')
cv2.imshow('IMAGEN 1', img)

#3. REDIMENSIONAMOS LA IMAGEN
img2 = cv2.resize(img, (250, 250))
cv2.imshow('IMAGEN 2 (REDIMENSIONADO)', img2)

#4. DIBUJAMOS UN RECTÁNGULO (SOBREESCRIBIMOS LA IMAGEN)
#EMPIEZA(x,y), ACABA(x,y), COLOR(rgb), GROSOR(2)
cv2.rectangle(img2, (100, 180), (180, 250), (0, 255, 0), 2)
cv2.imshow('IMAGEN 3 (LOCALIZACIÓN DE ERROR)', img2)

#5. ROTAR UNA IMAGEN
(filas, columnas) = img.shape[:2]
M = cv2.getRotationMatrix2D((columnas/2, filas/2), 45, 1) #45 grados, 1 color de fondo(negro)
img3 = cv2.warpAffine(img, M, (columnas, filas))
cv2.imshow('IMAGEN 4 (ROTACIÓN)', img3)

#6. RECORTAR LA IMAGEN
img4 = img[200:300, 100:300]
cv2.imshow('IMAGEN 5 (RECORTE)', img4)

#7. FUNCIOMNES MÁS CONCRETAS
    #DESENFOQUE:
img5 = cv2.blur(img, (1, 10))
cv2.imshow('IMAGEN 6 (DESENFOQUE)', img5)
    #ENFOQUE
patron = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img6 = cv2.filter2D(img, -1, patron)
cv2.imshow('IMAGEN 7 (ENFOQUE)', img6)
    #ANÁLISIS DE SILUETA
escala_de_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_final = cv2.Canny(escala_de_grises, 100, 200)
cv2.imshow('IMAGEN 8 (ANÁLISIS FINAL)', img_final)
