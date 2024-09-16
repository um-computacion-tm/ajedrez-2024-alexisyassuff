from Ajedrez.Piece import Piece


class Bishop(Piece):
    white_icon = '♝'
    black_icon = '♗'

    def __init__(self, x, y, color):

        super().__init__(x, y, color)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_diagonal_move(new_x, new_y) and self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False
