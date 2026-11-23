"""Actualiza y muestra el historial de partidas de la sesión."""

from Enumerations.gameActions import GameAction
from Enumerations.gameResults import GameResult


def update_statistics(resultados, acciones_ordenador, resultado, accion_ordenador):
    """Añade el resultado y la jugada del ordenador al historial.

    Args:
        resultados (list[str]): Lista de resultados de las partidas.
        acciones_ordenador (list[int]): Lista de jugadas del ordenador.
        resultado (str): Nombre del resultado: VICTORIA, DERROTA o EMPATE.
        accion_ordenador (int): Jugada del ordenador: 0, 1 o 2.

    Modifica las listas recibidas manteniendo la correspondencia entre
    cada resultado y su jugada. No devuelve ning?n valor explícito.
    """
    try:
        resultados.append(resultado)
        acciones_ordenador.append(accion_ordenador)
    except AttributeError as e:
        print("Ocurrió un error al actualizar las estadísticas: ", e)

def display_statistics(resultados, acciones_ordenador):
    """Muestra el resultado y la jugada del ordenador de cada partida.

    Args:
        resultados (list[str]): Nombres de los resultados registrados.
        acciones_ordenador (list[int]): Jugadas del ordenador (0, 1 o 2),
            en el mismo orden que los resultados.

    zip() empareja las listas hasta agotar la más corta. enumerate()
    numera las partidas desde cero. Las enumeraciones proporcionan
    el texto del resultado y el nombre de la jugada.
    No modifica las listas ni devuelve ningún valor explícito.
    """
    try:
        for indice, (resultado, accion_ordenador) in enumerate(zip(resultados, acciones_ordenador)):
            print("El resultado de la partida {} es: {} y el ordenador realizo la accion {}".format(indice, GameResult[resultado].value, GameAction(accion_ordenador).name))
    except (KeyError, ValueError, TypeError) as e:
        print("Ocurrió un error al mostrar las estadísticas: ", e)

    print("Estadísticas de la sesión:")
    print("Nº de victorias: {}".format(resultados.count("VICTORIA")))
    print("Nº de derrotas: {}".format(resultados.count("DERROTA")))
    print("Nº de empates: {}\n".format(resultados.count("EMPATE")))
    print("Nº de veces que el ordenador jugó piedra: {}".format(acciones_ordenador.count(0)))
    print("Nº de veces que el ordenador jugó papel: {}".format(acciones_ordenador.count(1)))
    print("Nº de veces que el ordenador jugó tijeras: {}".format(acciones_ordenador.count(2)))