import chess
import unittest

class ChessTest(unittest.TestCase):
    def get_board(self):
        board = [['',  '',  '',  '',  'r', '',  '',  ''],
                 ['p', '',  '',  '',  '',  'p', 'k', 'p'],
                 ['q', '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  'B', 'b', 'b', '',  ''],
                 ['P', '',  '',  'P', '',  'p', 'p', 'P'],
                 ['',  '',  'N', '',  '',  '',  'n', ''],
                 ['',  'P', 'P', '',  '',  'K', 'P', 'R'],
                 ['R', '',  'B', 'Q', '',  '',  '',  '']]

        return board


    def test_can_rook_move(self):
        board = self.get_board()

        # can't jump pieces
        assert not chess.can_rook_move(board, 0, 4, 4, 4)
        assert not chess.can_rook_move(board, 7, 0, 7, 3)

        # can't move diagonally
        assert not chess.can_rook_move(board, 0, 4, 1, 3)

        # can move in vertical line
        assert chess.can_rook_move(board, 0, 4, 3, 4)

        # can move in horizontal line
        assert chess.can_rook_move(board, 0, 4, 0, 0)

        # can take piece
        assert chess.can_rook_move(board, 0, 4, 2, 4)
        assert chess.can_rook_move(board, 7, 0, 7, 2)


    def test_can_bishop_move(self):
        board = self.get_board()

        # can move diagonally up or down
        assert chess.can_bishop_move(board, 7, 2, 4, 5)
        assert chess.can_bishop_move(board, 7, 2, 6, 1)
        assert chess.can_bishop_move(board, 7, 2, 7, 2)
        assert chess.can_bishop_move(board, 3, 5, 0, 2)

        # can't move left
        assert not chess.can_bishop_move(board, 7, 2, 7, 1)
        # can't move down
        assert not chess.can_bishop_move(board, 3, 4, 4, 4)
        # can't move right
        assert not chess.can_bishop_move(board, 3, 5, 3, 6)
        # can't move up
        assert not chess.can_bishop_move(board, 3, 5, 2, 5)


    def test_can_knight_move(self):
        board = self.get_board()

        # can take pieces
        assert chess.can_knight_move(board, 5, 2, 3, 3)
        # can jump pieces
        assert chess.can_knight_move(board, 5, 2, 7, 3)
        # can move in 'L' shape
        assert chess.can_knight_move(board, 5, 2, 7, 1)
        assert chess.can_knight_move(board, 1, 6, 3, 5)
        assert chess.can_knight_move(board, 1, 6, 0, 4)
        assert chess.can_knight_move(board, 1, 6, 3, 7)

        # can't move horizontally
        assert not chess.can_knight_move(board, 1, 6, 0, 6)
        assert not chess.can_knight_move(board, 1, 6, 2, 6)
        assert not chess.can_knight_move(board, 1, 6, 3, 6)
        # can't move virtically
        assert not chess.can_knight_move(board, 1, 6, 1, 7)
        assert not chess.can_knight_move(board, 1, 6, 1, 4)
        assert not chess.can_knight_move(board, 1, 6, 1, 5)

        # can't move diagonally
        assert not chess.can_knight_move(board, 1, 6, 0, 5)
        assert not chess.can_knight_move(board, 1, 6, 0, 7)
        assert not chess.can_knight_move(board, 1, 6, 2, 7)
        assert not chess.can_knight_move(board, 1, 6, 2, 5)


    def test_can_king_move(self):
        board = self.get_board()

        # can move 1 square in any direction
        assert chess.can_king_move(board, 5, 6, 4, 6)
        assert chess.can_king_move(board, 5, 6, 4, 7)
        assert chess.can_king_move(board, 5, 6, 5, 7)
        assert chess.can_king_move(board, 5, 6, 6, 7)
        assert chess.can_king_move(board, 5, 6, 6, 6)
        assert chess.can_king_move(board, 5, 6, 6, 5)
        assert chess.can_king_move(board, 5, 6, 5, 5)
        assert chess.can_king_move(board, 5, 6, 4, 5)

        # cannot move more than 1 square in any direction
        assert not chess.can_king_move(board, 5, 6, 3, 6)
        assert not chess.can_king_move(board, 5, 6, 3, 7)
        assert not chess.can_king_move(board, 5, 6, 5, 8)
        assert not chess.can_king_move(board, 5, 6, 7, 8)
        assert not chess.can_king_move(board, 5, 6, 7, 6)
        assert not chess.can_king_move(board, 5, 6, 7, 4)
        assert not chess.can_king_move(board, 5, 6, 5, 4)
        assert not chess.can_king_move(board, 5, 6, 3, 4)


    def test_can_white_pawn_move(self):
        board = self.get_board()
        
        # white cannot move into a blank diagnoally
        assert not chess.can_pawn_move(board, 4, 3, 3, 2)
        # white cannot move backward
        assert not chess.can_pawn_move(board, 6, 1, 7, 1)
        # white cannot hop pieces
        assert not chess.can_pawn_move(board, 6, 2, 4, 2)
        # white cannot move two and take
        assert not chess.can_pawn_move(board, 6, 6, 4, 5)
        # white cannot move two if not on home row
        assert not chess.can_pawn_move(board, 4, 0, 2, 0)

        # white home is allowed to move 2
        assert chess.can_pawn_move(board, 6, 1, 4, 1)
        # white can move forward
        assert chess.can_pawn_move(board, 6, 1, 4, 1)
        assert chess.can_pawn_move(board, 4, 7, 3, 7)
        # white can take diagonally
        assert chess.can_pawn_move(board, 4, 3, 3, 4)


    def test_can_black_pawn_move(self):
        board = self.get_board()

        # black cannot move into a blank diagnoally
        assert not chess.can_pawn_move(board, 1, 5, 2, 6)
        # black cannot move backward
        assert not chess.can_pawn_move(board, 1, 5, 0, 5)
        # black cannot hop pieces
        assert not chess.can_pawn_move(board, 1, 0, 1, 3)
        # black cannot move two and take
        assert not chess.can_pawn_move(board, 1, 5, 3, 4)
        # black cannot move two if not on home row
        assert not chess.can_pawn_move(board, 4, 5, 6, 5)

        # black home is allowed to move 2
        assert chess.can_pawn_move(board, 1, 7, 3, 7)
        # black can move forward
        assert chess.can_pawn_move(board, 4, 5, 5, 5)
        assert chess.can_pawn_move(board, 1, 7, 2, 7)
        # black can take diagonally
        assert chess.can_pawn_move(board, 4, 5, 5, 6)


    def test_can_move(self):
        board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

        assert chess.try_move('white', board, 6, 3, 4, 3)
        assert chess.try_move('black', board, 0, 6, 2, 5)
        assert chess.try_move('white', board, 6, 2, 4, 2)
        assert chess.try_move('black', board, 1, 6, 2, 6)
        assert chess.try_move('white', board, 7, 1, 5, 2)
        assert chess.try_move('black', board, 1, 3, 3, 3)
        assert chess.try_move('white', board, 4, 2, 3, 3)
        assert chess.try_move('black', board, 2, 5, 3, 3)
        assert chess.try_move('white', board, 6, 4, 4, 4)
        assert chess.try_move('black', board, 3, 3, 5, 2)
        assert chess.try_move('white', board, 6, 1, 5, 2)
        assert chess.try_move('black', board, 0, 5, 1, 6)
        assert chess.try_move('white', board, 7, 6, 5, 5)
        assert chess.try_move('black', board, 1, 1, 2, 1)
        assert chess.try_move('white', board, 7, 5, 3, 1)
        assert chess.try_move('black', board, 1, 2, 2, 2)
        assert chess.try_move('white', board, 3, 1, 4, 2)


    def test_find_king(self):
        board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['',  '',  '',  '',  '',  '',  '',  ''],
                 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

        assert chess.find_king('white', board) == [7, 4]
        assert chess.find_king('black', board) == [0, 4]
        assert not chess.find_king('white', [[]])

if __name__ == '__main__':
    unittest.main()
