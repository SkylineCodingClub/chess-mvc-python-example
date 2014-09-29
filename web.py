from renderer import Renderer


class WebRenderer(Renderer):
    def draw(self, board):
        file = open('web/chess.html', 'w')
        file.write('<html><head>')
        file.write('<link rel="stylesheet" type="text/css" href="chess.css">')
        file.write('</head>')
        file.write('<body>\n')
        color = ['light', 'dark']
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == ''):
                    file.write('<div class="square {}"></div>'.format(
                        color[col % 2]))
                else:
                    piece = board[row][col]
                    if(piece.isupper()):
                        team = 'white'
                    else:
                        team = 'black'
                    file.write('<div class="square {} {} {}"></div>'.format(
                        piece, color[col % 2], team))
            color.reverse()
            file.write("<br/>\n")
        file.write('</body></html>')
