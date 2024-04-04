#FUNCIONES AVANZADAS DE LA LIBRERÍA NUMPY

#1. IMPORTAMOS LA LIBRERÍA NUMPY
import numpy as np
import random

#2. CREAMOS DATOS FIJOS O CAPTURADOS (CONSOLA, TKINTER, PYGAME, TEXTO PLANO O BBDD)
contenido1 = [0,0,0] #1D (vector)
contenido2 = [5,7,11,23,56], [3,7,23,15,21] #2D (matriz) ancho y alto
contenido3 = [[1,1,1], [5,5,5]], [[3,3,3], [7,7,7]] #3D (cubo) 
contenido4 = [True, False, True] #Boleano
contenido5 = [] #Vacío
contenido6 = ["Diego", "Raquel", "Julia"] #Caracteres

#3. LA FUNCIÓN NDIM() PERMITE CONOCER LAS DIMENSIONES DE UN ARRAY
a = np.array(contenido1)
print(a)
print(f"La dimensión del array contenido1 es: {a.ndim}")

b = np.array(contenido2)
print(b)
print(f"La dimensión del array contenido2 es: {b.ndim}")

c = np.array(contenido3)
print(c)
print(f"La dimensión del array contenido3 es: {c.ndim}")

d = np.array(contenido5)
print(d)
print(f"La dimensión del array contenido5 es: {d.ndim}")

#4. LA FUNCIÓN DTYPE() PERMITE CONOCER EL TIPO DE DATOS
print(a)
print(f"El tipo de datos del array contenido1 es: {a.dtype}")

e = np.array(contenido4)
print(e)
print(f"El tipo de datos del array contenido4 es: {e.dtype}")

f = np.array(contenido6)
print(f)
print(f"El tipo de datos del array contenido6 es: {f.dtype}")

#5. LA FUNCIÓN SIZE() NOS INFORMA DEL NÚMERO DE ELEMENTOS QUE TIENE UN ARRAY
print(f"El número de elementos de contenido2 es: {b.size}")
print(f"El número de elementos de contenido3 es: {c.size}")
print(f"El número de elementos de contenido4 es: {e.size}")

#6. LA FUNCIÓN RESHAPE(x,y) CONVIERTE FILAS EN COLUMNAS Y COLUMNAS EN FILAS, ES DECIR, LA TRANSPUESTA
print(b)
g = b.reshape(5,2)
print(g)

#7. PARA ACCEDER A UN CONTENIDO CONCRETO DE UN ARRAY: 
contenido7 = [9,100,2], [11,300,5], [1,500,8]
h = np.array(contenido7)
print(h)
print(h[1,1])
print(h[1,2])

#8. PARA EXTRAER UNA COLUMNAD DE UNA MATRIZ. MUY UTILIZADO:
print(h[0:, 2])

#9. PARA EXTRAER UNA FILA DE UNA MATRIZ. MUY UTILIZADO:
print(h[1, 0:])