import unittest
from Piece import Piece
from Ajedrez.Queen import Queen


class TestPiece(unittest.TestCase):
    def setUp(self):
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


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.queen_white = Queen(3, 3, 'white')
        self.queen_black = Queen(5, 5, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.queen_white.get_position(), (3, 3))

    def test_initial_position_black(self):
        self.assertEqual(self.queen_black.get_position(), (5, 5))

    def test_get_color_black(self):
        self.assertEqual(self.queen_black.get_color(), 'black')

    def test_get_icon_white(self):
        self.assertEqual(self.queen_white.get_icon(), 'QW')


if __name__ == '__main__':
    unittest.main()
