from Ajedrez.Piece import Piece


class Knight(Piece):
    def __init__(self, x, y, color):
        # Inicializar reyes blancos y negros
        if color == 'white':
            icon = 'KnW'
        elif color == "black":
            icon = 'KnB'

        super().__init__(x, y, color, icon)
