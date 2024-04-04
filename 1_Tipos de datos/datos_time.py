#TIPO DE DATOS DATE (TAMBIÉN CONOCIDOS COMO TIME, FECHA, ETC, ...)

#OJO, TODOS LOS DATOS DE FECHAS EN PHYTON LLEVAN FORMATO AMERICANO.
#ES DECIR, (AÑO-MES-DÍA).
#OJO, POR TANTO, NO ES FORMATO EUROPEO, QUE ES (DÍA-MES-AÑO).
#NO CONSIDERAR ESTO NOS PUEDE ACARREAR PROBLEMAS AL CAMBIAR COSAS DE SITIO
#SIN HACER COMPROBACIONES.

#APUNTE 1. ES MUY RECOMENDABLE ASEGURAR LA COMPATIBILIDAD DEL SCRIPT IMPORTANDO
# LA LIBRERÍA datetime

from datetime import date
from datetime import datetime

#PARTE 1. (FECHAS).
#PARA COMPROBAR SI FUNCIONAN FECHAS, CREAMOS UNA VARIABLE hoy, 
#LE DAMOS EL VALOR today Y LO SACAMOS POR PANTALLA
#date.today() MUESTRA LA FECHA DE SISTEMA OPERATIVO (EN PRINCIPIO ACTUALIZADA POR LOS SERVIDORES NTP
#DE MICROSOFT / LINUX / MAC/ GOOGLE / BLACKBERRY / ..., POR TANTO, SE CONSIDERA REAL Y FIABLE).

hoy = date.today()
print("La fecha actual es:",hoy)

    #1A. ATRIBUTOS POSIBLES

    #day
print("El día de la fecha actual es:",hoy.day)
    #month
print("El mes de la fecha actual es:",hoy.month)
    #year
print("El año de la fecha actual es:",hoy.year)

#PARTE 2. (HORAS).
    #PARA COMPROBAR SI FUNCIONAN HORAS, CREAMOS UNA VARIABLE ahora,

ahora = datetime.now()
print("La hora actual es:",ahora)

    #2A. ATRIBUTOS POSIBLES

    #hour
print("La hora de la fecha actual es:",ahora.hour)
    #minute
print("El minuto de la fecha actual es:",ahora.minute)
    #second
print("El segundo de la fecha actual es:",ahora.second)
