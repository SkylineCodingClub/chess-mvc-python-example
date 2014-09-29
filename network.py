import socket
import json


class SocketMover:
    def __init__(self):
        HOST = socket.gethostname()
        PORT = 5000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)

    def get_next_move(self, color, board):
        while True:
            try:
                client, address = self.socket.accept()
                client.settimeout(10)
                move = client.recv(1024)
                client.close()
                if(not move):
                    continue
                else:
                    try:
                        move = json.loads(move)
                    except ValueError:
                        continue
                    break
            except socket.timeout:
                continue

        return move
