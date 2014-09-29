import os
import sys
import time
from renderer import Renderer


class ConsoleRenderer(Renderer):
    def draw(self, board):
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
