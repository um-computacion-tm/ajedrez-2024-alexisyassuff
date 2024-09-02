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
        return abs(new_x - self.x) == abs(new_y - self.y) and (new_x != self.x and new_y != self.y)

    def is_path_clear(self, new_x, new_y, board):
        dx = 1 if new_x > self.x else -1
        dy = 1 if new_y > self.y else -1
        x, y = self.x + dx, self.y + dy
        while x != new_x and y != new_y:
            if board.get_piece_at(x, y):
                return False
            x += dx
            y += dy
        return True

    def is_same_color_piece(self, new_x, new_y, board):
        # Verificar si la nueva posición está ocupada por una pieza del mismo color
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() == self.color

    def is_valid_move(self, new_x, new_y, board):
        if self.is_diagonal_move(new_x, new_y) and self.is_path_clear(new_x, new_y, board) and not self.is_same_color_piece(new_x, new_y, board):
            return True
        return False

    def is_diagonal_move(self, new_x, new_y):
        return abs(new_x - self.x) == abs(new_y - self.y) and (new_x != self.x and new_y != self.y)

    def is_path_clear(self, new_x, new_y, board):
        dx = 1 if new_x > self.x else -1
        dy = 1 if new_y > self.y else -1
        x, y = self.x + dx, self.y + dy
        while x != new_x and y != new_y:
            if board.get_piece_at(x, y):
                return False
            x += dx
            y += dy
        return True

    def is_same_color_piece(self, new_x, new_y, board):
        # Verificar si la nueva posición está ocupada por una pieza del mismo color
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() == self.color
