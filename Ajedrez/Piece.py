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
