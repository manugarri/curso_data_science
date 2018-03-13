# -*- coding: utf-8 -*-

"""
Aquí se explican lo que son las clases en Python 

@author: manugarri
"""

"""
Python es un lenguaje orientado a objetos. ¿Eso que significa? Que pese a que 
podamos programar de forma "funcional", esto es simplemente enviando datos a través 
de funciones, muchas de las ventajas de python están en su uso de clases. 

Las clases en python se definen de la forma (en python 3):
    
    
class Clase:
    def metodo1(self): -->TODOS LOS METODOS DE CLASE TOMAN 'self' COMO PRIMER ARGUMENTO
        #método que tienen los objetos de la clase
        
    def metodo2(self):
        #otro método que tienen los objetos de la clase
        
"""

#%%

# Por ejemplo, podemos crear una clase Coche
class CocheBasico:

    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self):
        # podemos usar pass cuando definimos una funcion, para que no haga nada
        pass

    def frenar(self):
        pass


print(CocheBasico)

#%% 
"""
Hemos generado una clase CocheBasico. Las clases se pueden considerar como plantillas
que se pueden usar para generar objetos. Por ejemplo la plantilla (clase) Coche
nos da instrucciones para fabricar un coche 
(en jerga de desarrollo se llama "instanciar una clase", es decir, creamos una 
instancia (objeto) de la clase Coche).
"""

coche_de_manuel = CocheBasico()
print(coche_de_manuel)

#%%
# Este objeto coche es un Coche, es decir, es un objeto de la Clase Coche

print(type(coche_de_manuel) == CocheBasico)

#%%
#Este coche tambien tiene todas las caracteristicas de la Clase Coche
coche_de_manuel.girar_derecha()
coche_de_manuel.girar_izquierda()
coche_de_manuel.acelerar() # esto no hace nada
#%%
"""
Al igual que con las funciones, generalmente querremos que los objetos que creemos
tengan unas características definidas de forma variable. 
Con la clase Coche que tenemos, todos los coches que creemos serán 100% iguales. 
¿Como podriamos generar coches que tengan distinto color, por ejemplo?

Para eso podemos usar el método especial __init__ que se ejecuta cuando se crea
un objeto de una Clase.
"""

class CocheConColor:

    def __init__(self, color):
        self.color = color  #<-- Esto es un atributo
    
    def describir(self):
        print("Coche de color {}".format(self.color))
        
    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self):
        # podemos usar pass cuando definimos una funcion, para que no haga nada
        pass

    def frenar(self):
        pass
    
coche_rojo = CocheConColor(color="rojo")
coche_rojo.describir()
print(coche_rojo.color)
#%%
# Tambien podemos añadir atributos a instancias
coche_rojo.matricula = "ER23244"
print(coche_rojo.matricula)

#%%
# Ahora al crear un CocheConColor tenemos que especificar un color
coche_sin_color = CocheConColor() 

#%% 
# Podemos evitar esto simplemente indicando argumentos por defecto en el metodo __init__
class CocheConColor:

    def __init__(self, color="negro"):
        self.color = color
    
    def describir(self):
        print("Coche de color {}".format(self.color))
        
    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self):
        # podemos usar pass cuando definimos una funcion, para que no haga nada
        pass

    def frenar(self):
        pass
    
coche_sin_color = CocheConColor()
coche_sin_color.describir()

#%%
# De igual forma, podemos definir todas las variables que necesitamos para definir
# un objeto
class CocheVariable:

    def __init__(self, modelo, velocidad_maxima, color="negro"):
        self.color = color
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        
    def describir(self):
        print("Coche Modelo:{}. Color {}. Velocidad máxima: {}".format(
                self.modelo, self.color, self.velocidad_maxima))

    def describir_estado(self):
        if self.velocidad == 0:
            print("El coche está parado")
        else:
            print("El coche va a {} kilómetros por hora".format(self.velocidad))
            
    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self):
        # podemos usar pass cuando definimos una funcion, para que no haga nada
        pass

    def frenar(self):
        pass

coche_manuel = CocheVariable(modelo="Peugeot 308", color="Azul", velocidad_maxima=200)
coche_manuel.describir()
coche_manuel.describir_estado()

#%%
# Podemos en cualquier momento cambiar cualquier atributo de un objeto
coche_manuel.velocidad = 100
coche_manuel.describir_estado()


