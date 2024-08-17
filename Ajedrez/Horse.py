from Ajedrez.Piece import Piece


class Horse(Piece):
    def __init__(self, x, y, color):
        # Inicializar reyes blancos y negros
        if color == 'white':
            icon = 'HW'
        elif color == "black":
            icon = 'HB'

        super().__init__(x, y, color, icon)
