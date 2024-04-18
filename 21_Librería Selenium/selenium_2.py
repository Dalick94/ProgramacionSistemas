#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import os #Control del sistema operativo
import selenium #Control del sistema web
from selenium import webdriver #Control de todos los navegadores
from selenium.webdriver.common.keys import Keys #Simular que se maneja el teclado
from selenium.webdriver.common.by import By #Simular que se maneja el ratón
import time

#2. ELEGIMIENTOS HERRAMIENTA Y VÍCTIMA
    #OBLIGO AL S.O. A ABRIR UNA WEB EN CHROME
ventana=webdriver.Chrome()
ventana.get("https://www.python.org/")
    #CLAÚSULAS DE SEGURIDAD (SI ENCUENTRA LA PALABRA CLAVE, CONTINÚA. SI NO, SALE DEL BUCLE)
assert "Python" in ventana.title
    #TENDREMOS EL ELEMENTO A MANEJAR PREVIAMENTE RECONOCIDO ("INSPECCIONAR LA WEB")
busqueda_1 = ventana.find_element(By.NAME, "q")
busqueda_1.send_keys("MI PRIMER ATAQUE")
time.sleep(5)
busqueda_1.clear()
time.sleep(5)
busqueda_1.send_keys("SELENIUM")
#busqueda_1.send_keys(Keys.RETURN)

busqueda_2 = ventana.find_element(By.NAME, "submit")
busqueda_2.click()

#3. QUIT() CIERRO LA VENTANA. CLOSE() CIERRO LA VENTANA Y BORRO LOGS DEL S.O.
ventana.close()
