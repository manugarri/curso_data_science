# -*- coding: utf-8 -*-
"""

Ejercicio. 3 en Raya

Este ejercicio nos va a ayudar a afianzar los conocimientos adquiridos sobre flujo
de control, y estructuras de datos

Vamos a hacer un programa que nos permita jugar al 3 en raya desde la terminal


Básicamente el panel de 3 en raya son 3 listas dentro de otra

tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la
izquerda, podemos acceder haciendo tablero[[0,0]]

Tenemos a 2 jugadores, que turno por turno iran eligiendo coordenadas en el tablero
y poniendo una ficha, una "X" para el jugador 1 y un circulo "O" para el jugador 2


El juego tendrá que validar que las casillas que elijan los jugadores no estén ya
ocupadas por una ficha (es decir, solo se pueden actualizar casillas que sean 0)

"""


from collections import deque

"""
Un deque es una lista donde se pueden insertar elementos por la izquierda y por la
derecha.

Tiene un método llamado rotate que simplemente "rota" los elementos.
Es decir, rotate() pone el ultimo elemento del deque el primero, el primer
elemento el segundo etcétera.
"""

turno = deque(["O", "X"])


tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Podemos crear una funcion, cambiar_turno() que rota el deque de turnos y devuelve
# el jugador activo


def cambiar_turno():
    turno.rotate()
    return turno[0]

