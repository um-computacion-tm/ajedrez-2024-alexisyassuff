from Piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, color):
        # Inicializar reyes blancos y negros
        if color == 'white':
            icon = 'BW'
        elif color == "black":
            icon = 'BB'

        super().__init__(x, y, color, icon)
