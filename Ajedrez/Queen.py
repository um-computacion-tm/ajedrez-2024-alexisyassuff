from Ajedrez.Piece import Piece


class Queen(Piece):
    white_icon = "♛"
    black_icon = "♕"

    def __init__(self, x, y, color):

        super().__init__(x, y, color)

    def is_valid_move(self, new_x, new_y, board):
        return self.is_valid_straight_move(new_x, new_y, board) or self.is_valid_diagonal_move(new_x, new_y, board)
