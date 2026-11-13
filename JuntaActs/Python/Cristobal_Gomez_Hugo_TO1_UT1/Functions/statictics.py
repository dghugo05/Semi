def update_statistics(resultados, accionesOrdenador, resultado, accionOrdenador):
    resultados.append(resultado)
    accionesOrdenador.append(accionOrdenador)


def display_statistics(resultados, accionesOrdenador):
    for indice, (resultado, accionOrdenador) in enumerate(zip(resultados, accionesOrdenador)):
        print("El resultado de la partida {} es: {} y el ordenador realizo la accion {}".format(indice, resultado, accionOrdenador))