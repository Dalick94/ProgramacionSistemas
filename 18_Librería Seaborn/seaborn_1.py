#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
    #PIP INSTALL NUMPY EN CASO QUE NO ESTÉ DESCARGADA YA.
    #PIP INSTALL PANDAS EN CASO QUE NO ESTÉ DESCARGADA YA.
    #PIP INSTALL SEABORN EN CASO QUE NO ESTÉ DESCARGADA YA.
    #PIP INSTALL MATPLOTLIB EN CASO QUE NO ESTÉ DESCARGADA YA.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl #Para mostrar el gráfico y guardarlo en un archivo PNG
import matplotlib.pyplot as plt

#2. INFORMAMOS AL CLIENTE DE LA VERSIÓN DE LAS LIBRERÍAS QUE ESTAMOS UTILIZANDO
print("La versión de la librería Numpy utilizada es: ", np.__version__)
print("La versión de la librería Pandas utilizada es: ", pd.__version__)
print("La versión de la librería Seaborn utilizada es: ", sns.__version__)
print("La versión de la librería XlWings utilizada es: ", xw.__version__) #Para trabajar con excell
print("La versión de la librería MatPlotLib utilizada es: ", mpl.__version__)

#3. CREAMOS O CAPTURAMOS DATOS
media_colesterol_ldl = 100
desviacion_ldl = 7.3
n = 50

print()
muestraldl = np.random.normal(media_colesterol_ldl, desviacion_ldl, n)
print("LAS 50 MUESTRAS ALEATORIAS OBTENIDAS DE LDL SON:")
print(muestraldl)
print()
print("LA MEDIANA ES:")
medianaldl = np.median(muestraldl)
print(medianaldl)

#4. MOSTRAMOS LOS DATOS EN UN OBJETO SEABORN
sns.histplot(muestraldl, kde=True)
sns.rugplot(muestraldl)
plt.show()
