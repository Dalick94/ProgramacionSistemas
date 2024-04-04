#MANEJO DE CLASES Y VENTANAS

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

from clasepadre import *

#2. CREO LA CLASE
class ventana2(App):
    ventana2=Tk()
    ventana2.title("Ventana 2")
    ventana2.geometry("400x400+250+250")
    appheredado = App(ventana2)
    ventana2.mainloop()


    
