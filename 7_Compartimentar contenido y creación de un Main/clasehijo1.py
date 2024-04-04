#MANEJO DE CLASES Y VENTANAS

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

from clasepadre import *

#2. CREO LA CLASE
class ventana1(App):
    ventana1=Tk()
    ventana1.title("Ventana 1")
    ventana1.geometry("400x400+250+250")
    appheredado = App(ventana1)
    ventana1.mainloop()
    
