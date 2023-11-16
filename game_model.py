class GameModel:
    def __init__(self, game_id):
        self.game_id = game_id
        self.game = Game(game_id)

    def reset_game(self):
        self.game.resetGame()

    def play_move(self, player, move):
        self.game.play(player, move)
        return self.game

    def find_winner(self):
        return self.game.findWinner()