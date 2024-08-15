from Piece import Piece


class Rook(Piece):
    def __init__(self, x, y, color):
        # Inicializar torres blancos y negros
        if color == 'white':
            icon = 'RW'
        elif color == "black":
            icon = 'RB'

        super().__init__(x, y, color, icon)
