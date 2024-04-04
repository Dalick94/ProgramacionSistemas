#IMPORTO LIBRERÍAS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#FUNCIÓN GUARDAR_DATOS()
def guardardatos():
    codigo1 = cajatexto1.get()
    codigo.set(codigo1)
    nombre1 = cajatexto2.get()
    nombre.set(nombre1)
    apellidos1 = cajatexto3.get()
    apellidos.set(apellidos1)
    departamento1 = cajatexto4.get()
    departamento.set(departamento1)
    with open("empleados.txt","a")as archivo:
        archivo.write(f"{codigo},{nombre},{apellidos},{departamento}\t \n")
        
def borrardatos():
    cajatexto1.delete(0,tk,END)
    cajatexto2.delete(0,tk,END)
    cajatexto3.delete(0,tk,END)
    cajatexto4.delete(0,tk,END)

#CREO VENTANA Y VARIABLES GLOBALES CONTENEDORAS
ventana1 = Tk()
ventana1.title("Registro de empleados")
ventana1.geometry("600x500+300+300")
ventana1.configure(bg="navy")

codigo=StringVar()
nombre=StringVar()
apellidos=StringVar()
departamento=StringVar()

#CONTENIDO DE LA VENTANA

#ETIQUETA TÍTULO
etiqueta0 = Label(ventana1,text="Introduzca datos y seleccione opción:", bg="navy", fg="white", font=("Arial", 14)).grid(row=0, column=0)
#ESPACIO EN BLANCO
etiqueta00 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=1, column=0)
#PRIMERA ETIQUETA (CÓDIGO DE EMPLEADO)
etiqueta1 = Label(ventana1,text="Código empleado: ", font=("Arial", 14)).grid(row=2, column=0)
#ESPACIO EN BLANCO
etiqueta2 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=3, column=0)
#CAJA DE TEXTO DE CÓDIGO EMPLEADO
cajatexto1 = Entry(ventana1, font=("Arial", 14), textvariable=codigo).grid(row=2, column=1)


#SEGUNDA ETIQUETA (NOMBRE DE EMPLEADO)
etiqueta3 = Label(ventana1,text="Nombre empleado: ", font=("Arial", 14)).grid(row=4, column=0)
#ESPACIO EN BLANCO
etiqueta4 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=5, column=0)
#CAJA DE TEXTO DE NOMBRE DE EMPLEADO
cajatexto2 = Entry(ventana1, font=("Arial", 14), textvariable=nombre).grid(row=4, column=1)


#TERCERA ETIQUETA (APELLIDOS DE EMPLEADO)
etiqueta5 = Label(ventana1,text="Apellido empleado: ", font=("Arial", 14)).grid(row=6, column=0)
#ESPACIO EN BLANCO
etiqueta6 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=7, column=0)
#CAJA DE TEXTO DE APELLIDO DE EMPLEADO
cajatexto3 = Entry(ventana1, font=("Arial", 14), textvariable=apellidos).grid(row=6, column=1)


#CUARTA ETIQUETA (DEPARTAMENTO)
etiqueta6 = Label(ventana1,text="Departamento: ", font=("Arial", 14)).grid(row=8, column=0)
#ESPACIO EN BLANCO
etiqueta7 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=9, column=0)
#CAJA DE TEXTO DE APELLIDO DE EMPLEADO
cajatexto4 = Entry(ventana1, font=("Arial", 14), textvariable=departamento).grid(row=8, column=1)


#BOTON GUARDAR
botonguardar = Button(ventana1, text="Guardar", font=("Arial", 10), command=lambda:guardardatos)
botonguardar.grid(row=10, column=0)

#BOTON BORRAR CONTENIDO
botonlimpiar = Button(ventana1, text="Borrar", font=("Arial", 10), command=borrardatos)
botonlimpiar.grid(row=10, column=1)

#ESPACIO EN BLANCO
etiqueta8 = Label(ventana1,text="", bg="navy", font=("Arial", 14)).grid(row=11, column=0)

#BOTON CONSULTAR
botonconsultar = Button(ventana1, text="Consultar", font=("Arial", 10))#, command=consultar_datos)
botonconsultar.grid(row=12, column=0)

#BOTON SALIR
botonsalir = Button(ventana1, text="Salir", font=("Arial", 10))#, command=salir)
botonsalir.grid(row=12, column=1)


















#EJECUTAMOS LA VENTANA
ventana1.mainloop()
