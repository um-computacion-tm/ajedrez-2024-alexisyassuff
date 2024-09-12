import unittest
from Ajedrez.Piece import Piece
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


if __name__ == '__main__':
    unittest.main()
