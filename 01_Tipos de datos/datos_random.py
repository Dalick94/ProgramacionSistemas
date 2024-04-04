#TIPO DE DATOS RANDOM (ALEATORIOS)

import random

#SI QUEREMOS QUE EL SISTEMA ME DE UN ENTERO ALEATORIO
print("ALEATORIO ENTERO: ",random.randint(10,20))

#SI QUEREMOS QUE EL SISTEMA ME DE UN FLOAT ALEATORIO
print("ALEATORIO FLOTANTE ENTRE 0 Y 1: ",random.random())

#ALEtorios entre un valor y otro y con paso
print("RANGO Y PASO: ",random.randrange(0,20,2))

#CHOICE()
#ELIGE ENTRE LOS VALORES FACILITADOS
print("CHOICE: ",random.choice((-1, 0, 20, 150)))
