# -*- coding: utf-8 -*-
"""
En este ejemplo vamos a hacer una aplicacion que lea los archivos de nombres más
populares de recien nacidos del INE, accesibles en este link
http://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177009&menu=resultados&secc=1254736195498&idp=1254734710990

En concreto, esta aplicación hará lo siguiente.

- Tomar como argumento un nombre propio
- Leer un conjunto de archivos conteniendo los nombres más populares de niños en España por Año.
  Cada archivo es un archivo con el formato "nomnacXX.csv"
  donde XX es un año del 02 al 16 (2002 a 2016)
- Para el nombre indicado, imprimir cuantos años ha estado entre los nombres más populares

@author: manugarri
"""

import argparse


def parsear_argumentos_avanzado():
    parser = argparse.ArgumentParser(
        description="""Este script calcula el numero de años desde 2002 que el nombre indicado fue de
                    los más populares en España"""
    )

    parser.add_argument("nombre", help="""
                            Nombre que queremos analizar
                        """)

    argumentos = parser.parse_args()
    return argumentos


def cargar_archivo(year):
    with open("data/nomnac{}.csv".format(year)) as fname:
        lineas = fname.readlines()
    nombres_masculinos = []
    nombres_femeninos = []
    for linea_nombres in lineas:
        nombres = linea_nombres.strip().split(",")
        assert len(nombres) == 2
        nombres_masculinos.append(nombres[0])
        nombres_femeninos.append(nombres[1])
    return nombres_masculinos + nombres_femeninos


def calcular_popularidad_por_nombre(nombre_busqueda):
    years_nombre = 0
    for year in ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]:
        nombres_year = cargar_archivo(year)
        if nombre_busqueda in nombres_year:
            years_nombre += 1
    return years_nombre

def main(argumentos):
    """
    Aquí ponemos la funcionalidad principal de nuestro script
    """
    nombre = argumentos.nombre.upper()
    years_nombre = calcular_popularidad_por_nombre(nombre)
    print("El nombre {} está entre los más populares en {} años".format(nombre, years_nombre))



if __name__ == "__main__":
    # Este código solo se ejecutará si ejecutamos este script directamente
    argumentos = parsear_argumentos_avanzado()
    main(argumentos)
