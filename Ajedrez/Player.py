from Ajedrez.King import King


class Player():
    #  Funcion que verifica si un jugador tiene a su King en el tablero de ajedrez
    def __init__(self, board):
        self.board = board

    def has_king(self, color):
        return self.has_piece(color, King)

    #  Funcion que verifica si un jugador tiene piezas en el tablero de ajedrez
    def has_piece(self, color, piece_type):
        for row in self.board.board:
            if self.has_piece_in_row(row, color, piece_type):
                return True
        return False

    def has_piece_in_row(self, row, color, piece_type):
        for piece in row:
            if self.is_piece_of_color(piece, color, piece_type):
                return True
        return False

    def has_pieces(self, color):
        for row in self.board.board:
            if self.row_has_piece_of_color(row, color):
                return True
        return False

    def row_has_piece_of_color(self, row, color):
        for piece in row:
            if piece and piece.get_color() == color:
                return True
        return False

    def is_piece_of_color(self, piece, color, piece_type):
        return isinstance(piece, piece_type) and piece.get_color() == color
