# -*- coding: utf-8 -*-
"""
Aquí se explican los principales métodos de control de flujo 

@author: manugarri
"""

"""
*******************************************************************************
IF-ELSE
*******************************************************************************

Usamos if-else para tomar decisiones y ejecutar distintas partes del código en
funcion de una condicion


NOTA: en python, la manera de indicar si estamos dentro de un bucle (o una funcion)
es mediante el indentado, es decir poniendo 4 espacios delante del código 
(en spyder pulsar la tecla Tabulador inserta 4 espacios automáticamente)
"""
#%%
# La manera mas sencilla de implementar una evaluación lógica es con un if.
temperatura = 35

if temperatura <= 20:
    #el codigo se indenta 4 espacios para indicar que estamos dentro del if
    print("Ponte una rebequita que refresca")
    print("esto se imprime si o si")
#%%
"""
 Si queremos tomar distintas condiciones en funcion de una condicionu otra ocurra
 podemos usar if-else
"""

temperatura = 35

    
if temperatura <= 10:
    respuesta_abuela = "¡Ponte un abrigo nene, que hace frío y te vas a resfriar!"
elif temperatura <= 20:    
    #el codigo se indenta 4 espacios dentro del if
    respuesta_abuela = "¡Ponte una rebequita que refresca!"
elif temperatura <= 30:
    respuesta_abuela = "Nenico no vuelvas muy tarde ¿eh?"
# el else se evaluará si ninguna de las condiciones anteriores se dan
else: 
    respuesta_abuela = "¡Ve por la sombra que hace calor!"

print(respuesta_abuela)    

#%%
#Tambien se pueden insertar ifs dentro de otros ifs (esto se llama "nestear")


temperatura = 25
lluvia = False

if 20 < temperatura < 30:
    #True evalua a True, usando not obtenemos el opuesto
    if not lluvia:
        print("¡Vámonos de picnic!")

#%%
"""
*******************************************************************************
BUCLES FOR (FOR LOOPS)
*******************************************************************************

Los bucles FOR sirven para iterar entre los elementos de una lista uno por uno 
(o de cualquier elemento de python que soporte iteración)
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for numero in numeros:
    if numero <= 10:
        print(f"numero válido {numero}")
    else:
        print(f"¡ERROR! numero {numero} mayor de 10")


#%%
"""
 Hay veces que queremos romper un bucle for si ocurre una condicion, podemos romper
 el loop con break
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for numero in numeros:
    if numero <= 10:
        print(f"numero válido {numero}")
    else:
        print(f"¡ERROR! numero {numero} mayor de 10. SALIENDO DEL BUCLE")
        break        
    
#%%
# Hay veces que en vez de romper el loop, simplemente queremos no hacer nada en
# una iteración en concreto, para esto podemos usar pass
        
numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for numero in numeros:
    if numero <= 10:
        print(f"numero válido {numero}")
    else:
        #pass se usa simplemente en aquellos casos en los que hay que poner
        # algo en un segmento del código, pero no hace nada
        pass        

       
#%%
# continue, al contrario de pass, nos lleva directamente a la siguiente iteración
# del bucle

numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for numero in numeros:
    if numero <= 10:
        print(f"numero válido {numero}")
    else:
        continue
        print("esto no se va a imprimir")
      
        
#%% 
# Hay una forma más simplificada de iterar los elementos de una lista 

[numero for numero in numeros if numero < 10]
#%%
inventario = {
        "melocotones": 3,
        "fresas": 1,
        "manzanas": 4
        }

#Podemos iterar las claves de un diccionario con un for
for fruta in inventario:
    print(fruta)        
#%%
#Podemos iterar las claves y los valores de un diccionario a la vez en un bucle for usando items()
for fruta, cantidad in inventario.items():
    print(fruta, cantidad)
    print("Tenemos {} kilo/s de {}".format(cantidad, fruta))        

#%%
# No sólo las listas son iterables (es decir, soportan bucles for), los strings también!

nombre = "MURCIA"

for letra in nombre:
    print("Dame una {}!".format(letra))    
#%%
"""
*******************************************************************************
TRY-EXCEPT
*******************************************************************************
En ocasiones los programas fallan lanzando una excepción, pero una manera de poder hacer que un programa
continúe su funcionamiento pese a haber fallado es "atrapando" la excepción. 
En python esto se hace mediante el bloque try-except
"""    

#%% 
numero_str = "10.5"

try:
    #se intentará hacer esto
    numero_int = int(numero_str)
except Exception as e: #pero si falla por alguna causa, no pares el programa y haz esto
    print("Error!")
#%%
"""

IMPORTANTE! Siempre que atrapemos una excepcion, es importante por lo menos 
imprimir el mensaje de error
Asi nos aseguramos de que nuestro programa no está fallando catastróficamente 
sin que nos demos cuenta

"""
numero_str = "10.5"

try:
    numero_int = int(numero_str)
except Exception as e: #Exception es una clase de python, capturamos el error en la variable e
    print("Error, el valor {} no se puede convertir a entero".format(numero_str))
    print("El mensaje de error ha sido:")
    print(e, type(e))
    
#%%
"""
 El problema de capturar todos los errores de nuestro programa a ciegas es que 
 podemos pasar errores que hagan que todo falle de forma silenciosa. Una manera
 más efectiva de capturar errores es capturar aquellos que conozcamos, y fallar 
 en caso de un error que no conozcamos
"""
numero_str = "10.5"

try:
    numero_int = int(numero_str)
except ValueError: #esto fallará para todo error que no esa un ValueError
    print("Error: el valor {} no se puede convertir a entero".format(numero_str))    
#%%
"""
*******************************************************************************
WHILE
*******************************************************************************

Los bucles while siguen ejecutandose mientras una condición sigue ocurriendo
"""

n_elefante = 2
print("🎜🎝♩ 1  elefante se balanceaba, sobre la tela de una araña... 🎜🎝♩") 
while n_elefante <=10: 
    print("🎜🎝♩ {} elefantes se balanceaban, sobre la tela de una araña... 🎜🎝♩ ".format(n_elefante))
    #usar n_elefante += 1 es lo equivalente a n_elefante = n_elefante + 1
    n_elefante += 1 
    
#%%
"""
 Hay que tener cuidado al usar un while, ya que podemos quedar atascados en un bucle infinito!
 en python podemos pulsar CTRL+z para parar la ejecucion
"""
while 1>0:
    print("atascado en el loop!")
#%%
"""
un uso común del bucle while es validar el input que nos da un usuario 

Podemos obtener el input de un usario usando la funcion input
"""

while 1:
    input_usuario = input("Dime un numero del 1 al 10, 'exit' para salir: ")
    try:
        if input_usuario == "exit":
            print("Adios!")
            break
        elif int(input_usuario) <= 10:
            cuadrado = int(input_usuario) ** 2
            print("el cuadrado del número {} es {}".format(input_usuario, cuadrado))
        else:
            print("el valor {} no es un valor válido".format(input_usuario))
    except ValueError:
        print("Error: el valor {} no se puede convertir a entero".format(input_usuario))    

#%%

"""
******************************************************************************

EJERCICIOS

******************************************************************************
"""

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

#%%    
"""
 De dicho diccionario, crear una lista de los dias de la semana que contengan 
 la letra "O"
"""
