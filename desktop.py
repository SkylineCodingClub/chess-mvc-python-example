from renderer import Renderer
HAS_PYGAME = True
try:
    import pygame
    from pygame.locals import *
except ImportError:
    HAS_PYGAME = False

SQUARE_SIZE = 75

class DesktopRenderer(Renderer):
    def __init__(self, rows):
        if(not HAS_PYGAME):
            print "Cannot use desktop renderer without pygame"
            raise ImportError("Missing dependency pygame")
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.windowSurfaceObj = pygame.display.set_mode(
            (SQUARE_SIZE * rows, SQUARE_SIZE * rows))
        pygame.display.set_caption('Chess Viewer')
        images = "images/"
        self.surfaces = {}
        for piece in ['r', 'n', 'b', 'q', 'k', 'p',
                      'R', 'N', 'B', 'Q', 'K', 'P']:
            self.surfaces[piece] = pygame.image.load(images+piece+'.png')
            self.surfaces[piece].convert_alpha()

        self.surfaces['board'] = pygame.image.load(images+'board.png')
        self.surfaces['board'].convert_alpha()

    def draw(self, board):
        self.windowSurfaceObj.blit(self.surfaces['board'], (0, 0))
        for row in range(len(board)):
            for col in range(len(board[0])):
                piece = board[row][col]
                if(piece != ''):
                    y = row*SQUARE_SIZE
                    x = col*SQUARE_SIZE
                    self.windowSurfaceObj.blit(self.surfaces[piece], (x, y))
        pygame.display.update()
        self.fpsClock.tick(30)
