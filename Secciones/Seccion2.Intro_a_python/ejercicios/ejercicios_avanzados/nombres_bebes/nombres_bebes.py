# -*- coding: utf-8 -*-
"""
En este ejemplo vamos a hacer una aplicacion que lea los archivos de nombres más
populares de recien nacidos del INE, accesibles en este link
http://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177009&menu=resultados&secc=1254736195498&idp=1254734710990

En concreto, esta aplicación hará lo siguiente.

- Tomar como argumento un nombre propio, por ejemplo "python nombres_bebes manuel"
- Leer un conjunto de archivos conteniendo los nombres más populares de niños en España por Año.
  Cada archivo es un archivo con el formato "nomnacXX.csv"
  donde XX es un año del 02 al 16 (2002 a 2016)
- Para el nombre indicado, imprimir cuantos años ha estado entre los nombres más populares

@author: manugarri
"""
