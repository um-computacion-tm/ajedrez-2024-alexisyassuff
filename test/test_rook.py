import unittest
from Ajedrez.Board import Board
from Ajedrez.Rook import Rook


class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.white_rook = Rook(7, 7, 'white')
        self.black_rook = Rook(0, 0, 'black')
        self.board.place_piece(self.white_rook)
        self.board.place_piece(self.black_rook)

    def test_initial_position_white(self):
        self.assertEqual(self.white_rook.get_position(), (7, 7))

    def test_initial_position_black(self):
        self.assertEqual(self.black_rook.get_position(), (0, 0))

    def test_get_color_black(self):
        self.assertEqual(self.black_rook.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.white_rook.get_color(), 'white')

    def test_get_icon_black(self):
        self.assertEqual(self.black_rook.get_icon(), '♖')

    def test_invalid_move_diagonal(self):
        # Movimiento diagonal no es válido para una torre
        self.assertFalse(self.white_rook.is_valid_move(1, 1, self.board))

    def test_invalid_move_obstructed(self):
        # Movimiento inválido cuando hay una pieza en el camino
        obstructing_rook = Rook(0, 3, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.white_rook.is_valid_move(0, 5, self.board))

    def test_invalid_capture_own_piece(self):
        # Movimiento inválido al intentar capturar una pieza propia
        self.board.place_piece(Rook(0, 5, 'white'))
        self.assertFalse(self.white_rook.is_valid_move(0, 5, self.board))

    if __name__ == '__main__':
        unittest.main()
