# -*- coding: utf-8 -*-
"""
Aquí se explican los principales tipos de variables 

@author: manugarri
"""
#%%
"""
python tiene muchos tipos de variables básicas que forman parte del núcleo del
lenguaje, son lo que se llama primitivas. 
"""

"""Las primitivas más comunes son strings, numeros, booleanos"""

"""
*******************************************************************************
STRINGS
*******************************************************************************
"""
print("Se usan para representar texto")
#%%
var_str = "Hola!"
var_str2 = "Mundo!"

print(var_str)
print(var_str2)
print(var_str, var_str2)

print(type(var_str2))
#%%

"""
los strings se pueden unir para formar strings más largos. Hay varias 
maneras de unir strings (lo que se llama interpolación de strings)
"""

# Podemos usar el simbolo + para "sumar" (concatenar) strings
var_str_unido = var_str + " " + var_str2
print(var_str_unido)
#%%
#Tambien podemos 'multiplicar' strings!
n = "monja"
print(n * 10)
#%%
"""
Tambien podemos usar el método format, que nos permite insertar unos  strings
dentro de otros
"""

nombre = "Manuel"
ciudad = "Murcia"

presentacion = "Hola, me llamo {}, soy de {}"

print(presentacion.format(nombre, ciudad))
#%%

nombre2 = "María"
ciudad2 = "Madrid"
print(presentacion.format(nombre2, ciudad2))

#%%
"""
Python es un lenguaje con "pilas incluidas" , esto quiere decir que tiene
un montón de funcionalidades incluidas con la instalación básica de Python.

Dichas funcionalidades se agrupan en módulos o paquetes y podemos usarlas 
con la palabra import

Por ejemplo, si queremos hacer uso del módulo de python encargado de operaciones 
matemáticas, escribimos "import math" (importamos el módulo math)
"""

import math

print(math.pi)
#%%
# Usando el metodo format se puede indicar como formatear las variables
# Por ejemplo, redondear números decimales.

pi_str = "los primeros dígitos de pi son: {}".format(math.pi)
print(pi_str)

#%%
# podemos restringir que se imprima pi con 2 decimales
pi_str = "los primeros dígitos de pi son: {:.2f}".format(math.pi)
print(pi_str)

#%%
#Si pasamos 0 decimales hemos redondeado a un entero
pi_str = "los primeros dígitos de pi son: {:.0f}".format(math.pi)
print(pi_str)

#%%
"""otra manera de usar interpolación de strings (solo disponible en python 3.6 
en adelante) es referenciar directamente las variables en el string convirtiendolo
en un f-string (se convierte un string poniendole la letra f delante)
"""

presentacion2 = f"Hola, me llamo {nombre}, soy de {ciudad}"
print(presentacion2)


#%%
nombre = "Juan"
print(presentacion2)

#%%
"""
Más OPERACIONES CON STRINGS
"""

titulo = "introduccion a PYTHON"

print("convertimos un string en mayusculas con upper")
print(titulo.upper())
print("convertimos un string en minusculas con lower")
print(titulo.lower())
print("Ponemos la primera letra en mayúscula con capitalize")
print(titulo.capitalize())
#%%
nombre_con_comas = ",manuel,"
print("usamos strip para eliminar caracteres al inicio y al final de un string")
print(nombre_con_comas.strip(","))

#%%
print("usamos replace para reemplazar partes de un string por otras")
print(nombre_con_comas.replace("nuel", "riano"))

#%%
print("todos los métodos se pueden encadenar")
print(nombre_con_comas.strip(",").replace("nuel","riano").upper())


#%%
# Se puede separar un string en múltiples usando el método split()

colores_str = "rojo|amarillo|verde|azul"
colores_lista = colores_str.split("|")
print(colores_lista)

#%%
"""
*******************************************************************************
NÚMEROS
*******************************************************************************
"""
print("hay dos tipos básicos de primitivas numéricas en python, int(enteros) y float(decimales)")

entero = 23
print(type(entero))

#%%
decimal = 23.1
print(type(decimal))

#%%
print(type(23.))

#%%
print("podemos convertir números a strings fácilmente")
print(type(str(entero)))
print("dos + " + str(decimal))
#%%
print("Tambien podemos usar numeros en interpolacion de strings")
nombre = "Manuel"
ciudad = "Murcia"
edad = 33
print(f"Hola, me llamo {nombre}, soy de {ciudad} y tengo {edad} años")
#%%
print("de igual forma, podemos convertir strings a números")
numero_string = "24"
print(int(numero_string) + 5)
print(float(numero_string) + 5)
#%%
print("Hay que asegurarse de que sean números válidos!")
numero_string_invalido = "24,5"
print(float(numero_string_invalido))
#%%
print("de igual forma, no podemos convertir un string float a un entero")
print(int("24.1"))
#%%
"""
OPERACIONES NUMERICAS


Podemos usar los simbolos basicos de aritmetica para realizar operaciones
"""
#suma
print("2+2=",2+2)
#resta
print("4-9=",4-9)
#multiplicacion
print("3*2=",3*2)
#division
print("7/2=",7/2)
#%%
"""
Aparte, tenemos más operaciones que podemos hacer
"""
a = 7
b = 2
# multiplo inferior, realizar la division eliminando el resto
print(f"{a}//{b}=", a//b)
# modulo, realizar una division y quedarse solo con el resto
print(f"{a}%{b}=", a%b)
#negacion, cambiar de sentido un valor
print(f"negacion de {a}=", -a)
#potencias, elevar al cuadrado, al cubo, etcétera
print(f"{a}**{b}=",a**b)
#%%
"""
*******************************************************************************
BOOLEANOS
*******************************************************************************

Una variable booleana es aquella que solo puede ser verdadera o falsa
"""

verdadero = True
falso = False

print(type(verdadero))


#%%
"""
Como tipo de primitiva especial, tenemos None, que es la variable nula.
"""

nulo = None
print(type(nulo))

#%%

#cualquier tipo de variable se puede convertir a booleano, transformandose en True
print(bool("patata"))

#%%
print(bool(""))
#%%
# 0 se transforma en False
print(bool(0))

#salvo None que se convierte a False
print(bool(nulo))
#%%
"""
COMPARACIONES LÓGICAS

Podemos hacer comparaciones entre variables, el resultado de estas comparaciones 
siempre es una variable booleana
"""

a = 7
b = 2
# a mayor o igual a b
print(f"{a} > {b}", a > b)
# b menor o igual a a
print(f"{b}<={a}", b<=a)
# b es igual a 2
print(f"{b}==2", b == 2)
# a es distinto a 23
print(f"{a}!=23",a != 23)
#%%

#podemos obtener el opuesto de un resultado logico con not
print(f"not {a}!=23",not a != 23)
#%%

# podemos evaluar que varias condiciones se cumplen con and
print(f"{a}!=23 and {a}<{b}=",a != 23 and a < b)
#podemos usar or para evaluar si se cumple una condicion u otra
print(f"{a}!=23 or {b}<{a}=",a != 23 or a < b)

#%%

"""
para comparar si algo es verdadero o falso, no usamos '==', sino que usamos 'is'
"""

print("verdadero is True=", verdadero is True)