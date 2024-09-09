from Ajedrez.Board import Board


class Piece:
    def __init__(self, x, y, color, icon):
        self.__x__ = x
        self.__y__ = y
        self.__color__ = color
        self.__icon__ = icon

    def get_position(self):
        return self.__x__, self.__y__

    def set_position(self, x, y):
        self.__x__ = x
        self.__y__ = y

    def get_color(self):
        return self.__color__

    def get_icon(self):
        return self.__icon__

    def is_same_color_piece(self, new_x, new_y, board):
        # Verificar si la nueva posición está ocupada por una pieza del mismo color
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() == self.__color__

    def is_valid_piece_move(self, new_x, new_y, board):
        raise NotImplementedError(
            "Este método debe ser implementado por las subclases")

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
