# -*- coding: utf-8 -*-
"""
Aquí se explican los principales métodos de control de flujo

EJERCICIOS

******************************************************************************
"""

#%%
# Dado el diccionario:
dias_semana = {"lunes":1,
               "martes":2,
               "miercoles": 3,
               "jueves": 4,
               "viernes": 5,
               "sabado": 6,
               "domingo": 7
               }

#%%
"""
De dicho diccionario, convertir todas las claves a mayúsculas, usando un bucle
"""
# Esto no funciona, no podemos cambiar el tamañó de un diccionario dentro de un loop
for clave, valor in dias_semana.items():
    dias_semana[clave.upper()] = valor
    dias_semana.pop(clave)

#%%
dias_semana_mayusculas = {}
for clave, valor in dias_semana.items():
    dias_semana_mayusculas[clave.upper()] = valor
dias_semana = dias_semana_mayusculas
print(dias_semana)


# %% De dicho diccionario, crear una lista de los dias de la semana que contengan
# la letra "O"
dias_con_o = []
for clave in dias_semana:
    if "O" in clave:
        dias_con_o.append(clave)
print(dias_con_o)
