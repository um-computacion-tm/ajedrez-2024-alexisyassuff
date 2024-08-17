class Board:
    def __init__(self):
        # Matriz vacia 8x8 y cada casilla inicializa como None
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece):
        x, y = piece.get_position()
        self.board[y][x] = piece
