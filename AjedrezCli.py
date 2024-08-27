from Ajedrez.Board import Board
from Ajedrez.Pawn import Pawn
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Horse import Horse


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
