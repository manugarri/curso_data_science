# -*- coding: utf-8 -*-
"""
Aquí se explica como crear funciones en python 

@author: manugarri
"""

"""
Los scripts de python se ejecutan linea a linea

Las funciones son formas de separar la lógica en piezas sin tener que ejecutarlas linea a linea,
 y ademas permitir reutilizar partes del código que se repiten
"""

"""
Las funciones se definen de la forma:
    
def nombre_de_la_funcion(argumento1, argumento2,...):
    logica_de_la_funcion

"""
#%%
def saludar():
    print("Hola Mundo!")
 
# Al crear la funcion saludar, no tenemos que escribir el print cada vez    
print(type(saludar))
saludar()

#%%

# La principal ventaja de las funciones es que nos permiten usar argumentos y 
# flexibilizar la lógica de nuestro código

def saludar(nombre):
    print(f"Hola {nombre}, ¿como estás?")
    
saludar("Manuel")
saludar("Antonio")

#%%
# Como esta función necesita un argumento, si la llamamos sin ningún argumento
# nos dará un error
saludar()
#%%
# Las funciones también pueden tener valores por defecto en los argumentos,
def saludar_despistado(nombre="amigo"):
    saludar(nombre)

saludar_despistado("Manuel")
saludar_despistado()

#%%
# Las funciones pueden devolver un valor. 

def suma(a, b):
    return a + b
    print("esto no se va a imprimir, porque la función acaba con el return")

resultado_suma1 = suma(2.5, 5)
print(resultado_suma1)
#%%
# ahora podemos usar el resultado de la función como input
resultado_suma2 = suma(resultado_suma1, 50)
print(resultado_suma2)
#%%
#Una funcion que no tiene un return devuelve None
def suma_erronea(a, b):
    resultado = a + b
    
resultado_suma1 = suma_erronea(2.5, 5)
print(resultado_suma1)


#%% Las funciones pueden tener un solo return, pero se pueden devolver multiples cosas!

def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = suma_y_resta(10, 5)
print(resultado)
print(type(resultado))

#%%
# podemos desempaquetar el resultado directamente
resultado_suma, resultado_resta = suma_y_resta(10, 5)
print(resultado_suma)
print(resultado_resta)


#%%
"""
Existe otra forma de crear funciones, las llamadas lambda o funciones anónimas

Se definen de la forma:
func_lambda = lambda input: output

Las funciones lambda se suelen utilizar cuando queremos aplicar lógica sencilla 
para la cual definir una función "oficial" no es necesario
"""

suma_lambda = lambda a, b: a + b
resultado_suma1 = suma_lambda(2.5, 5)
print(resultado_suma1)
#%%
# ahora podemos usar el resultado de la función como input
resultado_suma2 = suma_lambda(resultado_suma1, 50)
print(resultado_suma2)


#%%
"""
******************************************************************************

EJERCICIOS

******************************************************************************
"""

#%%
"""
 Crear funcion resta que resta 2 numeros y devuelve el resultado
"""

#%%
"""
 Crear funcion lambda que convierte un string a minusculas
"""

#%%
""" Crar una funcion que acepta 3 argumentos, 2 numeros y un string. Si el string es
 "suma", devolver la suma de los dos numeros, si el string es "resta" devolver
 la resta
"""

#%% 
"""
Crear una funcion que pregunte al usuario una frase y devuelva dicha frase con
palabras en orden inverso. Por ejemplo, si el usuario dice "la lluvia en Sevilla"
la funcion devolverà "Sevilla en lluvia la"
"""

#%% 
"""
Crear una función que detecte si una palabra o frase es palindromo (un palíndromo
es aquella palabra o frase que se lee de igual forma de un sentido u otro)
"""

#%%
"""
 Crear una funcion que dada una lista de listas, nos devuelva una lista simple (es decir, sin ninguna lista dentro)

por ejemplo, si a dicha funcion le pasamos el argumento

lista_nesteada = [
        [1,2,3],
        [4,5.6,7],
        [8,9]
]

la funcion nos devolveria la lista [1,2,3,4,5,6,7,8,9]

"""




