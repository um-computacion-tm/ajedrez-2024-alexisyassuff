from Ajedrez.Piece import Piece


class Queen(Piece):
    def __init__(self, x, y, color):
        if color == 'white':
            icon = 'QW'
        elif color == "black":
            icon = 'QB'

        super().__init__(x, y, color, icon)
