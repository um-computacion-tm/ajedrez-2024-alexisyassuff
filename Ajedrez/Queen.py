from Piece import Piece

# Clase de Reina


class Queen(Piece):
    def __init__(self, x, y, color):
        # Inicializar peones blancos y negros
        if color == 'white':
            icon = 'QW'
        elif color == "black":
            icon = 'QB'

        super().__init__(x, y, color, icon)
