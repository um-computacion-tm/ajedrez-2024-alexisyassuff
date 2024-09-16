from Ajedrez.Board import Board
from Ajedrez.Bishop import Bishop

import unittest


class TestBishop(unittest.TestCase):

    def setUp(self):
        # Configura el tablero y el alfil para cada prueba
        self.board = Board()
        self.white_bishop = Bishop(2, 0, 'white')
        self.black_bishop = Bishop(5, 7, 'black')
        self.board.place_piece(self.white_bishop)
        self.board.place_piece(self.black_bishop)

    def test_initial_position_white(self):
        self.assertEqual(self.white_bishop.get_position(), (2, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.black_bishop.get_position(), (5, 7))

    def test_get_color_black(self):
        self.assertEqual(self.black_bishop.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.white_bishop.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.white_bishop.get_icon(), '♝')

    def test_get_icon_black(self):
        self.assertEqual(self.black_bishop.get_icon(), '♗')

    def test_path_not_clear(self):
        # Movimiento no válido si hay piezas en el camino
        obstructing_piece = Bishop(3, 1, 'white')
        self.board.place_piece(obstructing_piece)
        self.assertFalse(self.white_bishop.is_valid_move(4, 2, self.board))


if __name__ == '__main__':
    unittest.main()
