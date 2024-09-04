from Ajedrez.Piece import Piece


class King(Piece):
    def __init__(self, x, y, color):
        if color == 'white':
            icon = 'KW'
        elif color == "black":
            icon = 'KB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_adjacent_move(new_x, new_y) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False

    def is_adjacent_move(self, new_x, new_y):
        return abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1
