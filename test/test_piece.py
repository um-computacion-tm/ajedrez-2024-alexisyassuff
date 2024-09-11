import unittest
from Ajedrez.Piece import Piece
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Knight import Knight
from Ajedrez.Pawn import Pawn
from Ajedrez.Board import Board


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.piece = Piece(4, 4, 'white', 'P')

    def test_get_position(self):
        self.assertEqual(self.piece.get_position(), (4, 4))

    def test_set_position(self):
        self.piece.set_position(2, 3)
        self.assertEqual(self.piece.get_position(), (2, 3))

    def test_get_color(self):
        self.assertEqual(self.piece.get_color(), 'white')

    def test_get_icon(self):
        self.assertEqual(self.piece.get_icon(), 'P')

    def test_is_valid_move_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.piece.is_valid_piece_move(5, 5, self.board)


if __name__ == '__main__':
    unittest.main()
