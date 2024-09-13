import unittest
from Ajedrez.Knight import Knight
from Ajedrez.Board import Board


class TestKnight(unittest.TestCase):
    def setUp(self):
        self.knight_white = Knight(1, 0, 'white')
        self.knight_black = Knight(1, 7, 'black')

    def test_initial_position_white(self):
        self.assertEqual(self.knight_white.get_position(), (1, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.knight_black.get_position(), (1, 7))

    def test_get_color_black(self):
        self.assertEqual(self.knight_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.knight_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.knight_white.get_icon(), '♞')

    def test_get_icon_black(self):
        self.assertEqual(self.knight_black.get_icon(), '♘')

    def test_empty_position_move(self):
        board = Board()
        knight = Knight(3, 3, 'white')
        board.place_piece(knight)
        assert knight.is_valid_move(4, 5, board)


if __name__ == '__main__':
    unittest.main()
