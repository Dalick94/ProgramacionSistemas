#TRATAMIENTO DE IMÁGENES EN TKINTER

#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

import os
from PIL import ImageTk, ImageColor, Image

#2. CREO LA VENTANA
ventana1 = Tk()

imagen = ImageTk.PhotoImage(Image.open("imagen.jpg"))

etiqueta1 = Label(ventana1, image=imagen)

etiqueta1.pack()

ventana1.mainloop()


