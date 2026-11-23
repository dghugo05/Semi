"""Inicia el juego de piedra, papel o tijeras desde la consola."""

from Functions import gameConduct as game_conduct

def game():
    """Muestra el menú, juega una partida y ofrece repetirla.

    Si la respuesta es "1", llama a play_another(). No devuelve un valor.
    """
    try:
        print("Bienvenido al juego: ¡Bienvenido al Piedra, Papel o Tijera!")
        print("Estas son las opciones:\n 1. Piedra\n 2. Papel\n 3. Tijeras")
        game_conduct.get_user_action()
        
        if(input("¿Quieres jugar otra?\n 1. Si\n 2. No\n ") == "1"): play_another()
    except EOFError as e:
        print("Ocurrió un error: ", e)
        game()


def play_another():
    """Inicia otra partida mediante una llamada recursiva a game()."""
    game()

game()
print("Gracias por jugar")

