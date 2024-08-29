from Ajedrez.Piece import Piece


class Knight(Piece):
    def __init__(self, x, y, color):
        # Inicializar reyes blancos y negros
        if color == 'white':
            icon = 'KW'
        elif color == "black":
            icon = 'KB'

        super().__init__(x, y, color, icon)
