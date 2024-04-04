#ALMACENAMIENTO DE INFORMACIÓN DE FORMA PERMANENTE
#NO ES NECESARIO IMPORTAR LIBRERÍAS
'''
fichero = open("primerarchivo.txt", "w")
'''


a = "Diego Santiago Pajares"
#¿CÓMO AÑADIMOS CONTENIDO A UN ARCHIVO?

#OJO BARRAS EN LA RUTA
fichero = open("C:/Users/DIEGO/Desktop/primerarchivo.txt", "a")

#AÑADIR CONTENIDO A UN FICHERO
fichero.write("MI PRIMER DATO ALMACENADO PERMANENTE\n          nfghfgdfgfgd\n")
fichero.write(a)
#ME MUESTRA POR CONSOLA SI EL ARCHIVO ESTÁ BIEN NOMBRADO (POR SI FALLA EL TXT)
print(fichero.name)

#ME MUESTRA POR CONSOLA EL ESTADO DEL ARCHIVO (OPEN O CLOSED)
print(fichero.closed)

#ME MUESTRA POR CONSOLA EL MODO DE APERTURA O MODO DE TRABAJO
print(fichero.mode)

#PARA CERRAR UN FICHERO
fichero.close()
