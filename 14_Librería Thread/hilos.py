#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS 
import threading
import time


#2. CREAMOS UNA FUNCIÓN QUE VA A EJECUTAR 1 ÚNICO HILO
def f1(rango):
    lista = list()
    for i in range(rango):
        lista.append(i)
        time.sleep(0.01)
    return lista

tiempoinicio = time.time()
lista = f1(100)
tiempoejecucion = time.time()- tiempoinicio
print('El tiempo de ejecución de 1 hilo ha sido: {}\n'.format(tiempoejecucion),' segundos')
print(lista,'\n')

#3. VARIOS HILOS REDUCEN TIEMPO DE EJECUCIÓN Y OPTIMIZAN EL USO DE RECURSOS (CPU Y RAM)
nhilos = 5
lista2 = list()

    #CREAMOS UNA FUNCIÓN
def f2(inicio,fin):
    lista2 = list()
    for i in range(inicio,fin):
        lista2.append(i)
        time.sleep(0.01)
    return lista2

p = len(lista)//nhilos
inicios = list()
fines = list()
inicio = 0
fin = p

for i in range(nhilos):
    inicios.append(inicio)
    fines.append(fin)
    inicio += p
    fin += p

tinicio = time.time()
hilos = list()

for i in range(len(inicios)):
    t = threading.Thread(target=f2, args=(inicios[i], fines[i],))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()        

lista2.sort()

tejecucion = time.time() - tinicio
print('El tiempo total en ejecutar {} hilos: {} segundos\n'.format(nhilos, tejecucion))