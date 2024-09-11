
# from Ajedrez.Pawn import Pawn
# from Ajedrez.Board import Board

# import unittest


# class TestPawn(unittest.TestCase):
#     def setUp(self):
#         self.board = Board()
#         self.pawn_white = Pawn(0, 1, 'white')
#         self.pawn_black = Pawn(0, 6, 'black')
#         self.board.place_piece(self.pawn_white)
#         self.board.place_piece(self.pawn_black)

#     def test_initial_position_white(self):
#         self.assertEqual(self.pawn_white.get_position(), (0, 1))

#     def test_initial_position_black(self):
#         self.assertEqual(self.pawn_black.get_position(), (0, 6))

#     def test_get_color_black(self):
#         self.assertEqual(self.pawn_black.get_color(), 'black')

#     def test_get_color_white(self):
#         self.assertEqual(self.pawn_white.get_color(), 'white')

#     def test_get_icon_white(self):
#         self.assertEqual(self.pawn_white.get_icon(), '♟')

#     def test_get_icon_black(self):
#         self.assertEqual(self.pawn_black.get_icon(), '♙')

#     def test_valid_move_white_pawn_initial(self):
#         result = self.pawn_white.is_valid_move(0, 3, self.board)
#         self.assertTrue(result)

#     def test_valid_move_black_pawn_initial(self):
#         result = self.pawn_black.is_valid_move(0, 4, self.board)
#         self.assertTrue(result)

#     def test_valid_move_white_pawn_capture(self):
#         target_piece = Pawn(1, 2, 'black')
#         self.board.place_piece(target_piece)
#         result = self.pawn_white.is_valid_move(1, 2, self.board)
#         self.assertTrue(result)

#     def test_valid_move_black_pawn_capture(self):
#         target_piece = Pawn(1, 5, 'white')
#         self.board.place_piece(target_piece)
#         result = self.pawn_black.is_valid_move(1, 5, self.board)
#         self.assertTrue(result)

#     def test_invalid_move_white_pawn_invalid_capture(self):
#         result = self.pawn_white.is_valid_move(1, 2, self.board)
#         self.assertFalse(result)

#     def test_invalid_move_black_pawn_invalid_capture(self):
#         result = self.pawn_black.is_valid_move(1, 5, self.board)
#         self.assertFalse(result)

#     def test_valid_move_white_pawn_single_step_after_initial(self):
#         self.pawn_white.set_position(0, 3)
#         result = self.pawn_white.is_valid_move(0, 4, self.board)
#         self.assertTrue(result)

#     def test_valid_move_black_pawn_single_step_after_initial(self):
#         self.pawn_black.set_position(0, 5)
#         result = self.pawn_black.is_valid_move(0, 4, self.board)
#         self.assertTrue(result)


# if __name__ == '__main__':
#     unittest.main()
import unittest
from Ajedrez.Board import Board
from Ajedrez.Pawn import Pawn


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_white_pawn_initial_move(self):
        pawn = Pawn(0, 1, 'white')
        self.board.place_piece(pawn)
        self.assertTrue(pawn.is_valid_move(0, 2, self.board))
        self.assertTrue(pawn.is_valid_move(0, 3, self.board))
        self.assertFalse(pawn.is_valid_move(0, 4, self.board))

    def test_white_pawn_forward_move(self):
        pawn = Pawn(0, 2, 'white')
        self.board.place_piece(pawn)
        self.assertTrue(pawn.is_valid_move(0, 3, self.board))
        self.assertFalse(pawn.is_valid_move(0, 4, self.board))

    def test_white_pawn_diagonal_capture(self):
        pawn = Pawn(1, 2, 'white')
        enemy_pawn = Pawn(0, 3, 'black')
        self.board.place_piece(pawn)
        self.board.place_piece(enemy_pawn)
        self.assertTrue(pawn.is_valid_move(0, 3, self.board))
        self.assertFalse(pawn.is_valid_move(1, 3, self.board))
        self.assertFalse(pawn.is_valid_move(2, 3, self.board))

    def test_white_pawn_invalid_vertical_capture(self):
        pawn = Pawn(1, 2, 'white')
        enemy_pawn = Pawn(1, 3, 'black')
        self.board.place_piece(pawn)
        self.board.place_piece(enemy_pawn)
        self.assertFalse(pawn.is_valid_move(1, 3, self.board))

    def test_black_pawn_initial_move(self):
        pawn = Pawn(0, 6, 'black')
        self.board.place_piece(pawn)
        self.assertTrue(pawn.is_valid_move(0, 5, self.board))
        self.assertTrue(pawn.is_valid_move(0, 4, self.board))
        self.assertFalse(pawn.is_valid_move(0, 3, self.board))

    def test_black_pawn_forward_move(self):
        pawn = Pawn(0, 5, 'black')
        self.board.place_piece(pawn)
        self.assertTrue(pawn.is_valid_move(0, 4, self.board))
        self.assertFalse(pawn.is_valid_move(0, 3, self.board))

    def test_black_pawn_diagonal_capture(self):
        pawn = Pawn(1, 5, 'black')
        enemy_pawn = Pawn(0, 4, 'white')
        self.board.place_piece(pawn)
        self.board.place_piece(enemy_pawn)
        self.assertTrue(pawn.is_valid_move(0, 4, self.board))
        self.assertFalse(pawn.is_valid_move(1, 4, self.board))
        self.assertFalse(pawn.is_valid_move(2, 4, self.board))

    def test_black_pawn_invalid_vertical_capture(self):
        pawn = Pawn(1, 5, 'black')
        enemy_pawn = Pawn(1, 4, 'white')
        self.board.place_piece(pawn)
        self.board.place_piece(enemy_pawn)
        self.assertFalse(pawn.is_valid_move(1, 4, self.board))


if __name__ == '__main__':
    unittest.main()
