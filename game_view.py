import pickle
class GameView:
    def __init__(self, connection, player):
        self.connection = connection
        self.player = player

    def send_data(self, data):
        self.connection.sendall(pickle.dumps(data))

    def receive_data(self):
        return self.connection.recv(4096).decode()