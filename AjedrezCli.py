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

# Se inicializan las piezas en el tablero
    def initialize_pieces(self):
        self.initialize_pawns(1, 'white')
        self.initialize_rooks(0, 'white')
        self.initialize_knights(0, 'white')
        self.initialize_bishops(0, 'white')
        self.initialize_queen(0, 'white')
        self.initialize_king(0, 'white')
        self.initialize_pawns(6, 'black')
        self.initialize_rooks(7, 'black')
        self.initialize_knights(7, 'black')
        self.initialize_bishops(7, 'black')
        self.initialize_queen(7, 'black')
        self.initialize_king(7, 'black')

    def initialize_pawns(self, row, color):
        for i in range(8):
            pawn = Pawn(i, row, color)
            self.board.place_piece(pawn)

    def initialize_rooks(self, row, color):
        positions = [0, 7]
        for i in positions:
            rook = Rook(i, row, color)
            self.board.place_piece(rook)

    def initialize_knights(self, row, color):
        positions = [1, 6]
        for i in positions:
            knight = Knight(i, row, color)
            self.board.place_piece(knight)

    def initialize_bishops(self, row, color):
        positions = [2, 5]
        for i in positions:
            bishop = Bishop(i, row, color)
            self.board.place_piece(bishop)

    def initialize_queen(self, row, color):
        queen = Queen(3, row, color)
        self.board.place_piece(queen)

    def initialize_king(self, row, color):
        king = King(4, row, color)
        self.board.place_piece(king)

    # Funcion del controlador que gestiona los flujos de juego con prints e input para el movimiento de pieza
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

    # Convierte coordenadas de Ajedrez en coordenadas de matriz
    def get_positions_from_notation(self, origin, destination):
        x1, y1 = self.board.get_position_from_notation(origin)
        x2, y2 = self.board.get_position_from_notation(destination)
        return x1, y1, x2, y2

    # Metodo donde se verifica si el movimiento es válido y se mueve la pieza si es así
    def attempt_move(self, x1, y1, x2, y2):
        piece = self.board.get_piece_at(x1, y1)
        if self.is_valid_piece(piece):
            self.handle_move(piece, x2, y2)
        else:
            self.invalid_move_message()

    def is_valid_piece(self, piece):
        return piece and piece.get_color() == self.current_turn

    def handle_move(self, piece, x2, y2):
        if self.is_valid_move_for_piece(piece, x2, y2):
            self.execute_piece_move(piece, x2, y2)
        else:
            self.invalid_move_message()

    def is_valid_move_for_piece(self, piece, x2, y2):
        return piece.is_valid_move(x2, y2, self.board)

    def execute_piece_move(self, piece, x2, y2):
        if self.board.move_piece(piece, x2, y2):
            self.check_pawn_promotion(piece, x2, y2)
            self.winner_move()

    def check_pawn_promotion(self, piece, x2, y2):
        if isinstance(piece, Pawn) and piece.is_promotion_move(y2):
            self.promote_pawn(piece, x2, y2)

    def invalid_move_message(self):
        print("No hay pieza en la posición inicial o no es tu turno")

    # Funcion que gestiona la declaracion de ganador del juego y la finalizacion cuando hay un movimiento ganador

    def winner_move(self):
        self.switch_turn_and_get_other_player()
        if not self.has_pieces(self.current_turn):
            self.declare_winner()
            self.game_over = True
        elif not self.has_king(self.current_turn):
            print("¡Atencion! Rey capturado")
            self.declare_winner()
            self.game_over = True

    #  Funcion que verifica si un jugador tiene a su King en el tablero de ajedrez

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

    def is_piece_of_color(self, piece, color, piece_type):
        return isinstance(piece, piece_type) and piece.get_color() == color

    def is_valid_piece_move(self, piece, x2, y2):
        return piece and self.is_valid_move(piece) and self.board.is_valid_destination(piece, x2, y2)

    def is_valid_move(self, piece):
        return piece and piece.get_color() == self.current_turn

    # Funcion que determina si el jugador tiene piezas en su poder

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

    # Funcion de bucle para que si un jugador se rinde, el otro tambien lo haga
    def handle_surrender(self):
        print(f"El jugador {self.current_turn} se ha rendido.")
        for i in range(1000):
            if self.other_player_surrendered():
                print(
                    "Ambos jugadores han pactado la rendida. El juego termina en empate.")
                self.game_over = True
                break
            else:
                continue

    # Verifica  si el oponente se ha rendido luego de que un jugador lo haga

    def other_player_surrendered(self):
        return self.get_user_input(f"El jugador oponente debe presionar 'q' y rendirse: ").lower() == 'q'

    # Metodo que cambia el turno actual y deveulve el color del jugador que tiene el turno siguiente
    def switch_turn_and_get_other_player(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        return self.current_turn

    # Método que declara el ganador del juego
    def declare_winner(self):
        winner = 'black' if self.current_turn == 'white' else 'white'
        print(f"El jugador {winner} ha ganado la partida.")

    # Funcion de prints e inputs para promover un peón a otra pieza cuando llega al final del tablero
    def promote_pawn(self, pawn, new_x, new_y):
        print("El peón ha llegado al final del tablero, Elegì de las opciones, la nueva pieza:")
        print("1. Queen")
        print("2. Rook ")
        print("3. Bishop ")
        print("4. Knight ")
        choice = input("Elige una opción (1-4): ")

        if choice == '1':
            new_piece = Queen(new_x, new_y, pawn.get_color())
        elif choice == '2':
            new_piece = Rook(new_x, new_y, pawn.get_color())
        elif choice == '3':
            new_piece = Bishop(new_x, new_y, pawn.get_color())
        elif choice == '4':
            new_piece = Knight(new_x, new_y, pawn.get_color())
        else:
            print("Opción inválida. Se selecciona Queen por defecto.")
            new_piece = Queen(new_x, new_y, pawn.get_color())

        self.board.promote_pawn(pawn, new_x, new_y, new_piece)
