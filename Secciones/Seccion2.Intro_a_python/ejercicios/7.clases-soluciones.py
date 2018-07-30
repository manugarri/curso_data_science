# -*- coding: utf-8 -*-

"""
Aquí se explican lo que son las clases en Python

EJERCICIO

Crear una clase Taxi, que herede de Vehiculo, y que pueda cobrarnos un trayecto
Tiene que tener un atributo "distancia_recorrida", y tres metodos adicionales:
  - metodo "cobrar", donde se imprime la cantidad a cobrar (3 euro por kilometro
    recorrido)
  - metodo "añadir_distancia", donde se suma a la distancia recorrida un numero
    de kilometros
  - metodo "añadir_tiempo", donde dado un tiempo (en horas) se añade distancia
    en función de la velocidad actual
******************************************************************************
"""

class Taxi(Vehiculo):
    def __init__(self, modelo, velocidad_maxima):
        self.color = "blanco"
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        self.distancia_recorrida = 0
        self.tarifa = 3

    def cobrar(self):
        print("El total es {} €".format(self.distancia_recorrida*self.tarifa))

    def añadir_distancia(self, distancia):
       self.distancia_recorrida += distancia

    def añadir_tiempo(self, tiempo):
        self.añadir_distancia(tiempo*self.velocidad)

taxi = Taxi(modelo="Mercedes Benz", velocidad_maxima=120)
taxi.acelerar(100)
taxi.añadir_tiempo(1)
taxi.añadir_tiempo(5)
taxi.cobrar()


#%%

class Taxi2(Vehiculo):
    def __init__(self, tarifa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.distancia_recorrida = 0
        self.tarifa = tarifa

    def cobrar(self):
        print("El total es {} €".format(self.distancia_recorrida*self.tarifa))

    def añadir_distancia(self, distancia):
       self.distancia_recorrida += distancia

    def añadir_tiempo(self, tiempo):
        self.añadir_distancia(tiempo*self.velocidad)

taxi = Taxi2(modelo="Mercedes Benz", velocidad_maxima=120, tarifa=3, color="blanco")
taxi.acelerar(100)
taxi.añadir_tiempo(1)
taxi.añadir_tiempo(5)
taxi.cobrar()

#%%
"""
******************************************************************************

EJERCICIO

Crear una clase Parking, donde puedan aparcar un limite determinado de Vehiculos
(solo Vehiculos!)
y donde se puede validar si un vehiculo esta aparcado o no
******************************************************************************
"""

class Parking:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []

    def nivel_ocupacion(self):
        return len(self.vehiculos) / self.capacidad

    def __repr__(self):
        return "Parking con capacidad {}. Nivel de ocupación {:.2f}".format(
                self.capacidad, self.nivel_ocupacion())

    def aparcar_vehiculo(self, vehiculo):
        if not type(vehiculo) == Vehiculo or vehiculo in self.vehiculos:
            print("Solo se admiten Vehiculos que no están aparcados")
        elif len(self.vehiculos) < self.capacidad:
            print("Aparcando vehiculo {}".format(vehiculo))
            self.vehiculos.append(vehiculo)

    def sacar_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos:
            print("Sacando el vehiculo {}".format(vehiculo))
            self.vehiculos.pop(self.vehiculos.index(vehiculo))
        else:
            print("Vehiculo {} no está aparcado".format(vehiculo))

parking_glorieta = Parking(capacidad=100)

coche_manuel = Vehiculo(modelo="Peugeot 308", color="Azul", velocidad_maxima=200)
coche_rojo = Vehiculo(modelo="Mercedes Benz", color="rojo", velocidad_maxima=240)
taxi = Taxi(modelo="Mercedes Benz", velocidad_maxima=120)

parking_glorieta.aparcar_vehiculo(coche_manuel)
parking_glorieta.aparcar_vehiculo(coche_rojo)

#%%
parking_glorieta.aparcar_vehiculo(coche_rojo)
parking_glorieta.aparcar_vehiculo(taxi)

#%%
print(parking_glorieta)

#%%
parking_glorieta.sacar_vehiculo(coche_rojo)
print(parking_glorieta)
