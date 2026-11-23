"""Define los resultados posibles de una partida."""

"""Define los resultados posibles de una partida."""

from enum import Enum

class GameResult(Enum):
    """Relaciona cada resultado con el texto mostrado al usuario.

    Attributes:
        VICTORIA: Resultado cuyo valor es "Victoria".
        DERROTA: Resultado cuyo valor es "Derrota".
        EMPATE: Resultado cuyo valor es "Empate".
    """
    """Relaciona cada resultado con el texto mostrado al usuario.

    Attributes:
        VICTORIA: Resultado cuyo valor es "Victoria".
        DERROTA: Resultado cuyo valor es "Derrota".
        EMPATE: Resultado cuyo valor es "Empate".
    """
    VICTORIA = "Victoria"
    DERROTA = "Derrota"
    EMPATE = "Empate"