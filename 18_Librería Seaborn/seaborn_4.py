#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

#2. IMPORTAMOS DATOS O LOS CREAMOS
datos = sns.load_dataset("tips")

datos_2 = []

datos_aleatorios = np.random.RandomState()
ejex = datos_aleatorios.normal(3, 7, size = 1000)

#3. PARA DARLE GRID
sns.set_style("whitegrid")
sns.histplot(x = ejex, kde=True, color = "red", alpha = 0.5)
plt.show()

# GRID EN PANELES
sns.set_style("darkgrid")
sns.histplot(x = ejex, kde=True, color = "red", alpha = 0.5)
plt.show()

# COLOR DEL GRID
sns.set_style("whitegrid", {'grid.color': 'red'})
sns.histplot(x = ejex, kde=True, color = "red", alpha = 0.5)
plt.show()

# ESTILO DEL GRID
sns.set_style("whitegrid", {'grid.color': 'red', 'grid.linestyle': '-.'})
sns.histplot(x = ejex, kde=True, color = "red", alpha = 0.5)
plt.show()

#4. DIFERENTES GRÁFICOS
    #HISTROGRAMA 2D
sns.histplot(x = "total_bill", y = "tip", data = datos).set_title("MODA DE COSTE Y PERSONAS")
plt.show()

    #REPRESENTACIÓN POR PUNTOS
sns.scatterplot(x = "total_bill", y = "tip", data = datos).set_title("MODA DE COSTE Y PERSONAS")
plt.show()

    #DIAGRAMA DE PARES(SIN CORRELACIÓN ES KDE, CON CORRELACIÓN ES REG)
sns.pairplot(datos, kind ="kde")
plt.show()

sns.pairplot(datos, kind ="reg")
plt.show()

    #MAPA DE CALOR
np.random.seed(1)
datos2 = np.random.rand(10, 10)
sns.heatmap(datos2, annot = True)
plt.show()

    #DIAGRAMA DE CAJAS
sns.boxplot(x = "day", y = "total_bill", data = datos, palette = 'rainbow')
plt.show()

    #DIAGRAMA DE VIOLINES
sns.violinplot(x = "day", y = "total_bill", data = datos, palette = 'rainbow')
plt.show()

    #GRÁFICO DE ENJAMBRE
np.random.seed(8)
x = np.random.normal(0,1,1000)
y = 3 * x + 5 * np.random.normal(0,1,1000)
figura, ax = plt.subplots()
ax.hexbin(x = x, y = y, bins = "log")
plt.show()

#5. GRÁFICOS 3D
np.random.seed(1000)

x = np.random.normal(size=200)
y = np.random.normal(size=200)
z = np.random.normal(size=200)

figura3d = plt.figure()

ax = figura3d.add_subplot(projection = '3d')
ax.scatter3D(x,y,z)
ax.set_xlabel("EDAD DEL PACIENTE")
ax.set_ylabel("PESO DEL PACIENTE")
ax.set_zlabel("COLESTEROL DEL PACIENTE")

plt.title("ANÁLISIS DE COLESTEROL EN FUNCIÓN EDAD Y PESO")
plt.show()

#EJEMPLO DE 3D EN ESPECTRAL
x1, y1 = np.meshgrid(np.linspace(-8,8),
                 np.linspace(-8,8))
a = np.sqrt(x1**2 + y1**2)
z1 = np.sin(a) / a

figura3d1 = plt.figure()

ax = figura3d1.add_subplot(projection = '3d')
ax.plot_surface(x1, y1, z1, cmap = 'Spectral_r')
plt.show()

