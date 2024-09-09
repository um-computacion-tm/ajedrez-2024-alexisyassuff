from Ajedrez.Piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, color):
        # Inicializar reyes blancos y negros
        if color == 'white':
            icon = 'BW'
        elif color == "black":
            icon = 'BB'

        super().__init__(x, y, color, icon)

    def is_valid_move(self, new_x, new_y, board):
        if self.is_diagonal_move(new_x, new_y) and self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False

    def is_diagonal_move(self, new_x, new_y):
        return abs(new_x - self.__x__) == abs(new_y - self.__y__) and (new_x != self.__x__ and new_y != self.__y__)
