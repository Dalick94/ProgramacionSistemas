#1. IMPORTACIÓN DE LIBRERÍAS QUE NECESITEMOS
from tkinter import *
from tkinter import ttk

#2. CREAMOS VENTANA
ventana2=Tk()
ventana2.geometry("400x400+300+300")

etiqueta1=Label(ventana2, text="ESTA ES LA VENTANA 2")
etiqueta1.pack()

boton1=Button(ventana2, text="SALIR", command=ventana2.destroy)
boton1.pack()

ventana2.mainloop()
