#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

import sqlite3

#2. CREO O ABRO LA BBDD
conexion = sqlite3.connect("articulos.db")
print("Base de Datos creada o abierta...")

#3. CREAMOS EL CURSOR (HERRAMIENTA PARA TRABAJAR DENTRO DE LA BBDD)
cur = conexion.cursor()
print("Cursor creado...")

#4. CREO LAS TABLAS NECESARIAS (EN ESTE CASO UNA DENOMINADA articulos)
try:
    cur.execute("CREATE TABLE articulos(id INTEGER PRIMARY KEY, descripcion VARCHAR, precio FLOAT)")
    conexion.commit()
    print("Tabla artículos creada ...")
except sqlite3.OperationalError:
    print("Puede continuar...")
          
#5. FUNCIÓN AGREGAR ARTÍCULO
def agregar():
    datos=(varid.get(), vardescripcion.get(),  varprecio.get())
    varid.set("")
    vardescripcion.set("")
    varprecio.set("")
    ordeninsercion="INSERT INTO articulos(id, descripcion, precio) VALUES (?, ?, ?)"
    cur.execute(ordeninsercion, datos)
    conexion.commit()
    mb.showinfo("Información", "ARTÍCULO REGISTRADO")

#6. CREO LA VENTANA
ventana1 = Tk()
ventana1.title("RESTAURANTE PACO")
ventana1.geometry("550x200+250+250")

frame1 = Frame(ventana1)
frame1.grid(column=0, row=0, padx=10, pady=10)

titulo=LabelFrame(frame1, text="Alta de Artículo")
titulo.grid(column=0, row=1, padx=4, pady=4)

etiqueta1=Label(titulo, text="ID: ")
etiqueta1.grid(column=0, row=0, padx=4, pady=4)

varid=StringVar()
cajadetextoid=Entry(titulo, textvariable=varid)
cajadetextoid.grid(column=0, row=1, padx=4, pady=4)

etiqueta2=Label(titulo, text="Descripción: ")
etiqueta2.grid(column=1, row=0, padx=4, pady=4)

vardescripcion=StringVar()
cajadetextodescripcion=Entry(titulo, textvariable=vardescripcion)
cajadetextodescripcion.grid(column=1, row=1, padx=4, pady=4)

etiqueta3=Label(titulo, text="Precio: ")
etiqueta3.grid(column=2, row=0, padx=4, pady=4)

varprecio=StringVar()
cajadetextoprecio=Entry(titulo, textvariable=varprecio)
cajadetextoprecio.grid(column=2, row=1, padx=4, pady=4)

boton1=Button(titulo, text="Confirmar", command=agregar)
boton1.grid(column=3, row=2, padx=4, pady=4)

boton2=Button(titulo, text="SALIR", command=ventana1.destroy)
boton2.grid(column=4, row=2, padx=4, pady=4)

ventana1.mainloop()

#7. CIERRO LA BBDD
conexion.close()
print("BBDD cerrada...")
