#1. IMPORTACIÓN DE LIBRERÍAS QUE NECESITEMOS
from tkinter import *
from tkinter import ttk

import os

#2. FUNCIONES CREADAS
def abrirventana2():
    os.system('ventana2.py')

def abrirventana3():
    os.system('ventana3.py')
    
#3. CREAMOS VENTANA
ventana1=Tk()

boton1=Button(ventana1, text="Ir a la ventana 2", command=abrirventana2)
boton1.pack()

boton2=Button(ventana1, text="Ir a la ventana 3", command=abrirventana3)
boton2.pack()

ventana1.mainloop()
