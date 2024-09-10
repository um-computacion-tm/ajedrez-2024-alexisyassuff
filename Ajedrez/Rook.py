from Ajedrez.Piece import Piece


class Rook(Piece):
    def __init__(self, x, y, color):
        # Inicializar torres blancos y negros
        if color == 'white':
            icon = 'RW'
        elif color == "black":
            icon = 'RB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_straight_move(new_x, new_y) and self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False
