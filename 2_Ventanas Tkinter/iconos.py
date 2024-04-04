#USO DE ARCHIVOS .ICO

#LOS ICONOS DE VENTANA DEBEN CUMPLIR DOS REQUISITOS:
#A. DEBE MEDIR COMO MÁXIMO 16 X 16 PÍXELES.
#B. DEBE SER UN ARCHIVO CON FORMSTO (.ICO)

#1. IMPORTAMOS LAS LIBERÍAS NECESARIAS
from tkinter import *
from tkinter import ttk

import os

#2. CREAMOS UNA VENTANA
ventana1=Tk()
ventana1.title("CONFIGURADOR VOLKSWAGEN")
ventana1.geometry("450x450+300+300")
ventana1.resizable(False, False)
ventana1.iconbitmap("logovw.ico")

ventana1.mainloop()
