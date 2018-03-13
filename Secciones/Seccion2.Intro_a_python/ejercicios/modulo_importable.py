# -*- coding: utf-8 -*-
"""
Aquí se puede poner código que se importa desde otros scripts (o la terminal de python!) 

Cuando un script se hace muy largo, es conveniente el agrupar distintos trozos
de la lógica en distintos archivos (módulos)

@author: manugarri
"""


def saludar_modulo(nombre):
    print("Hola {}, esta función se ha importado del módulo {}, {}".format(nombre, __file__, __name__))
    

def felicitar_modulo(nombre):
    print("¡Felicidades {}!".format(nombre))
    
def main():
    saludar_modulo("Tú")    
    
if __name__ == "__main__":
    main()