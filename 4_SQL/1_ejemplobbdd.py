#IMPORTAMOS LA LIBRERÍA NECESARIA PARA ENTENDERNOS CON EL GESTOR DE BBDD
import sqlite3

#CREA O ABRE UNA BASE DE DATOS
conexion = sqlite3.connect("miprimerabbdd.db")
print("Conexión realizada")

#CIERRA LA BBDD
conexion.close()
print("Conexión cerrada")
