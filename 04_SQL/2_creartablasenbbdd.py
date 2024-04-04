#IMPORTAMOS LA LIBRERÍA NECESARIA PARA ENTENDERNOS CON EL GESTOR DE BBDD
import sqlite3

#CREA O ABRE UNA BASE DE DATOS
conexion = sqlite3.connect("miprimerabbdd.db")
print("Conexión realizada")

#CREAMOS UN CURSOR (HERRAMIENTA PARA TRABAJAR DENTRO DE LA BBDD)
cur = conexion.cursor()
print("Creado el cursor")

#PARA CREAR UNA TABLA EMPLEADO
cur.execute("CREATE TABLE empleado(id, nombre, departamento)")
conexion.commit()
print("Tabla empleado creada")

#PARA CREAR UNA TABLA DEPARTAMENTO
cur.execute("CREATE TABLE departamento(id, nombre)")
conexion.commit()
print("Tabla departamento creada")

#CERRAMOS LA CONEXIÓN
conexion.close()
print("Conexión cerrada")
