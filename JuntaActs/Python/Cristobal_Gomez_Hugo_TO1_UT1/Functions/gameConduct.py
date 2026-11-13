import random
from Enumerations.gameActions import GameAction
from Enumerations.gameResults import GameResult
from Functions import statictics

resultados = []
accionesOrdenador = []

def get_user_action():
    jugada = input("Seleccione su jugada: ")
    if(jugada == None and (jugada not in range(0,3))):
        print("Elija una jugada válida")
        get_user_action()
    asses_game(jugada, get_computer_action())
    

def get_computer_action():
    return random.randint(0,2)

def asses_game(jug_usuario, jug_ordenador):
    resultado = ""
    if(jug_usuario == jug_ordenador):
        resultado = "EMPATE"
    elif((jug_usuario == 0 and jug_ordenador == 3) or (jug_usuario == 1 and jug_ordenador == 0) or (jug_usuario == 3 and jug_ordenador == 2)):
        resultado = "VICTORIA"
    else:
        resultado = "DERROTA"

    print(GameResult[resultado].value)
    statictics.update_statistics(resultados, accionesOrdenador, resultado, jug_ordenador)
    statictics.display_statistics(resultados, GameAction(jug_ordenador).name)
