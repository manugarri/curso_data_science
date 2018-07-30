# -*- coding: utf-8 -*-
"""
Aquí se explican estructuras de datos avanzadas

EJERCICIOS

*******************************************************************************
"""
#%%
"""
 Convertir la lista de pokemon_entrenadores en una lista de diccionarios con las
claves "entrenador" y "pokemon"
"""

pokemon_entrenadores_dict = []
for tupla_entrenador in pokemon_entrenadores_lista:
    pokemon_entrenadores_dict.append({"entrenador": tupla_entrenador[0], "pokemon": tupla_entrenador[1]})

pokemon_entrenadores_dict

#%% Otra forma sería:
pokemon_entrenadores_dict = []
for entrenador, pokemon in pokemon_entrenadores_lista:
    pokemon_entrenadores_dict.append({"entrenador": entrenador, "pokemon": pokemon})
pokemon_entrenadores_dict
#%%
"""
Hacer una funcion que toma una frase y devuelve las 5 letras mas comunes
"""

def contar_letras(frase):
    contador = Counter([letra for letra in frase if letra not in " ,.\n"])
    return contador.most_common(5)


"""
Crear una función que, dados dos listas de elementos, nos devuelva su coeficiente de jaccard.
 El coeficiente de Jaccard es una medida de similaridad entre dos grupos y se define
 como el número de elementos en los dos grupos dividido entre el número de elementos
 en uno u otro grupo
"""

def jaccard(grupo1, grupo2):
    union = len(set(grupo1).union(set(grupo2)))
    interseccion = len(set(grupo1).intersection(set(grupo2)))
    return interseccion / union

grupo_amigos1 = ["Manuel", "Rodrigo", "Miguel", "Jesus", "Iñigo"]
# tambien se pueden crear con llaves {}
grupo_amigos2 = ["Manuel", "Alejandro", "Fernando", "Antonio", "Lazaro"]

jaccard_amigos = jaccard(grupo_amigos1, grupo_amigos2)
print(jaccard_amigos)
