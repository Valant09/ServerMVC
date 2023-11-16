import socket
from threading import Thread
from game_model import GameModel
from game_view import GameView
from game_controller import GameController

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and the port on which the server will run
host = 'localhost'
port = 5555

# Bind the server to the specified host and port
server.bind((host, port))

# Enable the server to accept connections
server.listen(2)

id_count = 0  # Initialize id_count
print("Waiting for connection...")

while True:
    connection, address = server.accept()
    print("Server is Connected to: ", address)

    id_count += 1
    player = 0
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        game_model = GameModel(game_id)
        print("Creating a new Game...")
    else:
        game_model = games[game_id]
        game_model.game.ready = True
        player = 1

    game_view = GameView(connection, player)
    game_controller = GameController(game_model, game_view, lock)

    Thread(target=game_controller.handle_connection).start()
