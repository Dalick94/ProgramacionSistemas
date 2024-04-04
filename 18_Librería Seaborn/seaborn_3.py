#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

#2. IMPORTAMOS DATOS O LOS CREAMOS
datos_aleatorios = np.random.RandomState()
ejex = datos_aleatorios.normal(3, 7, size = 1000)

#3. VISIONAMOS EL PRIMER RESULTADO (ESTÁDAR EN EL EJE X)
sns.histplot(x = ejex, kde = True)
plt.show()

#4. VISIONAMOS EN EL EJE Y
sns.histplot(y = ejex, kde = True)
plt.show()

#5. PARA MANEJAR EL ANCHO DE BARRAS
sns.histplot(x = ejex, kde = True, shrink = 0.5)
plt.show()

#6. FORMA DE VISIONADO (POR DEFECTO ES 'BARS')
sns.histplot(x = ejex, kde = True, element = "bars")
plt.show()

sns.histplot(x = ejex, kde = True, element = "step")
plt.show()

sns.histplot(x = ejex, kde = True, element = "poly")
plt.show()

#7. EL ATRIBUTO STAT() CONTROLA EL NÚMERO DE OBSERVACIONES
sns.histplot(x = ejex, kde = True, stat = "density")
plt.show()

sns.histplot(x = ejex, kde = True, stat = "frequency")
plt.show()

sns.histplot(x = ejex, kde = True, stat = "percent")
plt.show()

#8. PARA CAMBIAR LA ESTÉTICA DEL GRÁFICO
sns.histplot(x = ejex, kde = True, color = "red", alpha = 0.5, fill = False)
plt.show()

