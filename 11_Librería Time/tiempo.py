#1. IMPORTAMOS LA LIBRERÍA TIME
import time

#2. LA FUNCIÓN TIME() NOS DEVUELVE EL TIEMPO EN SEGUNDOS QUE HA PASADO HASTA AHORA
# DESDE EL 1/1/1970 (ESTANDARIZADO). NO SE UTILIZA MUCHO...
print(time.time())

#3. LA FUNCIÓN CTIME() NOS DEVUELVE LA FECHA Y HORA DEL SISTEMA OPERATIVO DONDE SE EJECUTA EL SCRIPT
print(time.ctime())

#4. LA FUNCIÓN LOCALTIME() DEVUELVE LA FECHA Y HORA DE ESA ZONA DONDE SE EJECUTA EL SCRIPT
print(time.localtime())

a=time.localtime()
print(a[2], a[1], a[0])

#5. LA FUNCIÓN GMTIME() DEVUELVE LA RESTA ENTRE EL AHORA DE SISTEMA OPERATIVO Y EL 1/1/1970. LO DEVUELVE EN
# ESTRUCTURA [...]. NO TIENE MUCHO USO...
print(time.gmtime())

#6. LA FUNCIÓN SLEEP(X) PARALIZA LA EJECUCIÓN DE UN SCRIPT, NO DEL SISTEMA OPERATIVO DURANTE X SEGUNDOS
print("Inicio de SLEEP")
time.sleep(3)
print("Fin de SLEEP")

#7. LA FUNCIÓN PERF_COUNTER() DEVUELVE EL VALOR EN SEGUNDOS
#   LA FUNCIÓN PERF_COUNTER_NS() HACE LO MISMO PERO EN NANOSEGUNDOS

def funciona(x):
    inicio = time.perf_counter()
    inicio2 = time.perf_counter_ns()
    n = 0
    for i in range(1, x):
        n += i**3
    final = time.perf_counter()
    final2 = time.perf_counter_ns()
    print(f'{final - inicio}')
    print(f'{final2 - inicio2}')
funciona(10000000)
