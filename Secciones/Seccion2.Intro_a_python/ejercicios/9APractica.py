#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script se utiliza para hacer una prueba

@author: erdvillegas
"""

import sys
from modulo_importable import saludar_modulo,felicitar_modulo

def parserar_argumentos_basico():
    argumentos = sys.argv[1:]
    return argumentos

def main(argumentos):
    """
    Esto es la funcion principal del script"
    """
    if(argumentos[0] == "saludar"):
        nombre = argumentos[1]
        saludar_modulo(nombre)
    elif (argumentos[0] == "felicitar"):
        nombre = argumentos[1]
        felicitar_modulo(nombre)
        
        
if __name__ == "__main__":
    argumentos = parserar_argumentos_basico()
    print("argumentos pasados al script: ",argumentos)
    main(argumentos)