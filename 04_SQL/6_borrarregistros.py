#PARA MODIFICAR CONTENIDO EN LAS TABLAS

#1. IMPORTAMOS LIBRERÍAS
import sqlite3

#2. ABRO LA BBDD
conexion = sqlite3.connect("miprimerabbdd.db")
print("Conexión realizada")

#3. CREO EL CURSOR
cur = conexion.cursor()
print("Creado cursor")

#4. UTILIZO EL CURSOR COMO HERRAMIENTA PARA MODIFICAR
cur.execute('DELETE FROM departamento WHERE id = 10')
conexion.commit()
print("Modificación realizada")

#5. CIERRO LA BBDD
conexion.close()
print("Conexión cerrada")
