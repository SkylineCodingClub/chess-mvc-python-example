#!/usr/bin/python
import copy
import random
import sys
import os
import time
import desktop

COLORS = ['white', 'black']
THRESHOLD = 500000


def play_game(renderer):
    board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             ['',  '',  '',  '',  '',  '',  '',  ''],
             ['',  '',  '',  '',  '',  '',  '',  ''],
             ['',  '',  '',  '',  '',  '',  '',  ''],
             ['',  '',  '',  '',  '',  '',  '',  ''],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

    moves = 0
    tries = 0
    turn_color = COLORS[moves % 2]
    while(1):
        next_move = get_next_move(color, board)
        if(tries > THRESHOLD):
            print "{0} loses".format(turn_color)
            break
        if(try_move(turn_color, board, next_move[0][0], next_move[0][1],
                    next_move[1][0], next_move[1][1])):
            moves += 1
            if(renderer == "console"):
                print_board(board)
            elif(renderer == "desktop"):
                desktop.draw_board(board)
            time.sleep(0.1)
            turn_color = COLORS[moves % 2]
            tries = 0
        else:
            tries += 1

        if(is_draw(board)):
            print "Draw"
            break


def is_draw(board):
    draw = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col].upper() != 'K' and board[row][col] != ''):
                draw = False

    return draw


def print_board(board):
    os.system('clear')
    print '---------'
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] == ''):
                sys.stdout.write(' ')
            else:
                sys.stdout.write(board[row][col])
        sys.stdout.flush()
        print '|'
    print '---------'


# "AI" function
def get_next_move(color, board):
    board_size = len(board) - 1
    return [
        [random.randint(0, board_size), random.randint(0, board_size)],
        [random.randint(0, board_size), random.randint(0, board_size)],
    ]


def try_move(turn_color, board, from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col]
    if(color(piece) != turn_color):
        return False

    if(can_move(board, from_row, from_col, to_row, to_col)):
        board[from_row][from_col] = ''
        if(to_row == 0 or to_row == len(board) - 1):
            if(should_promote(to_row, piece, board)):
                piece = promote(piece)
        board[to_row][to_col] = piece
        return True

    return False


def should_promote(row, piece, board):
    if(piece == 'p' and row == len(board) - 1):
        return True
    elif(piece == 'P' and row == 0):
        return True


def promote(piece):
    if(piece == 'p'):
        return 'q'
    if(piece == 'P'):
        return 'Q'


def on_board(from_row, from_col, to_row, to_col, board):
    board_size = len(board) - 1
    if(from_row < 0 or from_row > board_size or to_row < 0 or
            to_row > board_size):
        return False
    if(from_col < 0 or from_col > board_size or 
            to_col < 0 or to_col > board_size):
        return False

    return True


def can_move(board, from_row, from_col, to_row, to_col):
    if(from_row == from_col and to_row == to_col):
        return False

    if(not on_board(from_row, to_row, from_col, to_col, board)):
        return False

    if(board[from_row][from_col] == ''):
        return False

    if(color(board[from_row][from_col]) == color(board[to_row][to_col])):
        return False

    if(piece_can_move(board, from_row, from_col, to_row, to_col)):
        if(results_in_loss(board, from_row, from_col, to_row, to_col)):
            return False
    else:
        return False

    return True


def results_in_loss(board, from_row, from_col, to_row, to_col):
    temp_board = copy.deepcopy(board)
    piece = temp_board[from_row][from_col]
    temp_board[from_row][from_col] = ''
    temp_board[to_row][to_col] = piece

    if(in_check(color(piece), temp_board)):
        return True

    return False


def in_check(king_color, board):
    king_position = find_king(king_color, board)
    if(not king_position):
        return True
    king_row = king_position[0]
    king_col = king_position[1]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] != '' and color(board[row][col]) !=
               king_color):
                if(can_move(board, row, col, king_row, king_col)):
                    return True
    return False


def find_king(king_color, board):
    # first find the king
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col].upper() == 'K' and color(board[row][col]) ==
               king_color):
                return [row, col]

    return False


def color(piece):
    if(piece == ''):
        return ''

    if(piece.isupper()):
        return 'white'
    else:
        return 'black'


def piece_can_move(board, from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col].upper()
    if(piece == 'R'):
        can_move = can_rook_move(board, from_row, from_col, to_row, to_col)
    elif(piece == 'K'):
        can_move = can_king_move(board, from_row, from_col, to_row, to_col)
    elif(piece == 'N'):
        can_move = can_knight_move(board, from_row, from_col, to_row, to_col)
    elif(piece == 'B'):
        can_move = can_bishop_move(board, from_row, from_col, to_row, to_col)
    elif(piece == 'Q'):
        can_move = can_queen_move(board, from_row, from_col, to_row, to_col)
    elif(piece == 'P'):
        can_move = can_pawn_move(board, from_row, from_col, to_row, to_col)

    return can_move


def can_rook_move(board, from_row, from_col, to_row, to_col):
    if(from_row != to_row and from_col != to_col):
        return False

    if(from_row == to_row):
        for col in range(min(from_col, to_col) + 1, max(from_col, to_col)):
            if(board[to_row][col] != ''):
                return False
    elif(from_col == to_col):
        for row in range(min(from_row, to_row) + 1, max(from_row, to_row)):
            if(board[row][to_col] != ''):
                return False

    return True


def can_bishop_move(board, from_row, from_col, to_row, to_col):
    if(abs(from_row - to_row) != abs(from_col - to_col)):
        return False

    if(from_row < to_row):
        row_sign = 1
    else:
        row_sign = -1

    if(from_col < to_col):
        col_sign = 1
    else:
        col_sign = -1

    for step in range(1, abs(from_row - to_row)):
        if(board[from_row + step * row_sign][from_col + step * col_sign] !=
                ''):
            return False

    return True


def can_knight_move(board, from_row, from_col, to_row, to_col):
    if(not (abs(to_row - from_row) == 2 and abs(to_col - from_col) == 1) and
       not (abs(to_col - from_col) == 2 and abs(to_row - from_row) == 1)):
        return False

    return True


def can_queen_move(board, from_row, from_col, to_row, to_col):
    return (can_bishop_move(board, from_row, from_col, to_row, to_col) or
            can_rook_move(board, from_row, from_col, to_row, to_col))


def can_king_move(board, from_row, from_col, to_row, to_col):
    if(abs(from_row - to_row) > 1 or abs(from_col - to_col) > 1):
        return False

    return can_queen_move(board, from_row, from_col, to_row, to_col)


def can_pawn_move(board, from_row, from_col, to_row, to_col):
    distance = abs(from_row - to_row)
    if(distance > 2 or abs(from_col - to_col) > 1):
        return False

    if(distance == 2):
        if(from_col != to_col):
            return False
        if(from_row != 1 and from_row != 6):
            return False
        for row in range(min(from_row, to_row) + 1, max(from_row, to_row)):
            if(board[row][from_col] != ''):
                return False

    if(from_col != to_col):
        if(from_row == to_row):
            return False
        if(board[to_row][to_col] == ''):
            return False

    piece = board[from_row][from_col]
    if(piece.isupper()):
        if(to_row > from_row):
            return False
    else:
        if(to_row < from_row):
            return False

    return True


def init_game():
    if(len(sys.argv) > 1):
        renderer = sys.argv[1]
    else:
        renderer = "console"
    play_game(renderer)

init_game()
