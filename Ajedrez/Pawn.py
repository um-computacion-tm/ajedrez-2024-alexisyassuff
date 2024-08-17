from Ajedrez.Piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color):
        # Inicializar peones blancos y negros
        if color == 'white':
            icon = 'PW'
        elif color == "black":
            icon = 'PB'

        super().__init__(x, y, color, icon)
