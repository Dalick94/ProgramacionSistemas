#IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import sqlite3

#Creo las opciones
driver = webdriver.Chrome()
driver.maximize_window()

#Entro a la web
driver.get("http://www.eltiempo.es")
time.sleep(2)

#Quito ventana de cookies
aceptar_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/a[1]')
aceptar_cookies.click()
time.sleep(3)

#Busco Murcia en la caja de texto
caja_busqueda = driver.find_element(By.XPATH, '//*[@id="term"]')
caja_busqueda.clear()
caja_busqueda.send_keys("Murcia")
time.sleep(1)
caja_busqueda.send_keys(Keys.RETURN)
time.sleep(2)

#Entro en la opcion Murcia
opcion_murcia = driver.find_element(By.XPATH, '/html/body/div[8]/main/div[4]/div/section[2]/div[1]/ul/li[1]/a/div[2]/p[1]')
opcion_murcia.click()
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div[4]/div/main/section[3]/section/section/ul[1]/li[2]/h2/a').click()

#Guardo los datos en variables

tiempo_hoy = driver.find_element(By.CLASS_NAME, "days").text
print(tiempo_hoy)

# Guardar los datos en un archivo CSV
data = {'Tiempo': [tiempo_hoy]}
df = pd.DataFrame(data)
df.to_csv('datos_tiempo.csv', index=False)

driver.close()
