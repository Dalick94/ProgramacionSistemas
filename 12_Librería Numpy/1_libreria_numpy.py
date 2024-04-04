#1. IMPORTAMOS LA LIBRERÍA NUMPY
import numpy as np

#2. CREAR U OBTENER DATOS DESDE EL ORIGEN:
# CONSOLA (INPUT())
# VENTANAS TKINTER (ENTRY())
# VENTANAS DINÁMICAS -----
# ARCHIVOS DE TEXTO PLANO X.OPEN("r")
# BBDD (SELECT XXXXX FROM XXX) A UNA TABLA

# IMPORTANTE, PARA REALIZAR OPERACIONES, LOS DATOS DEBEN SER COHERENTES, ES DECIR, DEL MISMO TIPO.

#3. UN ARRAY DE 1D ES UNA LISTA CLÁSICA. NO ES MUY UTILIZADO. LE LLAMAN TAMBIÉN VECTOR.
contenido1 = [1,2,3]
contenido2 = [1,5,9]
array1da = np.array(contenido1)
array1db = np.array(contenido2)
print(array1da)
print(array1db)
print()
print(contenido1)
print(contenido2)
print()
print(array1da+array1db)
print()
print(contenido1 + contenido2)
print()

#4. UN ARRAY 2D SE DENOMINA MATRIZ. ES EL MÁS UTILIZADO. SE PUEDE ENCONTRAR COMO MATRIX.
contenido3 = [0,0,0], [2,5,8]
contenido4 = [1,7,3], [23,47,63]
array2da = np.array(contenido3)
array2db = np.array(contenido4)
print(array2da)
print(array2db)
print()
print(contenido3)
print(contenido4)
print()
print(array2da+array2db)
print()
print(contenido3 + contenido4)
print()

#5. UN ARRAY 3D O CUBO ES POCO UTILIZADO. SE PUEDE ENCONTRAR LLAMADO CUBE.
contenido5 = [[0,0,0], [2,5,8]], [[1,1,1], [6,7,8]]
contenido6 = [[5,7,9], [3,1,0]], [[23,45,87], [19,17,13]]
array3da = np.array(contenido5)
array3db = np.array(contenido6)
print(array3da)
print(array3db)
print()
print(contenido5)
print(contenido6)
print()
print(array3da+array3db)
print()
print(contenido5 + contenido6)
print()

#6. LA FUNCIÓN ZEROS() O ONES() CREAN ARRAYS DE CEROS O UNOS Y DE LAS DIMENSIONES QUE LE DIGAMOS.
arrayceros = np.zeros(4)
print(arrayceros)
print()

arrayunos = np.ones(4)
print(arrayunos)
print()

print(arrayceros+arrayunos)
print()































