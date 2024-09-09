from Ajedrez.Piece import Piece


class Queen(Piece):
    def __init__(self, x, y, color):
        if color == 'white':
            icon = 'QW'
        elif color == "black":
            icon = 'QB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_straight_move(new_x, new_y) or self.is_diagonal_move(new_x, new_y):
            if self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board):
                return True
        return False

    def is_straight_move(self, new_x, new_y):
        return new_x == self.__x__ or new_y == self.__y__

    def is_diagonal_move(self, new_x, new_y):
        return abs(new_x - self.__x__) == abs(new_y - self.__y__) and (new_x != self.__x__ and new_y != self.__y__)
