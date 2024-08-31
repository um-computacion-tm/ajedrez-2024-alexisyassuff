from Ajedrez.Board import Board
from Ajedrez.Pawn import Pawn
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Knight import Knight


class AjedrezCli:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'
        self.game_over = False  # Variable para controlar si el juego terminó

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
            knight = Knight(i, 0, 'white')
            self.board.place_piece(knight)

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
            knight = Knight(i, 7, 'black')
            self.board.place_piece(knight)

        positions = [2, 5]
        for i in positions:
            bishop = Bishop(i, 7, 'black')
            self.board.place_piece(bishop)

        queen = Queen(3, 7, "black")
        self.board.place_piece(queen)

        king = King(4, 7, "black")
        self.board.place_piece(king)

    def play_turn(self):
        if self.game_over:
            return False  # Terminar el juego si game_over es True

        self.board.print_board()
        print(f"Turno de {self.current_turn}")

        origin = self.get_user_input(
            "Ingrese la posición de origen (por ejemplo, D2) o 'q' para rendirse: ")
        if origin.lower() == 'q':
            self.handle_surrender()
            return False  # Indicar que el juego ha terminado

        destination = self.get_user_input(
            "Ingrese la posición de destino (por ejemplo, D3): ")

        try:
            x1, y1, x2, y2 = self.get_positions_from_notation(
                origin, destination)
            self.attempt_move(x1, y1, x2, y2)
        except (ValueError, IndexError):
            print("Entrada inválida")

        return True  # Continuar el juego

    def get_user_input(self, prompt):
        return input(prompt)

    def get_positions_from_notation(self, origin, destination):
        x1, y1 = self.board.get_position_from_notation(origin)
        x2, y2 = self.board.get_position_from_notation(destination)
        return x1, y1, x2, y2

    def attempt_move(self, x1, y1, x2, y2):
        piece = self.board.get_piece_at(x1, y1)
        if self.is_valid_move(piece):
            if self.board.move_piece(piece, x2, y2):
                self.switch_turn()
            else:
                print("Movimiento no válido")
        else:
            print("No hay pieza en la posición inicial o no es tu turno")

    def is_valid_move(self, piece):
        return piece and piece.get_color() == self.current_turn

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
