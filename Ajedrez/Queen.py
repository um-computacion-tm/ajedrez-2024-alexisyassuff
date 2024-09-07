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

    def is_path_clear(self, new_x, new_y, board):
        if new_x == self.__x__:
            return self.is_vertical_path_clear(new_y, board)
        elif new_y == self.__y__:
            return self.is_horizontal_path_clear(new_x, board)
        else:
            return self.is_diagonal_path_clear(new_x, new_y, board)

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

    def is_diagonal_path_clear(self, new_x, new_y, board):
        dx = 1 if new_x > self.__x__ else -1
        dy = 1 if new_y > self.__y__ else -1
        x, y = self.__x__ + dx, self.__y__ + dy
        while x != new_x and y != new_y:
            if board.get_piece_at(x, y):
                return False
            x += dx
            y += dy
        return True
