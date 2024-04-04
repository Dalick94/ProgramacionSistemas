#1. IMPORTAMOS LA LIBRERÍA NUMPY
# LE PONEMOS EL SOBRENOMBRE NP POR ACORTAR CÓDIGO CUANDO LA LLAMEMOS (... AS NP)
import numpy as np
import random

#2. CREAMOS DATOS FIJOS O LOS CAPTURAMOS DE CONSOLA, VENTANA TKINTER, VENTANA
#DINÁMICA, ARCHIVO DE TEXTO PLANO O ALGIUNA TABLA DE UNA BBDD.

#MUY IMPORTANTE, LOS DATOS DEBEN SER COHERENTES, ES DECIR, TODOS DEL MISMO TIPO.
contenido1 = [0, 900, 23], [1000, 2, 37], [1,5,8]
contenido2 = [23, -900, 1], [10, -2, 37], [0,0,0,]
a = np.array(contenido1)
b = np.array(contenido2)

#3. LA FUNCIÓN MIN() DEVUELVE EL VALOR MÍNIMO DE UN ARRAY YA CREADO.
minimo = a.min()
print("El valor mínimo es: ", minimo)
print()

#4. LA FUNCIÓN MAX() DEVUELVE EL VALOR MÁXIMO DE UN ARRAY YA CREADO.
maximo = a.max()
print("El valor máximo es: ", maximo)
print()

#5. LA FUNCIÓN SUM() DEVUELVE LA SUMA DE UN ARRAY YA CREADO.
suma = a.sum()
print("La suma de todos los elementos es: ", suma)
print()

#6. LA FUNCIÓN SQRT() DEVUELVE LA RAIZ CUADRADA DE LOS ELEMENTOS DE UNA MATRIZ.
raiz = np.sqrt(a)
print(raiz)
print()

#7. LA FUNCIÓN STD() DEVUELVE LA DESVIACIÓN ESTÁNDAR DE CADA UNO DE LOS ELEMENTOS DE UNA MATRIZ.
desviacion = np.std(a)
print(desviacion)
print()

#8. SUMA DE MATRICES (DEBEN TENER MISMAS DIMENSIONES)
suma = a + b
print(suma)
print()

#9. RESTA DE MATRICES (DEBEN TENER MISMAS DIMENSIONES)
resta = a - b
print(resta)
print()

#10 MULTIPLICACIÓN DE MATRICES (DEBEN TENER MISMAS DIMENSIONES)
mutiplicacion = np.matmul(a, b)
print(mutiplicacion)
print()

#11. DIVISIÓN DE MATRICES (DEBEN TENER MISMAS DIMENSIONES)
division = a / b
print(division)
print()








































