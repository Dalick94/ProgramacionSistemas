#1. IMPORTAR LIBRERÍAS
import threading
import time
import datetime

#2. EJECUCIÓN EN UN ÚNICO HILO(SECUENCIAL)
def funcion1():
    time.sleep(2)
    pass

def funcion2():
    time.sleep(5)
    pass

def funcion3():
    time.sleep(2)
    pass

def funcion4():
    time.sleep(5)
    pass

tinicio = datetime.datetime.now()
funcion1()
funcion2()
funcion3()
funcion4()
tejecucion =datetime.datetime.now() - tinicio
print(tejecucion)


#3. EJECUCIÓN POR HILOS
tinicio_hilos = datetime.datetime.now()
hilo1 = threading.Thread(name="hilo1", target=funcion1)
hilo2 = threading.Thread(name="hilo2", target=funcion2)
hilo3 = threading.Thread(name="hilo3", target=funcion3)
hilo4 = threading.Thread(name="hilo4", target=funcion4)

hilosvivos = threading.active_count()
print(hilosvivos)

#INICIO LOS HILOS
hilo1.start()
idhiloactual1 = threading.current_thread()
nombrehiloactual = threading.current_thread().name
print(idhiloactual1)
print(nombrehiloactual)
hilo2.start()
hilo3.start()
hilo4.start()

#MATO LOS HILOS
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

tejecucion_hilos = datetime.datetime.now() - tinicio_hilos
print(tejecucion_hilos)