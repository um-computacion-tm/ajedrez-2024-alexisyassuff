from Ajedrez.Board import Board


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

    def is_valid_move(self, new_x, new_y):
        raise NotImplementedError(
            "Este método debe ser implementado por las subclases")
