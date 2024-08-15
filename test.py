import unittest
from Piece import Piece
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Horse import Horse


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
        self.queen_white = Queen(3, 0, 'white')
        self.queen_black = Queen(3, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.queen_white.get_position(), (3, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.queen_black.get_position(), (3, 7))

    def test_get_color_black(self):
        self.assertEqual(self.queen_black.get_color(), 'black')

    def test_get_icon_white(self):
        self.assertEqual(self.queen_white.get_icon(), 'QW')


class TestKing(unittest.TestCase):

    def setUp(self):
        self.king_white = King(4, 0, 'white')
        self.king_black = King(4, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.king_white.get_position(), (4, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.king_black.get_position(), (4, 7))

    def test_get_color_black(self):
        self.assertEqual(self.king_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.king_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.king_white.get_icon(), 'KW')

    def test_get_icon_black(self):
        self.assertEqual(self.king_black.get_icon(), 'KB')


class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook_white = Rook(1, 0, 'white')
        self.rook_black = Rook(1, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.rook_white.get_position(), (1, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.rook_black.get_position(), (1, 7))

    def test_get_color_black(self):
        self.assertEqual(self.rook_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.rook_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.rook_white.get_icon(), 'RW')

    def test_get_icon_black(self):
        self.assertEqual(self.rook_black.get_icon(), 'RB')


class TestHorse(unittest.TestCase):

    def setUp(self):
        self.horse_white = Horse(1, 0, 'white')
        self.horse_black = Horse(1, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.horse_white.get_position(), (1, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.horse_black.get_position(), (1, 7))

    def test_get_color_black(self):
        self.assertEqual(self.horse_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.horse_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.horse_white.get_icon(), 'HW')

    def test_get_icon_black(self):
        self.assertEqual(self.horse_black.get_icon(), 'HB')


class TestBishop(unittest.TestCase):

    def setUp(self):
        self.rook_white = Bishop(1, 0, 'white')
        self.rook_black = Bishop(7, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.rook_white.get_position(), (1, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.rook_black.get_position(), (7, 7))

    def test_get_color_black(self):
        self.assertEqual(self.rook_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.rook_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.rook_white.get_icon(), 'BW')

    def test_get_icon_black(self):
        self.assertEqual(self.rook_black.get_icon(), 'BB')


if __name__ == '__main__':
    unittest.main()
