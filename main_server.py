import socket
from threading import Thread
from game_model import GameModel
from game_view import GameView
from game_controller import GameController
from threading import Lock
import pickle

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and the port on which the server will run


host_name = socket.gethostname()

# Obtener la dirección IP asociada al nombre del host
direccion_ip = socket.gethostbyname(host_name)

print("Direccion IP servidor:", direccion_ip)
host = direccion_ip
port = 5555

# Bind the server to the specified host and port
server.bind((host, port))

# Enable the server to accept connections
server.listen(2)


id_count = 0
lock = Lock()
games = []
print("Waiting for connection...")

while True:
    connection, address = server.accept()
    print("Server is Connected to: ", address)

    id_count += 1
    player = 0
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        game_model = GameModel(game_id)
        games.append(game_model)  # Add the new game_model to the games list
        print("Creating a new Game...")
    else:
        if game_id < len(games):
            game_model = games[game_id]
            game_model.game.ready = True
            player = 1
        else:
            print("Game ID is out of range")
            continue  # Skip the rest of the loop iteration if game_id is out of range

    game_view = GameView(connection, player)
    game_controller = GameController(game_model, game_view, lock)

    Thread(target=game_controller.handle_connection).start()
