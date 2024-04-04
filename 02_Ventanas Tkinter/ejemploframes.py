#FRAME = ES UNA CAJA DONDE SITUAR WIDGETS
# ES UN SIMPLE CONTENEDOR
#SIEMPRE CUELGA DE UNA VENTANA


#1. IMPORTAR LIBERÍAS
from tkinter import *
from tkinter import ttk

#2. CREAR VENTANA O VENTANAS
ventana1 = Tk()
ventana1.title("Ejemplo FRAMES 1")
ventana1.geometry("800x800+100+100")
ventana1.resizable(False,False)
ventana1.configure(bg="lightblue")
ventana1.attributes("-alpha",1)

ventana2 = Tk()
ventana2.title("Ejemplo FRAMES 2")
ventana2.geometry("600x600+200+200")
ventana2.resizable(False,False)
ventana2.configure(bg="blue2")
ventana2.attributes("-alpha",0.5)

#3. CREAR FRAME O FRAMES

frame1 = Frame(ventana1)
frame1.configure(width=350, height=350, bg="red", bd=50)
#frame1.config(relief="flat")
#frame1.config(relief="sunken")
#frame1.config(relief="raised")
#frame1.config(relief="groove")
frame1.config(relief="ridge")

frame2 = Frame(ventana1)
frame2.configure(width=200, height=200, bg="green", bd=25)
frame2.config(relief="sunken")

frame2.pack()
frame1.pack()

ventana1.mainloop()

