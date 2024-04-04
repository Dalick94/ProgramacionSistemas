#1. IMPORTAMOS LIBRERÍAS NECESARIAS
import bs4
from bs4 import BeautifulSoup
import requests

#2. COMENZAMOS A REALIZAR UN ANÁLISIS WEB
    #MARCAMOS EL DESTINO DEL ANÁLISIS
destino = requests.get('https://www.ferreteriadefrutos.com')
sopa = BeautifulSoup(destino.text, 'lxml')
    #EJECUTAMOS EL ANÁLISIS
    #OBTENER EL TÍTULO DE LA WEB
titulo = sopa.title
print(titulo)
print()
    #OBTENER EL FORMATO DE ESCRITURA
escritura = sopa.meta
print(escritura)
print()
    #OBTENER LOS LINKS QUE CONTIENE LA WEB 
enlaces = sopa.links
print(enlaces)
print()
    #OBTENER COMENTARIOS
comentarios = sopa.comment
print(comentarios)
print()
#3. PARA HACER BÚSQUEDAS CONCRETAS
busqueda = sopa.find('head')
print(busqueda)
print()
busqueda = sopa.find('title')
print(busqueda)
print()
busqueda = sopa.find('h1')
print(busqueda)
print()
busqueda = sopa.find('h2')
print(busqueda)
print()
busqueda = sopa.find('h3')
print(busqueda)
print()
busqueda = sopa.find('h4')
print(busqueda)
print()
busqueda = sopa.find('h5')
print(busqueda)
print()
busqueda = sopa.find('h6')
print(busqueda)

