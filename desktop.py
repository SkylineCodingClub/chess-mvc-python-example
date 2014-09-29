import pygame
from pygame.locals import *

square_size = 75

pygame_inited = False
fpsClock = []
windowSurfaceObj = []
surfaces = {}


def draw_board(board):
    if(not pygame_inited):
        init_pg(len(board))
    windowSurfaceObj.blit(surfaces['board'], (0, 0))
    for row in range(len(board)):
        for col in range(len(board[0])):
            piece = board[row][col]
            if(piece != ''):
                y = row*square_size
                x = col*square_size
                windowSurfaceObj.blit(surfaces[piece], (x, y))
    pygame.display.update()
    fpsClock.tick(30)


def init_pg(rows):
    pygame.init()
    global fpsClock
    fpsClock = pygame.time.Clock()
    global windowSurfaceObj
    windowSurfaceObj = pygame.display.set_mode(
        (square_size * rows, square_size * rows))
    pygame.display.set_caption('Chess Viewer')
    images = "images/"
    for piece in ['r', 'n', 'b', 'q', 'k', 'p',
                  'R', 'N', 'B', 'Q', 'K', 'P']:
        surfaces[piece] = pygame.image.load(images+piece+'.png')
        surfaces[piece].convert_alpha()

    surfaces['board'] = pygame.image.load(images+'board.png').convert_alpha()
