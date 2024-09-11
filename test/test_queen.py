
from Ajedrez.Board import Board
from Ajedrez.Rook import Rook
from Ajedrez.Queen import Queen
import unittest


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen(3, 0, 'white')
        self.queen_black = Queen(3, 7, 'black')
        self.board.place_piece(self.queen_white)
        self.board.place_piece(self.queen_black)

    def test_initial_position_white(self):
        self.assertEqual(self.queen_white.get_position(), (3, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.queen_black.get_position(), (3, 7))

    def test_get_color_black(self):
        self.assertEqual(self.queen_black.get_color(), 'black')

    def test_get_icon_white(self):
        self.assertEqual(self.queen_white.get_icon(), '♛')

    def test_valid_move_diagonal(self):
        # Movimiento válido en diagonal
        self.assertTrue(self.queen_white.is_valid_move(7, 4, self.board))
        self.assertTrue(self.queen_white.is_valid_move(0, 3, self.board))

    def test_invalid_move_non_linear(self):
        # Movimiento inválido que no es en línea recta ni en diagonal
        self.assertFalse(self.queen_white.is_valid_move(4, 5, self.board))

    def test_initial_position_black(self):
        self.assertEqual(self.queen_black.get_position(), (3, 7))

    def test_valid_move_vertical(self):
        # Movimiento vertical válido
        self.assertTrue(self.queen_white.is_valid_move(3, 5, self.board))

    def test_invalid_move_knight(self):
        # Movimiento en forma de L no es válido para una reina
        self.assertFalse(self.queen_white.is_valid_move(4, 2, self.board))

    def test_invalid_move_obstructed_vertical(self):
        # Coloca una pieza en el camino vertical de la reina
        obstructing_rook = Rook(3, 2, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(3, 5, self.board))

    def test_invalid_move_obstructed_horizontal(self):
        # Coloca una pieza en el camino horizontal de la reina
        obstructing_rook = Rook(5, 0, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(7, 0, self.board))

    def test_invalid_move_obstructed_diagonal(self):
        # Coloca una pieza en el camino diagonal de la reina
        obstructing_rook = Rook(4, 1, 'white')
        self.board.place_piece(obstructing_rook)
        self.assertFalse(self.queen_white.is_valid_move(5, 2, self.board))

    def test_valid_capture_enemy_piece(self):
        # Movimiento válido para capturar una pieza enemiga
        enemy_rook = Rook(5, 0, 'black')
        self.board.place_piece(enemy_rook)
        self.assertTrue(self.queen_white.is_valid_move(5, 0, self.board))


if __name__ == '__main__':
    unittest.main()
