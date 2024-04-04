#MANEJO DE CLASES Y VENTANAS

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

from importaciones import *

#2. CREO LA CLASE
class ventana1(App):
    ventana1=Tk()
    ventana1.title("Ventana 1")
    ventana1.geometry("400x400+250+250")
    appheredado = App(ventana1)
    #ventana1.mainloop()

class ventana2(App):
    ventana2=Tk()
    ventana2.title("Ventana 2")
    ventana2.geometry("400x400+250+250")
    appheredado = App(ventana2)
    #ventana2.mainloop()

class ventana3(App):
    ventana2=Tk()
    ventana2.title("Ventana 3")
    ventana2.geometry("400x400+250+250")
    appheredado = App(ventana2)
    ventana2.mainloop()

app1 = ventana1
app2 = ventana2
app3 = ventana3
    
