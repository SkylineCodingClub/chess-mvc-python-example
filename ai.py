import random


class RandomMover:
    def get_next_move(self, color, board):
        board_size = len(board) - 1
        return [
            [random.randint(0, board_size), random.randint(0, board_size)],
            [random.randint(0, board_size), random.randint(0, board_size)],
        ]