#%%
print(coche_manuel)
#%%
"""

Uno de los usos principales de las clases es conservar el "estado" de un objeto.
Si no usaramos clases para almacenar la velocidad de un coche, tendriamos que tener
un diccionario con los identificadores de los coches y su velocidad, y cadad 
vez que cambiaramos la velocidad tendriamos que cambiar el diccionario.

Ahora nos falta simplemente añadir las funciones para acelerar y tendremos un 
vehículo completo
"""
class Vehiculo:

    def __init__(self, modelo, velocidad_maxima, color="negro"):
        self.color = color
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        
    def describir(self):
        descripcion = "Vehiculo Modelo:{}. Color {}. Velocidad máxima: {}".format(
                self.modelo, self.color, self.velocidad_maxima)
        return descripcion
    
    # El metodo __repr__ es un metodo mágico que se usa cuando queremos representar algo (con el metodo print)
    def __repr__(self):
        return self.describir()

    def describir_estado(self):
        if self.velocidad == 0:
            print("El vehiculo está parado")
        elif self.velocidad > 0:
            print("El vehiculo va a {} kilómetros por hora".format(self.velocidad))
        else:
            print("El vehiculo va marcha atrás {} a kilómetros por hora".format(self.velocidad))
            
    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self, diferencia_velocidad):
        print("Acelerando {} km/h".format(diferencia_velocidad))
        # abs devuelve un numero positivo si es negativo
        self.velocidad += abs(diferencia_velocidad)
        # min devuelve el valor minimo de una lista de números
        self.velocidad = min(self.velocidad, self.velocidad_maxima)

    def frenar(self, diferencia_velocidad):
        print("Frenando {} km/h".format(diferencia_velocidad))
        self.velocidad -= abs(diferencia_velocidad)
        # max nos devuelve el máximo valor de una lista de números
        self.velocidad = max(self.velocidad, -5)


coche_manuel = Vehiculo(modelo="Peugeot 308", color="Azul", velocidad_maxima=200)
coche_manuel.describir_estado()
coche_manuel.acelerar(20)
coche_manuel.describir_estado()

#%%
coche_manuel.acelerar(20)
coche_manuel.describir_estado()
#%%
coche_manuel.frenar(60)
coche_manuel.describir_estado()
#%%
coche_manuel.acelerar(5)
coche_manuel.describir_estado()
print(coche_manuel)
#%%
"""
Herencia de clases

Una de las principales ventajas de usar clases es que se pueden crear clases usando
como plantillas otras clases (se dice que una clase "hereda" de otra)

Ésto nos permite el crear una clase base con funcionalidades genéricas
y despues crear clases avanzadas con diversas funcionalidades más específicas.

Por ejemplo, podemos crear una clase Autobus, que no tiene marcha atrás y que tiene
un limite de velocidad de 100.
"""

class AutoBus(Vehiculo): #-->ESTO INDICA QUE AutoBus hereda de Vehiculo
    def acelerar(self, diferencia_velocidad):
        print("Autobus acelerando {} km/h".format(diferencia_velocidad))
        # abs devuelve un numero positivo si es negativo
        self.velocidad += abs(diferencia_velocidad)
        # min devuelve el valor minimo de una lista de números
        self.velocidad = min(self.velocidad, 100)
        
    def frenar(self, diferencia_velocidad):
        print("Autobus frenando {} km/h".format(diferencia_velocidad))
        self.velocidad -= abs(diferencia_velocidad)
        # max nos devuelve el máximo valor de una lista de números
        self.velocidad = max(self.velocidad, 0)

autobus_urbano = AutoBus(modelo="Mercedes", color="rojo", velocidad_maxima=180)
autobus_urbano.describir_estado()
autobus_urbano.acelerar(50)
autobus_urbano.describir_estado()
autobus_urbano.acelerar(100)
autobus_urbano.describir_estado()
autobus_urbano.frenar(120)
autobus_urbano.describir_estado()

#%%
"""
******************************************************************************

EJERCICIO

Crear una clase Taxi, que herede de Vehiculo, y que pueda cobrarnos un trayecto
Tiene que tener un atributo "distancia_recorrida", y tres metodos adicionales:
  - metodo "cobrar", donde se imprime la cantidad a cobrar (3 euro por kilometro)
  - metodo "añadir_distancia", donde se suma a la distancia recorrida un numero de kilometros
  - metodo "añadir_tiempo", donde dado un tiempo (en horas) se añade distancia en función de la velocidad
******************************************************************************
"""



#%%
"""
******************************************************************************

EJERCICIO

Crear una clase Parking, donde puedan aparcar un limite determinado de Vehiculos 
(solo Vehiculos!)
y donde se puede validar si un vehiculo esta aparcado o no
******************************************************************************
"""

