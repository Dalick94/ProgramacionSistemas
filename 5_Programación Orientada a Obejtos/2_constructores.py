#CONSTRUCTORES (TAMBIÉN LLAMADOS INICIALIZADORES)
#LA SINTAXIS ES SIEMPRE (__init__)


#1. CREO LA CLASE
class alumno:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, {self.nombre}")

alumno1 = alumno("Pablo")
alumno1.saludar()

alumno2 = alumno("Pepe")
alumno2.saludar()





alumno.saludar()
