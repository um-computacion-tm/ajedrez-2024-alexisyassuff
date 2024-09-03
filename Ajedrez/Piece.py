class Piece:
    def __init__(self, x, y, color, icon):
        self.x = x
        self.y = y
        self.color = color
        self.icon = icon

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_color(self):
        return self.color

    def get_icon(self):
        return self.icon

    def is_same_color_piece(self, new_x, new_y, board):
        # Verificar si la nueva posición está ocupada por una pieza del mismo color
        target_piece = board.get_piece_at(new_x, new_y)
        return target_piece and target_piece.get_color() == self.color

    def is_valid_piece_move(self, new_x, new_y, board):
        raise NotImplementedError(
            "Este método debe ser implementado por las subclases")
