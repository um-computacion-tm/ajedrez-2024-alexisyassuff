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

            # Movimiento diagonal para capturar pieza del color contrario
            if abs(new_x - self.x) == 1 and new_y == self.y + 1:
                target_piece = board.get_piece_at(new_x, new_y)
                if target_piece and target_piece.get_color() != self.color:
                    return True

        else:
            if self.y == 6:
                if new_x == self.x and (new_y == self.y - 1 or new_y == self.y - 2):
                    return True
            else:
                if new_x == self.x and new_y == self.y - 1:
                    return True

            # Movimiento diagonal para capturar pieza del color contrario
            if abs(new_x - self.x) == 1 and new_y == self.y - 1:
                target_piece = board.get_piece_at(new_x, new_y)
                if target_piece and target_piece.get_color() != self.color:
                    return True

        return False
