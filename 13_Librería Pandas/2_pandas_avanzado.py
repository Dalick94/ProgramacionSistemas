#1. IMPORTAMOS LA LIBRERÍA PANDAS
import pandas as pd

#2. PARA IMPORTAR LOS DATOS DESDE UN CSV A UN DATAFRAME (PANDAS):
#EL FORMATO CSV SÓLO PERMITE TRABAJAR A UNA HOJA POR ARCHIVO.
#SE DETECTA CIERTAS INCOMPATIBILIDADES CON CSV REALIZADO EN EXCEL
#SÓLO PERMITE UNA HOJA, AUNQUE VARIAS COLUMNAS.
datos = pd.read_csv('prueba2_csv.csv')

a = pd.DataFrame(datos)

print("La importación del archivo CSV ha sido exitosa:")

print(a)

print()

print(a['Nombre'])
print()

print(a['Apellido 1'])
print()

print(a['Apellido 2'])
print()

#3. PARA IMPORTAR ARCHIVOS EXCEL
#PERMITE ACCESO A XLS O XLSX
#PERMITE ACCESO A VARIAS HOJAS DE UN LIBRO EXCEL (SHEET_NAME)
#OJO AL ATRIBUTO HEADER (POR DEFECTO ES YES).

datos2 = pd.read_excel('ejemplo_excel.xlsx')
b = pd.DataFrame(datos2)
print("La importación del archivo EXCEL ha sido exitosa:")
print(b)
print()

print(b['Nombre'])
print()

datos3 = pd.read_excel('ejemplo_excel.xlsx', sheet_name='propiedades')
c = pd.DataFrame(datos3)
print("La importación del archivo EXCEL ha sido exitosa:")
print(c)
print()

print(c['Ubicación'])
print()


