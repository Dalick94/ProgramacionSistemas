#IMPORTAMOS LAS LIBRERÍAS NECESARIAS PARA MANEJAR VENTANAS
from tkinter import *
from tkinter import ttk

#PARA CREAR UNA VENTANA (Tk())
ventana1 = Tk()
ventana2 = Tk()

#PROPIEDADES DEL OBJETO TK

#TÍTULO DE VENTANA
ventana1.title("Ejemplo TK")
ventana2.title("Ejemplo TK")

#DIMENSIONES Y POSICIÓN (ANCHO x ALTO + POSICIÓN EJE X + POSICIÓN EJE Y)
ventana1.geometry("550x550+200+200")
ventana2.geometry("550x550+400+400")

#COLOR DE FONDO
ventana1.configure(bg="yellow")
ventana2.configure(bg="grey")

#TRANSPARENCIA Y OPACIDAD
ventana1.attributes("-alpha",1)
ventana2.attributes("-alpha",1)

'''
#TRANSIENT = TRAER AL FRENTE UNA VENTANA ENTRE VARIAS
#ventana2.transient(ventana1)

ventana1.mainloop()
ventana2.mainloop()
'''

#WITHDRAW : OCULTA UNA VENTANA DADA
ventana1.withdraw()

#ICONIFY Y DEICONIFY: PERMITEN MINIMIZAR (CON PRESENCIA EN BARRA DE TAREAS)Y MOSTRAR VENTANAS EN PANTALLA
ventana2.iconify()

ventana1.deiconify()
ventana2.deiconify()

#MAXSIZE Y MINSIZE: DEFINEN TAMAÑO MÁXIMO Y MÍNIMO DE PANTALLA
ventana1.maxsize(800,800)
ventana1.minsize(300,150)

#RESIZABLE
ventana1.resizable(True, True)

#DESTROY (DESTRUYE TODO EL CONTENIDO, VARIABLES Y VALORES DEL SISTEMA)
#ventana1.destroy()
#ventana2.destroy()





















