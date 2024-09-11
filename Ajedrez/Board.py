

class Board:
    def __init__(self):
        # Matriz vacia 8x8 y cada casilla inicializa como None
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece):
        x, y = piece.get_position()
        self.board[y][x] = piece

    def move_piece(self, piece, new_x, new_y):
        if piece.is_valid_move(new_x, new_y, self):
            # La posicion actual de la pieza, se guarda en variables
            old_x, old_y = piece.get_position()

            # Se vacia la posicion anterior
            self.board[old_y][old_x] = None

            # Si hay una pieza en la nueva posición, se elimina
            if self.board[new_y][new_x]:
                self.board[new_y][new_x] = None

            # Para insertar la nueva pieza en el lugar
            self.board[new_y][new_x] = piece
            piece.set_position(new_x, new_y)
            return True
        return False

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
