#MANEJO DE DIRECTORIOS Y CARPETAS

#1. IMPORTAMOS LIBRERÍAS NECESARIAS
import os
import shutil

#2. SABER LA RUTA ACTUAL
carpetaactual = os.path.dirname(__file__)
print(carpetaactual)

#3. CREAR UNA CARPETA
carpetanueva = os.makedirs("nueva")
print(carpetanueva)
print("CARPETA NUEVA CREADA...")
input()

try:
    carpetanueva2 = os.makedirs("nueva2")
    print(carpetanueva2)
    print("CARPETA NUEVA2 CREADA...")
    input()
except OSError as error:
    print("CARPETA NUEVA2 YA EXISTE...")
    
    #3A. ¿CÓMO COPIAR Y PEGAR ARCHIVOS DE UNA CARPETA A OTRA?
shutil.copy("logovw.ico", "nueva2/1.ico")
print("ARCHIVO COPIADO A NUEVA2...")
input()

    #3B. ¿CÓMO CORTAR Y PEGAR ARCHIVOS DE UNA CARPETA A OTRA?
shutil.move("logovw.ico", "nueva/2.ico")
print("ARCHIVO CORTADO A NUEVA...")
input()

#4. ¿CÓMO BORRAR UNA CARPETA?
shutil.rmtree("nueva")
print("CARPETA NUEVA BORRADA...")
input()

try:
    os.rmdir("nueva2")
    print("CARPETA NUEVA2 BORRADA...")
    input()
except OSError as error:
    print("NO HA SIDO POSIBLE BORRAR DICHA CARPETA")
    
shutil.rmtree("nueva2")
print("CARPETA NUEVA2 BORRADA...")
input()

#5. ¿CÓMO MOVERSE ENTRE CARPETAS?
print(carpetaactual)
print(os.listdir())

carpetanueva = os.makedirs("nueva23")
os.chdir("nueva23")
print("La ruta actual tras el .chdir es: ", os.getcwd())

print(os.listdir())

