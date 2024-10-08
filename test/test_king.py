from Ajedrez.King import King
from Ajedrez.Board import Board
import unittest
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Board import Board


class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.king_white = King(4, 0, 'white')
        self.king_black = King(4, 7, 'black')
        self.board.place_piece(self.king_white)
        self.board.place_piece(self.king_black)

    def test_initial_position_white(self):
        self.assertEqual(self.king_white.get_position(), (4, 0))

    def test_initial_position_black(self):
        self.assertEqual(self.king_black.get_position(), (4, 7))

    def test_get_color_black(self):
        self.assertEqual(self.king_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.king_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.king_white.get_icon(), '♚')

    def test_get_icon_black(self):
        self.assertEqual(self.king_black.get_icon(), '♔')

    def test_valid_move_adjacent(self):
        self.assertTrue(self.king_white.is_valid_move(4, 1, self.board))
        self.assertTrue(self.king_white.is_valid_move(3, 0, self.board))
        self.assertTrue(self.king_white.is_valid_move(3, 1, self.board))

    def test_invalid_move_non_adjacent(self):
        self.assertFalse(self.king_white.is_valid_move(4, 2, self.board))
        self.assertFalse(self.king_white.is_valid_move(2, 0, self.board))

    def test_valid_capture_enemy_piece(self):
        enemy_rook = Rook(3, 0, 'black')
        self.board.place_piece(enemy_rook)
        self.assertTrue(self.king_white.is_valid_move(3, 0, self.board))

    def test_invalid_capture_own_piece(self):
        own_rook = Rook(3, 0, 'white')
        self.board.place_piece(own_rook)
        self.assertFalse(self.king_white.is_valid_move(3, 0, self.board))

    def test_valid_move_adjacent(self):
        self.board = Board()
        self.king_white = King(4, 4, 'white')
        self.board.place_piece(self.king_white)
        # Movimiento válido del rey a una casilla adyacente
        # Ajustar posición si es necesario
        self.assertTrue(self.king_white.is_valid_move(3, 4, self.board))
