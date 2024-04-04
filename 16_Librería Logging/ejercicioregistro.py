#IMPORTAMOS LIBRERÍAS
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import logging

#2. CREAMOS EL LOGGER
logging.basicConfig(
    format='%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level=logging.INFO, 
    filename="info_log_almacen.log",  # Ruta y nombre del archivo de registro
    filemode="a"
)

#CREAMOS LA BBDD
conexion = sqlite3.connect("gestion_almacen.db")

cur = conexion.cursor()

logging.info('BASE DE DATOS ABIERTA')

try:
    cur.execute("CREATE TABLE almacen(articulos VARCHAR, precio FLOAT, precio_con_iva FLOAT, precio_con_descuento FLOAT)")
    conexion.commit()
    print("Tabla artículos creada ...")
except sqlite3.OperationalError:
    print("Puede continuar...")

# CREAMOS UNA FUNCIÓN AGREGAR
def agregar():
    precio = float(varprecio.get())
    precio_con_iva = precio * 1.21
    precio_con_descuento = precio_con_iva * 0.8
    datos=(vararticulo.get(), precio, precio_con_iva, precio_con_descuento)
    vararticulo.set("")
    varprecio.set("")
    ordeninsercion="INSERT INTO almacen(articulos, precio, precio_con_iva, precio_con_descuento) VALUES (?, ?, ?, ?)"
    cur.execute(ordeninsercion, datos)
    conexion.commit()
    mb.showinfo("Información", "ARTÍCULO REGISTRADO CON IVA Y DESCUENTO")

# CREAMOS UNA VENTANA
ventana1 = Tk()
ventana1.title("Gestión de almacén")
ventana1.geometry("550x200+250+250")

frame1 = Frame(ventana1)
frame1.grid(column=0, row=0, padx=10, pady=10)

titulo=LabelFrame(frame1, text="Alta de Artículo")
titulo.grid(column=0, row=1, padx=4, pady=4)

etiqueta1=Label(titulo, text="articulo: ")
etiqueta1.grid(column=0, row=0, padx=4, pady=4)

vararticulo=StringVar()
cajadetextoarticulo=Entry(titulo, textvariable=vararticulo)
cajadetextoarticulo.grid(column=0, row=1, padx=4, pady=4)

etiqueta2=Label(titulo, text="precio: ")
etiqueta2.grid(column=1, row=0, padx=4, pady=4)

varprecio=StringVar()
cajadetextoprecio=Entry(titulo, textvariable=varprecio)
cajadetextoprecio.grid(column=1, row=1, padx=4, pady=4)

boton1=Button(titulo, text="Confirmar", command=agregar)
boton1.grid(column=3, row=2, padx=4, pady=4)

logging.info('ALTA DE ARTÍCULO')

boton2=Button(titulo, text="SALIR", command=ventana1.destroy)
boton2.grid(column=4, row=2, padx=4, pady=4)

logging.info('CIERRE DE VENTANA')

ventana1.mainloop()
#CERRAMOS LA BASE DE DATOS Y EL LOGGER
conexion.close()
logging.shutdown()