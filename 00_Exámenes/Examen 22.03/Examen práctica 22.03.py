# Importar las librerías necesarias
import tkinter as tk
import pygame
import time
import sqlite3
import pandas as pd

# Crear la ventana estática (Tkinter).
root = tk.Tk()
root.title("Dimensiones de los objetos")
root.geometry("400x300")

# Crear variables para almacenar las dimensiones de los objetos
linea_dim = tk.StringVar()
rectangulo_dim = tk.StringVar()
circulo_dim = tk.StringVar()
elipse_dim = tk.StringVar()

# Función para guardar los datos en la base de datos
def guardar_datos():
    conn = sqlite3.connect('poligonos.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS poligonos (objeto text, dimensiones text)')
    c.execute('INSERT INTO poligonos VALUES (?, ?)', ('Linea', linea_dim.get()))
    c.execute('INSERT INTO poligonos VALUES (?, ?)', ('Rectangulo', rectangulo_dim.get()))
    c.execute('INSERT INTO poligonos VALUES (?, ?)', ('Circulo', circulo_dim.get()))
    c.execute('INSERT INTO poligonos VALUES (?, ?)', ('Elipse', elipse_dim.get()))
    conn.commit()
    conn.close()

# Función para exportar a Excel
def exportar_excel():
    conn = sqlite3.connect('poligonos.db')
    df = pd.read_sql_query("SELECT * FROM poligonos", conn)
    df.to_excel("dimensiones_poligonos.xlsx", index=False)
    conn.close()

# Función para salir y cerrar las variables intermedias y la ventana.
def salir():
    root.destroy()

# Crear etiquetas y campos de entrada para cada objeto
tk.Label(root, text="Línea (Inicio, Fin):").pack()
tk.Entry(root, textvariable=linea_dim).pack()

tk.Label(root, text="Rectángulo (Ancho, Alto):").pack()
tk.Entry(root, textvariable=rectangulo_dim).pack()

tk.Label(root, text="Círculo (Radio):").pack()
tk.Entry(root, textvariable=circulo_dim).pack()

tk.Label(root, text="Elipse (Semieje Mayor, Semieje Menor):").pack()
tk.Entry(root, textvariable=elipse_dim).pack()

# Botón para guardar los datos y exportar a Excel
tk.Button(root, text="Guardar Datos", command=guardar_datos).pack()
tk.Button(root, text="Exportar a Excel", command=exportar_excel).pack()
tk.Button(root, text="SALIR", command=salir).pack()

root.mainloop()

# Crear la ventana dinámica (Pygame)
def iniciar_ventana():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Objetos")
    return screen

# Representar los objetos con delay
def representar_objetos(screen):
    conn = sqlite3.connect('poligonos.db')
    c = conn.cursor()

    c.execute("SELECT * FROM poligonos WHERE objeto=?", ('Linea',))
    linea = c.fetchone()[1].split(",")
    pygame.draw.line(screen, (255, 0, 0), (int(linea[0]), int(linea[1])), (int(linea[2]), int(linea[3])), 5)
    pygame.display.flip()
    time.sleep(3)

    c.execute("SELECT * FROM poligonos WHERE objeto=?", ('Rectangulo',))
    rectangulo = c.fetchone()[1].split(",")
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(int(rectangulo[0]), int(rectangulo[1]), int(rectangulo[2]), int(rectangulo[3])))
    pygame.display.flip()
    time.sleep(3)

    c.execute("SELECT * FROM poligonos WHERE objeto=?", ('Circulo',))
    circulo = c.fetchone()[1]
    pygame.draw.circle(screen, (0, 0, 255), (500, 200), int(circulo))
    pygame.display.flip()
    time.sleep(3)

    c.execute("SELECT * FROM poligonos WHERE objeto=?", ('Elipse',))
    elipse = c.fetchone()[1].split(",")
    pygame.draw.ellipse(screen, (255, 255, 0), pygame.Rect(int(elipse[0]), int(elipse[1]), int(elipse[2]), int(elipse[3])))
    pygame.display.flip()
    time.sleep(3)

screen = iniciar_ventana()
representar_objetos(screen)

# Mantener la ventana abierta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
