#PARA CONSULTAR CONTENIDO EN LAS TABLAS DE UNA BBDD

#1. IMPORTAMOS LIBRERÍAS
import sqlite3

#2. ABRO LA BBDD
conexion = sqlite3.connect("miprimerabbdd.db")
print("Conexión realizada")

#3. CREO EL CURSOR
cur = conexion.cursor()
print("Creado cursor")

#4. EJECUTAMOS LA CONSULTA MEDIANTE FUNCIÓN
def consultasimple():
    try:
        consulta = """SELECT * FROM empleado"""
        cur.execute(consulta)
        registros = cur.fetchall()
        print("El número de registros seleccionados es: ", len(registros))
        for row in registros:
            print("ID: ", row[0])
            print("NOMBRE: ", row[1])
            print("DEPARTAMENTO: ", row[2])
            print("\n")

    except sqlite3.error as error:
        print("ERROR EN LA EJECUCIÓN DE LA CONSULTA", error)

    finally:
        #conexion.commit()
        conexion.close()
        print("Conexión cerrada")
        #EL CIERRE DE CONEXIÓN SE PUEDE HACER AQUÍ (OPCIONAL)

#5. LLAMAMOS A LA FUNCIÓN PARA QUE SE EJECUTE LA CONSULTA
consultasimple()

#6. CERRAMOS LA CONEXIÓN AQUÍ (OPCIONAL)
