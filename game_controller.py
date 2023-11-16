class GameController:
    def __init__(self, model, view, lock):
        self.model = model
        self.view = view
        self.lock = lock

    def handle_connection(self):
        with self.lock:
            self.view.send_data(str(self.view.player))

            while True:
                try:
                    data = self.view.receive_data()

                    if not data:
                        if self.lock.locked():
                            self.lock.release()
                        break
                    elif data == "reset":
                        self.model.reset_game()
                    elif data != "get":
                        self.model.play_move(self.view.player, data)

                    winner = self.model.find_winner()
                    if winner != -1:
                        self.view.send_data(f"Player {winner} wins!")
                        break

                    self.view.send_data(self.model.game)

                    if self.lock.locked():
                        self.lock.release()

                except Exception as e:
                    print(f"Exception: {e}")
                    if self.lock.locked():
                        self.lock.release()
                    break

            print("Lost Connection")