"""Define los valores internos de las jugadas del juego."""

from enum import IntEnum


class GameAction(IntEnum):
    """Representa las jugadas posibles mediante valores enteros.

    Attributes:
        Piedra: Jugada con valor 0.
        Papel: Jugada con valor 1.
        Tijeras: Jugada con valor 2.
    """
    Piedra = 0
    Papel = 1
    Tijeras = 2