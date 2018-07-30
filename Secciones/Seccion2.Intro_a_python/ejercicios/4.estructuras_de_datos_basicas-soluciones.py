# -*- coding: utf-8 -*-
"""
Aquí se explican los principales tipos de estructuras de datos

EJERCICIOS

******************************************************************************
"""

#%%
# Crear un diccionario cuyas claves sean los tres primeros dias de la semana y los valores sean
# la posicion en la semana de dicho dia

dias_semana = {
        "lunes": 1,
        "martes": 2,
        "miercoles": 3
        }

print(dias_semana)

#%%
dias_semana["lunes"]
#%%
# De dicho diccionario, convertir todas las claves a mayúsculas
dias_semana["LUNES"] = dias_semana.pop("lunes")
dias_semana["MARTES"] = dias_semana.pop("martes")
dias_semana["MIERCOLES"] = dias_semana.pop("miercoles")
print(dias_semana)

#%%
dias_semana = {
        "LUNES": dias_semana["lunes"],
        "MARTER": dias_semana["martes"],
        "MIERCOLES": dias_semana["miercoles"]
        }