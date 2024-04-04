#VENTANAS GRÁFICAS

#1. LIBRERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

#2. ¿CÓMO CREAR UNA VENTANA?
ventana = Tk()

#3. UN FRAME ES UNA TABLA DONDE IR COLOCANDO OBJETOS POR COLUMNAS
formulario = ttk.Frame(ventana, padding=10)
formulario.grid()

#4. ETIQUETAS
ttk.Label(formulario, text="Hello World!").grid(column=0, row=0)

#5. BOTONES Y ACCIÓN A EJECUTAR AL HACER CLICK
ttk.Button(formulario, text="Quit", command=ventana.destroy).grid(column=1, row=0)
ventana.mainloop()
