# -*- coding: utf-8 -*-
"""
Aquí se explica como leer y escribir archivos

@author: manugarri
"""

#%%

"""
******************************************************************************
CREACION DE CARPETAS
******************************************************************************
"""

# podemos crear directorios con os.makedirs()
import os
os.makedirs("./data/nombres/", exist_ok=True)
#%%
"""
******************************************************************************
LISTADO DE ARCHIVOS
******************************************************************************
"""
archivos_carpeta_actual = os.listdir(".")
print(archivos_carpeta_actual)


#%%
"""
*******************************************************************************
ESCRITURA DE ARCHIVOS
*******************************************************************************
"""
#%%
# Podemos usar open para abrir archivos. Si el archivo no existe, dará un error 
archivo_inexistente = open("./data/nombres/usuarios.txt")

#%%
# Si queremos crear un archivo para escribir, debemos especificar el método de escritura "w"
archivo_para_escribir = open("./data/nombres/usuarios.txt", "w")
archivo_para_escribir.write("hola")
archivo_para_escribir.write(" Mundo!")
#%%
# no se escribe nada hasta que no cerramos el archivo
archivo_para_escribir.close()
#%%
# Si usamos el método "w" de escritura sobreescribe el archivo
archivo_para_escribir = open("./data/nombres/usuarios.txt", "w")
archivo_para_escribir.write("hola")
archivo_para_escribir.write(" Mundo!")
archivo_para_escribir.close()

#%%
# Podemos usar el metodo "a" para escribir añadiendo sin borrar el archivo original
archivo_para_escribir = open("./data/nombres/usuarios.txt", "a")
archivo_para_escribir.write("hola")
archivo_para_escribir.write(" Mundo!")

archivo_para_escribir.close()


#%%
"""
Usar el metodo de open, close no es ideal, basicamente por que si ocurre un error
entre los dos métodos podemos perder el archivo.

la manera mejor de leer y escribir de archivos es mediante el contexto with
"""
usuarios = ["Manuel", "Antonio", "Juan", "Miguel"]
with open("./data/nombres/usuarios.txt", "w") as fname:
    for usuario in usuarios:
        fname.write(usuario)
#%%
# Si queremos escribir cada elemento de la lista en una lina, escribimos un |n entre lineas

usuarios = ["Manuel", "Antonio", "Juan", "Miguel", "Fernando", "Alejandro"]
with open("./data/nombres/usuarios.txt", "w") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")
#%%

"""
*******************************************************************************
LECTURA DE ARCHIVOS
*******************************************************************************
"""        

with open("./data/nombres/usuarios.txt") as fname:
    datos = fname.read()
print(datos)

type(datos)
#%%

# Si queremos separar los usuarios debemos separar el texto en lineas.
# para esto lo mejor es usar el método readlines(), que no lee todo el archivo
# a la vez, sino de forma iterativa (así no consume tanta memoria)
usuarios_desde_archivo = []

with open("./data/nombres/usuarios.txt") as fname:
    lineas = fname.readlines()
    for linea in lineas:
        usuarios_desde_archivo.append(linea.strip("\n"))
print(usuarios_desde_archivo)

type(usuarios_desde_archivo)

#%%
"""
*******************************************************************************
USANDO PATHLIB
*******************************************************************************

En windows las carpetas se definen con \ mientras que en mac o linux se usa /

Esto puede dar errores

Una manera de garantizar que podemos acceder a archivos independientemente del
sistema operativo es con el modulo pathlib (disponible en python 3 solo)
"""

from pathlib import Path

carpeta = Path("./data/nombres/")

archivo = carpeta / "usuarios.txt" 
print(type(archivo)) #PosixPath o WindowsPath
# no tenemos que usar with
archivo.read_text()
#%%
# con pathlib podemos escribir facilmente a un archivo
carpeta = Path("./data/nombres/")

archivo = carpeta / "usuarios_2.txt"

archivo.write_text("hola!")
#%%
print(archivo.read_text())

#%%
# para añadir texto al final de un archivo seguimos necesitando 
usuarios = ["Manuel", "Antonio", "Juan", "Miguel", "Fernando", "Alejandro"]

carpeta = Path("./data/nombres/")
archivo = carpeta / "usuarios_2.txt"

with open(archivo, "a") as fname:
    for usuario in usuarios:
        fname.write(usuario)
        fname.write("\n")
        
archivo.read_text()
#%%
"""

EJERCICIOS

"""
#%%
"""
Hacer una función que dado el nombre de un archivo, lo lea y devuelva la linea 
con la mayor longitud

"""

#%% 
"""
Hacer una función que tenga como argumento un nombre de un archivo y un
número n y devuelva las n ultimas lineas del archivo
"""


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
    Miguel,40,Almería
    ...
    
"""
