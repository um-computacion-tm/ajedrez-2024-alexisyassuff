from Ajedrez.Piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color):
        # Inicializar peones blancos y negros
        if color == 'white':
            icon = 'PW'
        elif color == "black":
            icon = 'PB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.color == 'white':
            if self.y == 1:  # Primer movimiento para blancas
                # El nuevo movimiento en x, debe ser si o si, en la misma columna
                # El nuevo movimiento en y, puede ser una posicion adelante o dos
                if new_x == self.x and (new_y == self.y + 1 or new_y == self.y + 2):
                    return True
            else:
                # Si el movimiento, no es el inicial solo se puede mover uno adelante en vertical
                if new_x == self.x and new_y == self.y + 1:
                    return True
