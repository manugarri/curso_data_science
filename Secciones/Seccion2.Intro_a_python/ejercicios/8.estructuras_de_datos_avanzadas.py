# -*- coding: utf-8 -*-
"""
Aquí se explican estructuras de datos avanzadas 

@author: manugarri
"""


"""
*******************************************************************************
SETS
*******************************************************************************

Los sets son conjuntos de elementos no repetidos. Sirven para dos funciones principales

"""



# los sets se pueden crear a partir de una lista
grupo_amigos1 = set(["Manuel", "Rodrigo", "Miguel", "Jesus", "Iñigo"])
print(type(grupo_amigos1))

#%%
# tambien se pueden crear con llaves {}
grupo_amigos2 = {"Manuel", "Alejandro", "Fernando", "Antonio", "Lazaro"}
print(type(grupo_amigos2))
#%%
# Los sets se usan para evaluar pertenencia de un elemento en un grupo

print("Manuel" in grupo_amigos1)
#%% 
# Con sets se pueden ver los elementos comunes o dispares de los mismos

todos_amigos = grupo_amigos1.union(grupo_amigos2)
print(todos_amigos)
#%%
amigos_comunes = grupo_amigos1.intersection(grupo_amigos2)
print(amigos_comunes)

#%%
amigos_exclusivos_grupo1 = grupo_amigos1 - grupo_amigos2
print(amigos_exclusivos_grupo1)

#%%
# Se pueden añadir o quitar elementos de un set

avengers = {"Iron Man", "Thor", "Hulk", "Viuda Negra", "Capitán América", "Ojo de Halcón"}

avengers.add("Spiderman")
print(avengers)
#%%
avengers.remove("Ojo de Halcón")
print(avengers)
#%% 
# Los sets tambien son utiles para eliminar elementos duplicados de una lista

avengers_repetidos = ["Iron Man", "Thor", "Hulk", "Viuda Negra", "Capitán América",
                      "Ojo de Halcón","Iron Man", "Thor", "Hulk", "Viuda Negra",
                       "Hulk", "Viuda Negra"]

print(len(avengers_repetidos))

avengers_unicos = list(set(avengers_repetidos))
print(avengers_unicos)

#%%
# Se pueden comparar sets

set1 = {"fresa", "manzana"}

set2 = {"manzana", "fresa"}

print(set1 == set2)
#%%
# un set es mas grande que otro si tiene todos los elementos del segundo y al 
# menos un elemento más
set3 = {"fresa", "manzana", "platano"}
print(set3 > set2)

#%%
set4 = {"mora", "manzana"}
print(set3 > set4)
#%%
"""
*******************************************************************************
Counter
*******************************************************************************

la clase Counter sirve para contar cosas
"""

from collections import Counter


votos = ['PODEMOS',
         'PSOE',
         'PSOE',
         'PODEMOS',
         'PP',
         'PSOE',
         'PP',
         'PP',
         'PP',
         'PODEMOS',
         'PSOE',
         'PP',
         'CIUDADANOS',
         'PSOE',
         'PP',
         'PODEMOS',
         'PODEMOS',
         'PODEMOS',
         'PODEMOS'
]

recuento_votos = Counter(votos)


print(recuento_votos)

#%%
# Podemos ver el numero de veces que un elemento en particular aparece
recuento_votos["PP"]
#%%
# Si un elemento no existe, se devuelve 0
recuento_votos["UPyD"]
#%%
#Se pueden añadir elementos a un Counter dinámicamente
print(recuento_votos["CIUDADANOS"])
recuento_votos.update(["CIUDADANOS"])
print(recuento_votos["CIUDADANOS"])
#%%
#tambien podemos aumentar el recuento usando un diccionario
recuento_votos.update({"CIUDADANOS":5,"PODEMOS":6})
print(recuento_votos)

#%%
#Tambien podemos especificar directamente el recuento de un elemento
recuento_votos["UPyD"] = 1

print(recuento_votos)
#%%
"""
*******************************************************************************
DefaultDict
*******************************************************************************

La clase DefaultDict nos permite crear diccionarios que permiten devolver un valor
por defecto si una clave no existe

defaultdict se inicia pasandole una funcion que indicará el valor a devolver en 
caso de no existir la clave especificada

DefaultDict no existe como primitiva de python, sino que está en el módulo collections
esto significa que tenemos que importarlo para poder utilizarlo



"""
from collections import defaultdict

# esto va a fallar, "vainilla" no es una funcion!
sabores_helado = defaultdict("vainilla")
#%%
sabores_helado = defaultdict(lambda: "vainilla")

print(sabores_helado)
#%%
sabores_helado["Manuel"] = "chocolate"
print(sabores_helado["Manuel"])
#%%
# maria no es una clave existente, por lo tanto devuelve el valor por defecto
print(sabores_helado["Maria"])
#%%
# Tambien podemos crear un defaultdict a partir de un diccionario

sabores_helado_dict = {"Manuel": "chocolate", "Maria": "fresa"}
sabores_helado = defaultdict(lambda: "vainilla", sabores_helado_dict)

print(sabores_helado)



#%%
"""
Un uso muy frecuente de defaultdict es cuando tenemos un conjunto de elementos 
donde cada elemento tiene múltiples caracteristicas, y queremos hacer un diccionario
para poder obtener rápidamente su lista de características.
"""

pokemon_entrenadores_lista = [
        ['Ash', 'Nidorian'],
         ['Ash', 'Charmander'],
         ['Ash', 'Jigglypuff'],
         ['Ash', 'Rattata'],
         ['Ash', 'Pikachu'],
         ['Ash', 'Pidgey'],
         ['Misty', 'Pikachu'],
         ['Misty', 'Squirtle'],
         ['Misty', 'Jigglypuff'],
         ['Misty', 'Rattata'],
         ['Brock', 'Nidorian'],
         ['Brock', 'Charmander'],
         ['Brock', 'Jigglypuff']
]

pokemons_por_entrenador = defaultdict(list)

for entrenador, pokemon in pokemon_entrenadores_lista:
    pokemons_por_entrenador[entrenador].append(pokemon)
pokemons_por_entrenador
#%%
"""
*******************************************************************************

EJERCICIOS

*******************************************************************************
"""
#%%
"""
 Convertir la lista de pokemon_entrenadores en una lista de diccionarios con las 
claves "entrenador" y "pokemon"

[
{"entrenador": "Ash", "pokemon": "Pikachu"},
{"entrenador":"Ash", "pokemon": "Nidorian"},
...
]
"""


#%%
"""
Hacer una funcion que toma una frase y devuelve las 5 letras mas comunes 
"""

        
#%%
"""
Crear una función que, dados dos listas de elementos, nos devuelva su coeficiente de jaccard.
 El coeficiente de Jaccard es una medida de similaridad entre dos grupos y se define
 como el número de elementos en los dos grupos dividido entre el número de elementos 
 en uno u otro grupo
"""
