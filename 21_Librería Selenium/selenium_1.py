#1. IMPORTAMOS LIBERÍAS NECESARIAS
import selenium
from selenium import webdriver
import time

#2. SELENIUM TIENE PODER ABSOLUTO SOBRE TODOS LOS NAVEGADORES
ventana_1 = webdriver.Chrome()
ventana_1.get('https://www.seat.es/')

#3. FUNCIONES DE LA LIBRERIA SELENIUM
    #REFRESH (ACTUALIZA LA PÁGINA)
time.sleep(5)
ventana_1.refresh()
    #QUIT (CERRRAR EL NAVEGADOR)
ventana_1.quit()
    #