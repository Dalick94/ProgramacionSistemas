#1. CREAR UNA CLASE
#UNA CLASE ENGLOBA TANTO FUNCIONES COMO VARIABLES COMO ÓRDENES
class miprimeraclase:
    #2. INTODUCIMOS EL CONCEPTO DE ÁMBITO
    def funcionlocal():
        mensaje = "SOY UNA VARIABLE LOCAL, SÓLO PARA ESTA FUNCIÓN..."
        print(mensaje)
        
    #def funcionnolocal():
    #    nonlocal mensaje1
    #    mensaje1 = "MODIFICACIÓN..."
    #   print(mensaje1)
        
    def funcionglobal():
        global mensaje2
        mensaje2="SOY UNA VARIABLE GLOBAL Y ME PUEDEN LLAMAR DESDE FUERA DE LA CLASE..."
        print(mensaje2)

#2. LA EJECUCIÓN SECUENCIAL DE ÓRDENES COMIENZA AQUÍ  
primerobjeto = miprimeraclase
#primerobjeto.funcionlocal()
#primerobjeto.funcionnolocal()
primerobjeto.funcionglobal()
#print(mensaje)
print(mensaje2)
mensaje2="GLOBAL MODIFICADO..."
print(mensaje2)
