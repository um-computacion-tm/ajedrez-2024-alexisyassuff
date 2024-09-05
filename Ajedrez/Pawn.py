from Ajedrez.Piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, color):
        # Inicializar peones blancos y negros
        if color == 'white':
            icon = 'PW'
        elif color == "black":
            icon = 'PB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.__color__ == 'white':
            return self.is_valid_white_move(new_x, new_y, board)
        else:
            return self.is_valid_black_move(new_x, new_y, board)

    def is_valid_white_move(self, new_x, new_y, board):
        if self.is_initial_move(new_x, new_y):
            return True
        if self.is_forward_move(new_x, new_y):
            return True
        if self.is_capture_move(new_x, new_y, board):
            return True
        return False

    def is_valid_black_move(self, new_x, new_y, board):
        if self.is_initial_move(new_x, new_y, is_black=True):
            return True
        if self.is_forward_move(new_x, new_y, is_black=True):
            return True
        if self.is_capture_move(new_x, new_y, board, is_black=True):
            return True
        return False

    def is_initial_move(self, new_x, new_y, is_black=False):
        return (self.is_same_column(new_x) and
                self.is_valid_initial_row(is_black) and
                self.is_valid_initial_move(new_y, is_black))

    def is_forward_move(self, new_x, new_y, is_black=False):
        return self.is_same_column(new_x) and self.is_valid_forward_move(new_y, is_black)

    def is_capture_move(self, new_x, new_y, board, is_black=False):
        return (self.is_diagonal_move(new_x, new_y, is_black) and
                self.is_enemy_piece(new_x, new_y, board))

    def is_same_column(self, new_x):
        return new_x == self.__x__

    def is_valid_initial_row(self, is_black):
        return self.__y__ == 6 if is_black else self.__y__ == 1

    def is_valid_initial_move(self, new_y, is_black):
        direction = -1 if is_black else 1
        return new_y == self.__y__ + direction or new_y == self.__y__ + 2 * direction

    def is_valid_forward_move(self, new_y, is_black):
        direction = -1 if is_black else 1
        return new_y == self.__y__ + direction

    def is_diagonal_move(self, new_x, new_y, is_black):
        direction = -1 if is_black else 1
        return abs(new_x - self.__x__) == 1 and new_y == self.__y__ + direction

    def is_enemy_piece(self, new_x, new_y, board):
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() != self.__color__
