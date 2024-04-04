#POLIMORFISMO Y HERENCIA

#1. CREO LA CLASE
class Poligono:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Rectangulo(Poligono):
    
    def calculararea(self):
        return self.a * self.b

class Triangulo(Poligono):

    def calculararea(self):
        return (self.a * self.b) / 2

rectangulo1 = Rectangulo(30, 5)

triangulo1 = Triangulo(10, 5)


print("El área del Rectángulo es: ", rectangulo1.calculararea())

print("El área del Triángulo es: ", triangulo1.calculararea())
