#1. IMPORTAMOS LA LIBRERÍA PANDAS
import pandas as pd
import numpy as np
import random

#2. CREACIÓN O CAPTURA DE DATOS ...
datos1 = ([["", "Glucosa en sangre 8:00", "Glucosa en sangre 14:00"],
           ["Paciente 1", 110, 98],
           ["Paciente 2", 110, 91],
           ["Paciente 3", 87, 98]])

datos2 = ([[110, 72, 100],
           [110, 91, 77],
           [87, 98, 135]])

#SI LO TRATO COMO UN ARRAY (NUMPY)
a = np.array(datos1)
print(a)

#SI LO TRATO COMO UNA TABLA DE DATOS (PANDAS)
b = pd.DataFrame(datos1)
print(b)

#3. PARA CREAR UNA SERIE DE DATOS EN PANDAS
#EL EQUIVALENTE A VECTOR EN NUMPY
serie = pd.Series({"Propiedad 1:":"120.000 $", "Propiedad 2:":"135.000$"})
print(serie)

#4. PARA SABER LAS DIMENSIONES DE UNA MATRIZ EN PANDAS
print(b.shape)

#5. LA FUNCIÓN LEN NOS DA LONGITUD DE LA TABLA:
print(len(b.index))

#6. PARA AVERIGUAR LOS VALORES ESTADÍSTICOS DE UNA VEZ:
c = b.describe()
print(c)

#7. PARA AVERIGUAR LA MEDIA DE CADA COLUMNA
d = pd.DataFrame(datos2)
e = d.mean()
print(e)

#8. PARA AVERIGUAR EL VALOR MÁXIMO DE UNA TABLA (DATAFRAME)
f = d.max()
print(f)

#9. PARA AVERIGUAR EL VALOR MÍNIMO DE UNA TABLA (DATAFRAME)
g = d.min()
print(g)

#10. PARA CALCULAR LA CORRELACIÓN DE UNA TABLA DE DATOS (DATAFRAME)
h = d.corr()
print(h)

#11. PARA CALCULAR DESVIACIÓN ESTÁNDAR DE UN DATAFRAME
i = d.std()
print(i)

#12. PARA EXTRAER UNA O VARIAS COLUMNAS
print(d)
print(d[1])
print(d[[1,2]])

#13. PARA EXTRAER UNA O VARIAS FILAS
print(d)
print(d.loc[1])
print(d.loc[[1, 2]])

#14. PARA EXTRAER UN DATO CONCRECO DE UN DATAFRAME
print(d)
print(d.iloc[1][1])

