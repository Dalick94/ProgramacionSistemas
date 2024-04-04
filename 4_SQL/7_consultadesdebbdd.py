#1. IMPORTAR LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

import sqlite3

#2. CREO O ABRO LA BBDD
conexion=sqlite3.connect("articulos.db")
print("BASE DE DATOS ABIERTA...")

#3. CREO EL CURSOR
cur=conexion.cursor()
print("CURSOR CREADO...")

#4. FUNCIONES NECESARIAS
def listar():
    ordenconsulta1="SELECT id, descripcion, precio FROM articulos"
    #ordenconsulta2="SELECT * FROM articulos"
    cur.execute(ordenconsulta1)
    return cur.fetchall()

#5. CREO LA VENTANA
ventana1=Tk()
ventana1.title("Listado de artículos")
ventana1.geometry("550x650+200+200")
ventana1.resizable(False,False)

frame1=Frame(ventana1)
frame1.grid(column=0, row=0, padx=5, pady=10)

titulo=LabelFrame(frame1, text="Listado")
titulo.grid(column=0, row=1, padx=5, pady=10)


etiqueta1=Label(titulo, text="Los artículos registrados son:")
etiqueta1.grid(column=0, row=2, padx=5, pady=10)

listatexto1=st.ScrolledText(titulo, width=40, height=30)
#OPCIONAL: scrollx=True or False, scrolly=True OR False
listatexto1.grid(column=0, row=3, padx=5, pady=10)
respuesta=listar()
listatexto1.delete("1.0", END)
for fila in respuesta:
    listatexto1.insert(END, "ID: "+str(fila[0])+"\n Descripción: "+str(fila[1])+"\n Precio: "+str(fila[2])+"\n\n")

boton1=Button(titulo, text="SALIR", command=ventana1.destroy)
boton1.grid(column=1, row=4, padx=5, pady=10)

ventana1.mainloop()

#6. CERRAMOS LA BBDD
conexion.close()
print("BBDD CERRADA...")













