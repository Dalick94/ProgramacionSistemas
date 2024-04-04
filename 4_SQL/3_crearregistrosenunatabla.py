#PARA INSERTAR CONTENIDO EN LAS TABLAS

#1. IMPORTAMOS LIBRERÍAS
import sqlite3

#2. ABRO LA BBDD
conexion = sqlite3.connect("miprimerabbdd.db")
print("Conexión realizada")

#3. CREO EL CURSOR
cur = conexion.cursor()
print("Creado cursor")

#4. EJECUTO ORDEN UTILIZANDO EL CURSOR PARA UN ÚNICO REGISTRO
cur.execute('INSERT INTO empleado (id, nombre, departamento) VALUES ("2","Diego","Mandado")')
conexion.commit()
print("Empleado añadido")

#5. EJECUTO ORDEN PARA INSERTAR VARIOS REGISTROS A LA VEZ EN DEPARTAMENTO

def insertarvariosregistros(nuevosempleados):
    try:
        ordendeinsercion = """INSERT INTO departamento(id, nombre) VALUES (?, ?)"""
        cur.executemany(ordendeinsercion, nuevosempleados)
        conexion.commit()
    except sqlite3.Error as error:
        print("ERROR AL INSERTAR VARIOS EMPLEADOS A LA VEZ", error)

lista = [(1,"Administración"),
         (2,"Ingeniería"),
         (3,"Mantenimiento")]

insertarvariosregistros(lista)

#6. CIERRO LA BBDD
conexion.close()
print("Conexión cerrada")
