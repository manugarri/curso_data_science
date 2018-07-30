# -*- coding: utf-8 -*-
"""
Aquí se explica como crear funciones en python

EJERCICIOS

******************************************************************************
"""

#%%
# Crear funcion resta que resta 2 numeros y devuelve el resultado
def resta(a, b):
    return a - b

print(resta(52, 10))
#%%
# Crear funcion lambda que convierte un string a minusculas

minusculas = lambda text: text.lower()
minusculas("Hola Mundo!")
#%%
# Crear una funcion que acepta 3 argumentos, 2 numeros y un string. Si el string es
# "suma", devolver la suma de los dos numeros, si el string es "resta" devolver
# la resta
def suma_o_resta(a, b, modo):
    if modo == "suma":
        return a + b
    elif modo == "resta":
        return a - b
    else:
        raise Exception("suma_o_resta solo admite dos modos, suma o resta")

print(suma_o_resta(10, 3, "suma"))

print(suma_o_resta(10, 3, "resta"))

print(suma_o_resta(5, 2, "multiplicacion"))
#%% Crear una funcion que pregunte al usuario una frase y devuelva dicha frase con
# palabras en orden inverso. Por ejemplo, si el usuario dice "la lluvia en Sevilla"
# la funcion devolverà "Sevilla en lluvia la"
def invertir_palabras(frase):
    frase_invertida = ""
    palabras = frase.split(" ")
    for palabra in palabras[::-1]:
        frase_invertida += palabra
        frase_invertida += " "
    return frase_invertida

print(invertir_palabras("la lluvia en Sevilla"))
#%%
def invertir_palabras_mejorado(frase):
    palabras = frase.split(" ")
    return " ".join(palabras[::-1])

print(invertir_palabras_mejorado("la lluvia en Sevilla"))

#%% Crear una función que detecte si una palabra o frase es palindromo (un palíndromo
# es aquella palabra o frase que se lee de igual forma de un sentido u otro)
def es_palindromo(frase):
    frase_invertida = frase[::-1]
    for i in range(len(frase_invertida)):
        if frase[i] != frase_invertida[i]:
            return False
    return True

es_palindromo("patata")
es_palindromo("dabalearrozalazorraelabad")
#%%
"""
 Crear una funcion que dada una lista de listas, nos devuelva una lista simple
 (es decir, sin ninguna lista dentro)

por ejemplo, si a dicha funcion le pasamos el argumento

lista_nesteada = [
        [1,2,3],
        [4,5, 6, 7],
        [8, 9]
]

la funcion nos devolveria la lista [1,2,3,4,5,6,7,8,9]

"""

def simplificar_lista(lista_nesteada):
    lista_simple = []
    for lista_interna in lista_nesteada:
        for elemento in lista_interna:
            lista_simple.append(elemento)
    return lista_simple

lista_nesteada = [
        [1,2,3],
        [4, 5, 6, 7],
        [8, 9]
]

simplificar_lista(lista_nesteada)
