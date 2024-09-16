from Ajedrez.Piece import Piece


class King(Piece):
    white_icon = '♚'
    black_icon = '♔'

    def __init__(self, x, y, color):

        super().__init__(x, y, color)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_adjacent_move(new_x, new_y) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False

    def is_adjacent_move(self, new_x, new_y):
        return abs(new_x - self.__x__) <= 1 and abs(new_y - self.__y__) <= 1
