from Ajedrez.Board import Board
from Ajedrez.Pawn import Pawn
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Horse import Horse


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def initialize_pieces(self):

        # -----------PIEZAS BLANCAS - ---------------
        for i in range(8):
            pawn = Pawn(i, 1, 'white')
            self.board.place_piece(pawn)

        positions = [0, 7]
        for i in positions:
            rook = Rook(i, 0, 'white')
            self.board.place_piece(rook)

        positions = [1, 6]
        for i in positions:
            horse = Horse(i, 0, 'white')
            self.board.place_piece(horse)

        positions = [2, 5]
        for i in positions:
            bishop = Bishop(i, 0, 'white')
            self.board.place_piece(bishop)

        queen = Queen(3, 0, "white")
        self.board.place_piece(queen)
        king = King(4, 0, "white")
        self.board.place_piece(king)

        # -----------PIEZAS NEGRAS - ---------------
        for i in range(8):
            pawn = Pawn(i, 6, 'black')
            self.board.place_piece(pawn)

        positions = [0, 7]
        for i in positions:
            rook = Rook(i, 7, 'black')
            self.board.place_piece(rook)

        positions = [1, 6]
        for i in positions:
            horse = Horse(i, 7, 'black')
            self.board.place_piece(horse)

        positions = [2, 5]
        for i in positions:
            bishop = Bishop(i, 7, 'black')
            self.board.place_piece(bishop)

        queen = Queen(3, 7, "black")
        self.board.place_piece(queen)

        king = King(4, 7, "black")
        self.board.place_piece(king)

    # def play_turn(self):
        self.board.print_board()
        print(f"Turno de {self.current_turn}")
        origin = input("Ingrese la posición de origen (por ejemplo, D2): ")
        destination = input(
            "Ingrese la posición de destino (por ejemplo, D3): ")

        try:
            # Se convierten las ubicaciones de origen y destino a coordenadas
            x1, y1 = self.board.get_position_from_notation(origin)
            x2, y2 = self.board.get_position_from_notation(destination)
            piece = self.board.get_piece_at(x1, y1)

            # Verifica si la pieza y color son pertenecientes al turno de quien la toca
            if piece and piece.get_color() == self.current_turn:
                # Mover pieza si movimiento es valido
                if self.board.move_piece(piece, x2, y2):
                    self.current_turn = 'black' if self.current_turn == 'white' else 'white'
                else:
                    print("Movimiento no válido")
            else:
                print("No hay pieza en la posición inicial o no es tu turno")
        except (ValueError, IndexError):
            print("Entrada inválida")

        return True

    def start(self):
        self.initialize_pieces()
        while self.play_turn():
            pass
        print("Juego terminado")
