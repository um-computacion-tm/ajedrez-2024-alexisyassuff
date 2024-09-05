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

    def is_straight_move(self, new_x, new_y):
        return new_x == self.__x__ or new_y == self.__y__

    def is_path_clear(self, new_x, new_y, board):
        if new_x == self.__x__:
            return self.is_vertical_path_clear(new_y, board)
        else:
            return self.is_horizontal_path_clear(new_x, board)

    def is_vertical_path_clear(self, new_y, board):
        step = 1 if new_y > self.__y__ else -1
        for y in range(self.__y__ + step, new_y, step):
            if board.get_piece_at(self.__x__, y):
                return False
        return True

    def is_horizontal_path_clear(self, new_x, board):
        step = 1 if new_x > self.__x__ else -1
        for x in range(self.__x__ + step, new_x, step):
            if board.get_piece_at(x, self.__y__):
                return False
        return True
