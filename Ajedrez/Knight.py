from Ajedrez.Piece import Piece


class Knight(Piece):
    def __init__(self, x, y, color):
        if color == 'white':
            icon = '♞'
        elif color == "black":
            icon = '♘'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        return self.is_knight_move(new_x, new_y) and not self.is_same_color_piece(new_x, new_y, board)

    def is_knight_move(self, new_x, new_y):
        return (abs(new_x - self.__x__), abs(new_y - self.__y__)) in [(1, 2), (2, 1)]
