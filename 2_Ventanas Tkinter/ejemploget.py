#1. IMPORTAMOS LIBRERÍAS NECESARIAS

from tkinter import *
from tkinter import ttk

def aceptar():
    try:
        n = int(var_texto.get())
    except ValueError:
        var_lbl.set("El número escogido no es válido")
        #var.set(f"El número escogido no es válido")
        #AÑADIR LIMPIADO DE CAJA DE TEXTO
    else: 
        var_lbl.set(f"Escogiste el número: {n}")

#2. CREAMOS UNA VENTANA

ventana = Tk()

var_texto = StringVar()
var_lbl = StringVar()

#3. SIN UTILIZAR FRAMES Y DEMÁS ADORNOS, METEMOS UNA CAJA DE TEXTO

etiqueta = Label(ventana, textvariable=var_lbl)
var_lbl.set("Hola. Escoge y escribe un número...")
#OJO, ESTO ES UN ERROR MUY COMÚN!!!!!!!!
#etiqueta(text("Hola, es la pantalla inicial")
etiqueta.grid(row=0, column=0, columnspan=4)

cajatexto = Entry(ventana, textvariable=var_texto)
cajatexto.grid(row=1, column=0, columnspan=2)

boton = Button(ventana, text="Aceptar", command=aceptar)
boton.grid(row=1, column=2)

ventana.mainloop()

