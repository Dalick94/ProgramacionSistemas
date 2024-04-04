#WIDGET = ES UN COMPONENTE QUE VA DENTRO UNA CAJA (FRAME)
#LES HABRÁ CON EJECUCIÓN DE COMANDOS O NO...
#SIEMPRE CUELGA DE UNA VENTANA O DE UN FRAME

listaprovincias = ["León", "Salamanca", "Burgos", "Segovia"]

#1. IMPORTAR LIBERÍAS
from tkinter import *
from tkinter import ttk

vara = ""


#2. CREAR VENTANA O VENTANAS
ventana1 = Tk()
ventana1.title("Ejemplo WIDGETS")
ventana1.geometry("800x800+100+100")
ventana1.resizable(False,False)
ventana1.configure(bg="lightblue")
ventana1.attributes("-alpha",1)

#3. CREAR FRAME
frame1 = Frame(ventana1)
frame1.configure(width=350, height=350, bg="blue3", bd=10)
frame1.config(relief="ridge")
frame1.pack()

#4. CREAR WIDGETS
    # 4A. ETIQUETAS
etiqueta = Label(frame1, text="Introduzca su Nombre:", bg="green", fg="yellow", font=("Courier", 16), anchor="center")
etiqueta.pack()

    # 4B. ENTRY (CAJAS DE TEXTO)
cajadetexto = Entry(frame1, width=10, state="normal") #textvariable(vara))
cajadetexto.pack()

    # 4C. BOTONES (LA PIEDRA ANGULAR DE TODA VENTANA, EJECUTA COMANDOS)

boton = Button(frame1, text="Pulsar aquí para ejecutar", bg="red", state="disabled") #command=calcularareatriangulo())
boton.pack()

    # 4D. LISTAS DESPLEGABLES
listadesplegable = Listbox(frame1)
listadesplegable.insert(0, *listaprovincias)

#listadesplegable.insert(0, "Galicia")
#listadesplegable.insert(1, "Asturias")
#listadesplegable.insert(2, "Cantabria")
#listadesplegable.insert(3, "Euskadi")
#listadesplegable.insert(4, "Navarra")
listadesplegable.pack()

etiqueta2 = Label(frame1, text=listadesplegable.get(2), bg="green", fg="yellow", font=("Courier", 16))
etiqueta2.pack()

listadesplegable.delete(2)

etiqueta3 = Label(frame1, text=listadesplegable.get(2), bg="green", fg="yellow", font=("Courier", 16))
etiqueta3.pack()

etiqueta4 = Label(frame1, text="", bg="green", fg="yellow", font=("Courier", 16))
etiqueta4.pack()

#etiqueta4.text(set("Ejemplo"))
#etiqueta4.pack()

    # 4E. CHECKBUTTON
botoncheck = Checkbutton(frame1, text="Opción 1")
botoncheck.invoke()
botoncheck.pack()


opcion1 = IntVar()
opcion2 = IntVar()
    # 4F. RADIOBUTTON
botonradio1 = Radiobutton(frame1, text="Opción 1", variable=opcion1, value=1)
botonradio2 = Radiobutton(frame1, text="Opción 2", variable=opcion1, value=2)
botonradio3 = Radiobutton(frame1, text="Opción 3", variable=opcion2, value=3)
botonradio4 = Radiobutton(frame1, text="Opción 4", variable=opcion2, value=4)

botonradio1.pack()
botonradio2.pack()
botonradio3.pack()
botonradio4.pack()


























ventana1.mainloop()

