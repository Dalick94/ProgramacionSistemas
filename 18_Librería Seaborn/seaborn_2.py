#1. IMPORTAMOS LA LIBRERÍA NECESARIA
import seaborn as sns

#2. PARA IMPORTAR DATOS EXTERNOS
datos = sns.load_dataset('tips')
print(datos)

#3. PARA SABER EL TIPO DE DATOS IMPORTADOS
print(datos.dtypes)

#4. PARA QUE MUESTRE LA CONSOLA LOS 5 PRIMEROS REGISTROS (CABECERA)
#Si no le decimos nada nos muestra los 5 primeros. 
#Si le damos valor, muestra el valor que le demos.
print(datos.head())

#5. BREVE RESUMEN ESTADÍSTICO DE LAS COLUMMNAS NUMÉRICAS
print(datos.describe())

