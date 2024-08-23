import unittest
from Ajedrez.Piece import Piece
from Ajedrez.Queen import Queen
from Ajedrez.King import King
from Ajedrez.Rook import Rook
from Ajedrez.Bishop import Bishop
from Ajedrez.Horse import Horse
from Ajedrez.Pawn import Pawn
from Ajedrez.Board import Board


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

    def test_is_valid_move_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.piece.is_valid_move(5, 5)


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


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn_white = Pawn(0, 1, 'white')
        self.pawn_black = Pawn(0, 6, 'black')
        self.board.place_piece(self.pawn_white)
        self.board.place_piece(self.pawn_black)

    def test_initial_position_white(self):
        self.assertEqual(self.pawn_white.get_position(), (0, 1))

    def test_initial_position_black(self):
        self.assertEqual(self.pawn_black.get_position(), (0, 6))

    def test_get_color_black(self):
        self.assertEqual(self.pawn_black.get_color(), 'black')

    def test_get_color_white(self):
        self.assertEqual(self.pawn_white.get_color(), 'white')

    def test_get_icon_white(self):
        self.assertEqual(self.pawn_white.get_icon(), 'PW')

    def test_get_icon_black(self):
        self.assertEqual(self.pawn_black.get_icon(), 'PB')

    def test_valid_move_white_pawn_initial(self):
        result = self.pawn_white.is_valid_move(0, 3, self.board)
        self.assertTrue(result)

    def test_valid_move_black_pawn_initial(self):
        result = self.pawn_black.is_valid_move(0, 4, self.board)
        self.assertTrue(result)

    def test_valid_move_white_pawn_capture(self):
        target_piece = Pawn(1, 2, 'black')
        self.board.place_piece(target_piece)
        result = self.pawn_white.is_valid_move(1, 2, self.board)
        self.assertTrue(result)

    def test_valid_move_black_pawn_capture(self):
        target_piece = Pawn(1, 5, 'white')
        self.board.place_piece(target_piece)
        result = self.pawn_black.is_valid_move(1, 5, self.board)
        self.assertTrue(result)

    def test_invalid_move_white_pawn_invalid_capture(self):
        result = self.pawn_white.is_valid_move(1, 2, self.board)
        self.assertFalse(result)

    def test_invalid_move_black_pawn_invalid_capture(self):
        result = self.pawn_black.is_valid_move(1, 5, self.board)
        self.assertFalse(result)

    def test_valid_move_white_pawn_single_step_after_initial(self):
        self.pawn_white.set_position(0, 3)
        result = self.pawn_white.is_valid_move(0, 4, self.board)
        self.assertTrue(result)

    def test_valid_move_black_pawn_single_step_after_initial(self):
        self.pawn_black.set_position(0, 5)
        result = self.pawn_black.is_valid_move(0, 4, self.board)
        self.assertTrue(result)


class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = Board()
        for row in board.board:
            for cell in row:
                self.assertIsNone(cell)

    def test_place_piece(self):
        board = Board()
        piece = Piece(0, 0, 'white', 'P')
        board.place_piece(piece)
        self.assertEqual(board.board[0][0], piece)

    def test_place_multiple_pieces(self):
        board = Board()
        piece1 = Piece(0, 0, 'white', 'P')
        piece2 = Piece(7, 7, 'black', 'P')
        board.place_piece(piece1)
        self.assertEqual(board.board[0][0], piece1)
        board.place_piece(piece2)
        self.assertEqual(board.board[7][7], piece2)


class TestBoardMovePiece(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(1, 1, 'white')
        self.queen = Queen(3, 0, 'black')
        self.board.place_piece(self.pawn)
        self.board.place_piece(self.queen)

    def test_valid_move_pawn(self):
        result = self.board.move_piece(self.pawn, 1, 2)
        self.assertTrue(result)
        self.assertIsNone(self.board.board[1][1])
        self.assertEqual(self.board.board[2][1], self.pawn)

    def test_invalid_move_pawn(self):
        result = self.board.move_piece(self.pawn, 1, 8)
        self.assertFalse(result)
        self.assertEqual(self.board.board[1][1], self.pawn)


class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(1, 1, 'white')
        self.board.place_piece(self.pawn)

    def test_get_piece_at(self):
        piece = self.board.get_piece_at(1, 1)
        self.assertEqual(piece, self.pawn)

    def test_get_piece_at_empty_square(self):
        piece = self.board.get_piece_at(0, 0)
        self.assertIsNone(piece)

    def test_get_position_from_notation(self):
        col, row = self.board.get_position_from_notation('a1')
        self.assertEqual((col, row), (0, 7))

        col, row = self.board.get_position_from_notation('h8')
        self.assertEqual((col, row), (7, 0))

        col, row = self.board.get_position_from_notation('d4')
        self.assertEqual((col, row), (3, 4))

    def test_print_board(self):
        self.board.print_board()


if __name__ == '__main__':
    unittest.main()
