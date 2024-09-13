from Ajedrez.Pawn import Pawn
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Knight import Knight


class Board:
    def __init__(self):
        # Matriz vacia 8x8 y cada casilla inicializa como None
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        # self.initialize_pawns(1, 'white')
        self.initialize_rooks(0, 'white')
        # self.initialize_knights(0, 'white')
        # self.initialize_bishops(0, 'white')
        self.initialize_queen(0, 'white')
        self.initialize_king(0, 'white')
        # self.initialize_pawns(6, 'black')
        self.initialize_rooks(7, 'black')
        # self.initialize_knights(7, 'black')
        # self.initialize_bishops(7, 'black')
        self.initialize_queen(7, 'black')
        self.initialize_king(7, 'black')

    def initialize_pawns(self, row, color):
        for i in range(8):
            pawn = Pawn(i, row, color)
            self.place_piece(pawn)

    def initialize_rooks(self, row, color):
        positions = [0, 7]
        for i in positions:
            rook = Rook(i, row, color)
            self.place_piece(rook)

    def initialize_knights(self, row, color):
        positions = [1, 6]
        for i in positions:
            knight = Knight(i, row, color)
            self.place_piece(knight)

    def initialize_bishops(self, row, color):
        positions = [2, 5]
        for i in positions:
            bishop = Bishop(i, row, color)
            self.place_piece(bishop)

    def initialize_queen(self, row, color):
        queen = Queen(3, row, color)
        self.place_piece(queen)

    def initialize_king(self, row, color):
        king = King(4, row, color)
        self.place_piece(king)

    def place_piece(self, piece):
        x, y = piece.get_position()
        self.board[y][x] = piece

    def move_piece(self, piece, new_x, new_y):
        if piece.is_valid_move(new_x, new_y, self):
            # La posicion actual de la pieza, se guarda en variables
            old_x, old_y = piece.get_position()
            # Se vacia la posicion anterior
            self.board[old_y][old_x] = None
            # Para insertar la nueva pieza en el lugar
            self.board[new_y][new_x] = piece
            piece.set_position(new_x, new_y)
            return True
        return False

    def remove_piece_at(self, x, y):
        self.board[y][x] = None

    def print_board(self):
        self.mark_superior()
        self.for_print_board()
        self.mark_inferior()

    def mark_superior(self):
        print("    A    B    C    D    E    F    G    H")
        print("  +---------------------------------------+")

    def mark_inferior(self):
        print("  +---------------------------------------+")
        print("    A    B    C    D    E    F    G    H")

    def for_print_board(self):
        for i in range(8):
            self.print_row(i)

    def print_row(self, row_index):
        print(f"{8 - row_index} |", end=" ")
        for j in range(8):
            self.print_piece(self.board[row_index][j])
        print("|")

    def print_piece(self, piece):
        if piece:
            print(f"{piece.get_icon():<4}", end=" ")
        else:
            print(".   ", end=" ")

    def get_piece_at(self, x, y):
        return self.board[y][x]

    def get_position_from_notation(self, notation):
        col = ord(notation[0]) - ord('a')
        row = 8 - int(notation[1])
        return col, row

# Insercion de la nueva pieza en tablero tras el cambio de pieza peon
    def promote_pawn(self, pawn, new_x, new_y, new_piece):
        old_x, old_y = pawn.get_position()
        self.board[old_y][old_x] = None
        self.board[new_y][new_x] = new_piece
        new_piece.set_position(new_x, new_y)
