#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS 
import threading
import time


#2. CREAMOS UNA FUNCIÓN QUE SE VA A EJECUTAR CUANDO SEA LLAMADA
def funcion1():
    print("Inicio de ejecución de la Función 1...")
    print()
    time.sleep(2)
    print("Fin de ejecución de la Función 1...")
    print()

#3. LLAMADA A LA FUNCIÓN SIMPLE (SIN UTILIZAR HILOS)
funcion1()
print()
print()

#4. CREACIÓN DE N HILOS
threads = list()
n=5
for i in range(n):
    t = threading.Thread(target=funcion1)
    #print()
    threads.append(t)
    #print()
    t.start()
    #print()

for t in threads:
    t.join()

    
