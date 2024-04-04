#TIPO DE DATOS LIST (TAMBIÉN LLAMADO ARRAY O MATRIZ)

#UN LIST SIEMPRE SE CREA ENTRE CORCHETES
#PUEDE CREARSE VACÍO

lista = []
print(lista)

#INDEXACIÓN: EN LAS LISTAS EMPIEZA EN 0

lista2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(lista2)
print(lista2[1])

#SON MUTABLES, ES DECIR, SU CONTENIDO PUEDE CAMBIAR "EN CALIENTE"

lista3=[1,2,3,4]
print(lista3)
lista3[2]=23
print(lista3)

#CONCATENACIÓN

lista4 = ["Diego", "Palencia"]
lista5 = ["Julia", "Valladolid"]

lista6 = lista4 + lista5
print(lista6)
print(lista4[0],lista5[1])

#REPETICIÓN DE LISTAS
lista7 = [1,2,3,4]
lista8 = lista7 * 3
print(lista8)
print(lista7[0])
print(lista7[1])
print(lista7[2])
print(lista7[3])

#SPLIT()
#SEPARA EN ELEMENTOS UN STRING

usuario = "Diego Santiago Pajares 44913185G"
print(usuario)
lista9 = usuario.split()
print(lista9)
print(lista9[0])
print(lista9[1])
print(lista9[2])
print(lista9[3])

#JOIN()
#PERMITE UNIR VALORES DE UNA LISTA UTILIZANDO UN CARÁCTER QUE LE DEFINAMOS

print("Antes del join, la lista7 era así: ", lista9)
resultadojoin = "".join(lista9)
print(resultadojoin)

#LEN()
#DEVUELVE EL TAMAÑO DE LISTA

lista10 = [2,3,9,14]
print(lista10)
tamaño = len(lista10)
print(tamaño)

#SUM()
#SUMAR TODOS LOS VALORES DE UNA LISTA

suma = sum(lista10)
print(suma)

'''
lista11 = ["a","b"]
print(lista11)
suma2 = sum(lista11)
print(suma2)
'''

#MAX()
#DEVUELVE EL MÁXIMO VALOR NÚMERICO

lista12 = [6, 0, -1.3456, 258.25]
maximo = max(lista12)
print("Valor maximo: ",maximo)

#MIN()
#DEVUELVE EL MÍNIMO VALOR NÚMERICO

minimo = min(lista12)
print("Valor mínimo: ",minimo)

#APPEND()
#NOS PERMITE AÑADIR UN NUEVO ELEMENTO A UNA LISTA, PERO AL FINAL.

lista13 = [2,5,7,23,34]
print(lista13)
lista13.append("Diego")
lista13.append(24)
lista13.append(3.15)
lista13.append(True)
print(lista13)

#INSERT()
lista14 = [2,5,7,23,34]
print(lista14)
lista14.append("Diego")
lista14.insert(0,"Santiago")
print(lista14)

#POP()
#ELIMINA EL ÚLTIMO (POR DEFECTO) ELEMENTO DE UNA LISTA, ADMITE ARGUMENTO INDEX.
lista14.pop(0)
print(lista14)

#REMOVE()
#ELIMINA LOS ELEMENTOS QUE LE DEFINAS COMO ARGUMENTO

lista15 = [1, 1.2, 1.4, 1, 1]
lista15.remove(1)
print(lista15)

#DEL
#BORRA TODA LA LISTA
#DEL[INDEX]
#BORRA EL ELEMENTO DEFINIDO POR INDEXACIÓN

lista16 = [1, 1.2, 1.4, 1, 10000]
print(lista16)
del lista16[2]
print(lista16)

lista16 = []
print(lista16)

#del lista16
#print(lista16)

#COUNT()
#DEVUELVE EL NÚMERO DE VECES QUE APARECE UN VALOR EN UNA LISTA

lista17 = [0, 1, 2, -1.5, 4, 100, -1.5, 1.1, "Diego"]
print(lista17)
repeticiones = lista17.count("Diego")
print("El número de apariciones de Diego en la lista es:",repeticiones)


# Definir una lista
lista = [1, 2, 3, 4, 2]

# Calcular la media aritmética
media = sum(lista) / len(lista)

print("La media aritmética de la lista es:", media)


#REVERSE()
#INVIERTE LA LISTA. OJO, NO LA ORDENA, LA DA LA VUELTA.

listab = [1, 2, 3, 4, 2]
print(listab)
print(listab[0])
listab.reverse()
print(listab)
print(listab[0])

#SORT()
#ORDENA DE MENOR A MAYOR (ARGUMENTO OPCIONAL REVERSE)

listac = [1, 2, 3, 4, 2, 79, 16, 1000, 0, -10, -1.66]
print(listac)
listac.sort(reverse=True)
print(listac)
listac.reverse()
print(listac)

listad = ["A","a","Z","y","c","F","J","@","/","1","-10.45"]
print(listad)
listad.sort()
print(listad)

















































