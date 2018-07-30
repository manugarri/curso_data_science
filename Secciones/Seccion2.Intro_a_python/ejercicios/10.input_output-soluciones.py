# -*- coding: utf-8 -*-
"""
Aquí se explica como leer y escribir archivos

EJERCICIOS

"""
#%%
"""
Hacer una función que dado el nombre de un archivo, lo lea y devuelva la linea
con la mayor longitud

"""

def linea_mas_larga(nombre):
    with open(nombre) as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
    linea_mas_larga = lineas[0]
    for linea in lineas:
        if len(linea) > len(linea_mas_larga):
            linea_mas_larga = linea
    return linea_mas_larga
#%%
"""
Hacer una función que tenga como argumento un nombre de un archivo y un
número n y devuelva las n ultimas lineas
"""

def leer_n_ultimas(nombre, n):
    with open(nombre, "r") as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
    return lineas[-n:]

#%%
"""
Hacer una función que dado un  diccionario cree un archivo csv (el nombre tiene
que acabar en .csv)  con los datos del mismo:

Los archivos csv (Comma-Separated-Values) son una forma de almacenar datos con
cada columna separada por una coma

Por ejemplo si tenemos el diccionario:
{
"nombre": ["Antonio", "Miguel", "Julian", "Andres"],
"edad": [45, 40, 22, 34],
"ciudad": ["Murcia", "Almería", "Barcelona", "Madrid"]
}

Dicho diccionario convertido a csv tendria el formato:

    nombre,edad,ciudad
    Antonio,45,Murcia
    Miguel,40,Almería,
    ...

"""

datos = {
"nombre": ["Antonio", "Miguel", "Julian", "Andres"],
"edad": [45, 40, 22, 34],
"ciudad": ["Murcia", "Almería", "Barcelona", "Madrid"]
}

def dict_a_csv(datos, nombre):
    claves = list(datos.keys())
    n_items = len(datos[claves[0]])
    with open(nombre, "w") as fname:
        fname.write(','.join(datos.keys()))
        fname.write("\n")
        for i in range(n_items):
            fila = ",".join([str(datos[clave][i]) for clave in claves])
            fname.write(fila)
            fname.write("\n")

dict_a_csv(datos, "data/nombres/nombres.csv")
