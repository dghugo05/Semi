from Functions import gameConduct

def game():
    print("Bienvenido al juego: ¡Bienvenido al Piedra, Papel o Tijera!")
    print("Estas son las opciones:\n 1. Piedra\n 2. Papel\n 3. Tijeras")
    gameConduct.get_user_action()

    if(input("¿Quieres jugar otra?\n 1. Si\n 2. No\n ") == "Si" or 1): play_another()
    print("Gracias por jugar")

def play_another():
    game()


game()

