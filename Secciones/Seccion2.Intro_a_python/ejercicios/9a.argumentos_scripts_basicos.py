# -*- coding: utf-8 -*-
"""
Aquí se explica como añadir funcionalidad a los scripts

@author: manugarri
"""
# los imports se añaden al principio en un script
import sys
from modulo_importable import saludar_modulo


def parsear_argumentos_basico():
    argumentos = sys.argv[1:]
    return argumentos


def main(argumentos):
    """
    Aquí ponemos la funcionalidad principal de nuestro script
    """
    if argumentos[0] == "saludar":
        nombre = argumentos[1]
        saludar_modulo(nombre)
    
if __name__ == "__main__":
    # Este código solo se ejecutará si ejecutamos este script directamente
    
    argumentos = parsear_argumentos_basico()
    print("argumentos pasados al script: ", argumentos)
    main(argumentos)