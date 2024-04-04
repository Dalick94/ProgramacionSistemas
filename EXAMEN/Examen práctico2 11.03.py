#IMPORTAMOS LAS BIBLIOTECAS NECESARIAS
from tkinter import *
from tkinter import ttk

#DEFINIMOS LAS FUNCIONES (REGISTRAR Y SALIR)
def registrar():
    ID = cajadetexto1.get()
    ARTÍCULO = cajadetexto2.get()
    FAMILIA = cajadetexto3.get()
    MATRÍCULA = cajadetexto4.get()
    
    with open("datos2.txt", "a") as file:
        file.write(f"id: {ID}, Artículo: {ARTÍCULO}, Familia: {FAMILIA}, Matrícula: {MATRÍCULA}\n")

def salir():
    ventana1.destroy()

#CREAMOS LA VENTANA Y SUS PROPIEDADES (VENTANA 2)
ventana1 = Tk()
ventana1.title("Ventana 2")
ventana1.geometry("550x550+200+200")
ventana1.resizable(False,False)
ventana1.configure(bg="lightblue")
ventana1.attributes("-alpha",1)

#CREAMOS FRAME
frame1 = Frame(ventana1)
frame1.configure(width=350, height=350, bg="blue3", bd=10)
frame1.config(relief="ridge")
frame1.pack()

#CREAMOS LAS ETIQUETAS (ID, ARTÍCULO, FAMILIA Y MATRÍCULA)
etiqueta1 = Label(frame1, text="ID:", bg="green", fg="yellow", font=("Courier", 16), anchor="center")
etiqueta1.pack()

cajadetexto1 = Entry(frame1, width=10, state="normal") 
cajadetexto1.pack()

etiqueta2 = Label(frame1, text="ARTÍCULO:", bg="green", fg="yellow", font=("Courier", 16), anchor="center")
etiqueta2.pack()

cajadetexto2 = Entry(frame1, width=10, state="normal") 
cajadetexto2.pack()


etiqueta3 = Label(frame1, text="FAMILIA:", bg="green", fg="yellow", font=("Courier", 16), anchor="center")
etiqueta3.pack()

cajadetexto3 = Entry(frame1, width=10, state="normal") 
cajadetexto3.pack()

etiqueta4 = Label(frame1, text="MATRÍCULA:", bg="green", fg="yellow", font=("Courier", 16), anchor="center")
etiqueta4.pack()

cajadetexto4 = Entry(frame1, width=10, state="normal") 
cajadetexto4.pack()

#CREAMOS LOS BOTONES (REGISTRAR Y SALIR)
boton1 = Button(frame1, text="REGISTRAR", bg="red", command=registrar) 
boton1.pack()

boton2 = Button(frame1, text="SALIR", bg="red", command=salir) 
boton2.pack()

ventana1.mainloop()
