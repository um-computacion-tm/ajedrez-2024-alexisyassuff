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
        if self.color == 'white':
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
        if is_black:
            return new_x == self.x and (new_y == self.y - 1 or new_y == self.y - 2) and self.y == 6
        else:
            return new_x == self.x and (new_y == self.y + 1 or new_y == self.y + 2) and self.y == 1

    def is_forward_move(self, new_x, new_y, is_black=False):
        if is_black:
            return new_x == self.x and new_y == self.y - 1
        else:
            return new_x == self.x and new_y == self.y + 1

    def is_capture_move(self, new_x, new_y, board, is_black=False):
        if is_black:
            return abs(new_x - self.x) == 1 and new_y == self.y - 1 and self.is_enemy_piece(new_x, new_y, board)
        else:
            return abs(new_x - self.x) == 1 and new_y == self.y + 1 and self.is_enemy_piece(new_x, new_y, board)

    def is_enemy_piece(self, new_x, new_y, board):
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() != self.color
