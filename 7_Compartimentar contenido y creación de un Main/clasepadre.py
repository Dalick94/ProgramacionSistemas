from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.etiquetasaludo = Label(self.frame, text="Estas son las opciones posibles")
        self.etiquetasaludo.pack()
        self.frame.pack()
