#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import webbrowser
import time


#1A. DECLARO VARIABLES GLOBALES
contador=0
total=5

#2. PODEMOS EJECUTAR EL NAVEGADOR DE FORMA SENCILLA (OPEN("URL"))
    #ES EQUIVALENTE OPEN() Y OPEN_NEW().
#webbrowser.open_new("https://www.google.com/")

#3. NO ES LO MISMO EJECUTAR EL NAVEGADOR, A BRIR UNA PESTAÑA.
#webbrowser.open_new_tab("https://www.youtube.com/")

#webbrowser.open_new("https://www.marca.com/")

#4. PARA SABER EN QUE NAVEGADOR SE ESTÁ EJECUTANDO
#a = webbrowser.get()
#print(a)

#5. INTERACTUAR CON EL NAVEGADOR
#print("¿QUÉ QUIERES BUSCAR?: ")
#busqueda = input()

#print("PROCESANDO ...")
#webbrowser.open("https://www.google.com/search?q=" + busqueda)

#webbrowser.open_new("https://www.google.com/")

#6. BUCLES DE TIEMPO
print("El programa se barió por primera vez a las: " + time.ctime())

while contador < total:
    time.sleep(5)
    webbrowser.open("https://www.marca.com/")
    print("La web se abrió exactamente a las: " + time.ctime())
    #contador += 1
    contador = contador + 1
