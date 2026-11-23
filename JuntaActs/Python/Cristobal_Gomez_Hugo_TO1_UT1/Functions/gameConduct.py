"""Gestiona las jugadas y el historial de la sesión.

resultados y acciones_ordenador guardan datos de las mismas partidas
en el mismo orden. El historial se conserva en memoria durante la ejecución.
"""

import random
from Enumerations.gameResults import GameResult
from Functions import statictics

resultados = []
acciones_ordenador = []

def get_user_action():
    """Solicita una jugada y evalúa la partida contra el ordenador.

    Convierte las opciones del menú (1, 2, 3) a valores internos (0, 1, 2).
    Repite la solicitud si el número queda fuera del rango permitido.
    Si ocurre una excepción, muestra el error y termina esta llamada.
    No devuelve ningún valor explícito.
    """
    try:
        jugada = int(input("Seleccione su jugada: ")) -1
        while(jugada not in [0, 1, 2]):
            print("Elija una jugada válida")
            jugada = int(input("Seleccione su jugada: ")) -1
        asses_game(jugada, get_computer_action())
    except (ValueError, EOFError) as e:
        print("Ocurrió un error: ", e)  

def get_computer_action():
    """Genera aleatoriamente la jugada del ordenador.

    Returns:
        int: Número entre 0 y 2, ambos incluidos: 0 representa piedra,
        1 representa papel y 2 representa tijeras.
    """
    return random.randint(0,2)

def asses_game(jug_usuario, jug_ordenador):
    """Compara las jugadas, registra el resultado y muestra el historial.

    Args:
        jug_usuario (int): Jugada del usuario: 0 (piedra), 1 (papel)
            o 2 (tijeras).
        jug_ordenador (int): Jugada del ordenador con la misma codificación.

    Guarda VICTORIA, DERROTA o EMPATE y la jugada del ordenador en las
    listas de la sesión. No devuelve ning?n valor explícito.
    """
    resultado = ""
    if(jug_usuario == jug_ordenador):
        resultado = "EMPATE"
    elif((jug_usuario == 0 and jug_ordenador == 2) or (jug_usuario == 1 and jug_ordenador == 0) or (jug_usuario == 2 and jug_ordenador == 1)):
        resultado = "VICTORIA"
    else:
        resultado = "DERROTA"

    print(GameResult[resultado].value)
    statictics.update_statistics(resultados, acciones_ordenador, resultado, jug_ordenador)
    statictics.display_statistics(resultados, acciones_ordenador)
