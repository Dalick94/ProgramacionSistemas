#1. IMPORTACIÓN DE LIBRERÍAS QUE NECESITEMOS
from tkinter import *
from tkinter import ttk

#2. CREAMOS VENTANA
ventana3=Tk()
ventana3.geometry("600x600+400+500")

etiqueta1=Label(ventana3, text="ESTA ES LA VENTANA 3")
etiqueta1.pack()

boton1=Button(ventana3, text="SALIR", command=ventana3.destroy)
boton1.pack()

ventana3.mainloop()
