from game import Game
from player import Player
from board import Board


class Main:
    def __init__(self):
        self.game = Game(Player(), Player(), Board())

    def start(self):
        self.play()

    def play(self):
        player1 = self.game.player1
        player2 = self.game.player2
        player1.name = input("Enter name for Player 1: ")
        player2.name = input("Enter name for Player 2: ")

        while True:
            player1.symbole = input(f"{player1.name}, choose X or O: ").strip().upper()
            if player1.symbole in ('X', 'O'):
                break
            print("Please choose X or O.")

        player2.symbole = 'O' if player1.symbole == 'X' else 'X'
        print(f"{player2.name}'s symbol is {player2.symbole}.")
        print(
            f"Starting game between {player1.name} ({player1.symbole}) "
            f"and {player2.name} ({player2.symbole})"
        )

        while self.game.game_status is None:
            self.game.board.display_board()
            current_player = self.game.switch_player()
            self.game.player_input(current_player)
            self.game.last_played = current_player

            if self.game.check_win(current_player):
                print(f"{current_player.name} wins!")
            else:
                self.game.check_tie()

        self.game.board.display_board()
        print(f"Game over: {self.game.game_status}.The winner is {self.game.last_played.name}!")


if __name__ == "__main__":
    Main().start()
