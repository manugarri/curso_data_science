# -*- coding: utf-8 -*-
"""
Aquí se muestra una solución del programa tres en raya.

@author: manugarri
"""
from collections import deque

turno = deque(["O", "X"])
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def cambiar_turno():
    turno.rotate()
    return turno[0]


def mostrar_tablero():
    print("")
    for row in tablero:
        print([square for square in row])


def procesar_posicion(posicion):
    fila, columna = posicion.split(",")
    return int(fila) - 1, int(columna) - 1


def posicion_valida(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False


def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador


def evaluar_victoria(j):
    if tablero[0] == [j, j, j] or tablero[1] == [j, j, j] or tablero[2] == [j, j, j]:
        return True
    elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
        return True
    elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
        return True
    elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
        return True
    elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
        return True
    elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
        return True
    return False


def evaluar_empate():
    return set(tablero[0]).union(set(tablero[1])).union(set(tablero[2])) == set(["X", "O"])


def juego():
    jugador = cambiar_turno()
    while True:
        posicion_str = input("Jugador {}, elige una posición (fila,columna) de 1 a 3. 'salir' para salir: ".format(jugador))
        if posicion_str == "salir":
            print("Adios!")
            break
        try:
            posicion_procesada = procesar_posicion(posicion_str)
        except:
            print("Error, posicion {} no es válida. formato debe ser (fila, columna)".format(posicion_str))
            continue
        if posicion_valida(posicion_procesada):
            actualizar_tablero(posicion_procesada, jugador)
            mostrar_tablero()
            if evaluar_victoria(jugador):
                print("Jugador {} ha ganado!.\nAdios!".format(jugador))
                break
            if evaluar_empate():
                print("Empate!.\nAdios!")
                break
            jugador = cambiar_turno()
        else:
            print("Posicion {} no válida".format(posicion_str))


if __name__ == "__main__":
    juego()
