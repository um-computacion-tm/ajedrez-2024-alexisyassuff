from Ajedrez.Piece import Piece


class Pawn(Piece):
    white_icon = '♟'
    black_icon = '♙'

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, new_x, new_y, board):
        if self.__color__ == 'white':
            return (self.is_initial_move(new_x, new_y, board) or
                    self.is_forward_move(new_x, new_y, board) or
                    self.is_capture_move(new_x, new_y, board))

        else:
            return (self.is_initial_move(new_x, new_y, board, is_black=True) or
                    self.is_forward_move(new_x, new_y, board, is_black=True) or
                    self.is_capture_move(new_x, new_y, board, is_black=True))

    def is_initial_move(self, new_x, new_y, board, is_black=False):
        direction = -1 if is_black else 1

        # El movimiento inicial debe ser en la misma columna y en la fila inicial
        if not (self.is_same_column(new_x) and self.is_valid_initial_row(is_black)):
            return False

        # Si es un movimiento de 2 casillas, ambas deben estar vacías
        if new_y == self.__y__ + 2 * direction:
            return (not self.has_piece_ahead(self.__y__ + direction, board) and
                    not self.has_piece_ahead(self.__y__ + 2 * direction, board))

        # Si es un movimiento de 1 casilla, la siguiente casilla debe estar vacía
        if new_y == self.__y__ + direction:
            return not self.has_piece_ahead(self.__y__ + direction, board)

        return False

    def is_forward_move(self, new_x, new_y, board, is_black=False):
        direction = -1 if is_black else 1

        # El movimiento hacia adelante debe ser en la misma columna y solo 1 casilla
        return (self.is_same_column(new_x) and
                new_y == self.__y__ + direction and
                not self.has_piece_ahead(new_y, board))

    def is_same_column(self, new_x):
        return new_x == self.__x__

    def is_valid_initial_row(self, is_black):
        return self.__y__ == 6 if is_black else self.__y__ == 1

    def is_valid_initial_move(self, new_y, is_black):
        direction = -1 if is_black else 1
        return new_y == self.__y__ + direction or new_y == self.__y__ + 2 * direction

    def is_valid_forward_move(self, new_y, board, is_black):
        direction = -1 if is_black else 1
        return new_y == self.__y__ + direction and not self.has_piece_ahead(new_y, board)

    def has_piece_ahead(self, new_y, board):
        return board.get_piece_at(self.__x__, new_y) is not None

    def is_capture_move(self, new_x, new_y, board, is_black=False):
        return (self.is_diagonal_capture_move(new_x, new_y, is_black) and
                self.is_enemy_piece(new_x, new_y, board))

    def is_diagonal_capture_move(self, new_x, new_y, is_black):
        direction = -1 if is_black else 1
        return abs(new_x - self.__x__) == 1 and new_y == self.__y__ + direction

    def is_enemy_piece(self, new_x, new_y, board):
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() != self.__color__

    def is_promotion_move(self, new_y):
        return (self.__color__ == 'white' and new_y == 7) or (self.__color__ == 'black' and new_y == 0)
