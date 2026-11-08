class Player:
    def __init__(self, name="", symbole="", position=None):
        self.name = name
        self.symbole = symbole
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return f"Player {self.name} ({self.symbole}) is at position {self.position}"

class Board:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def display_board(self):
        print('*' * 17)
        for index, row in enumerate(self.board):
            print('*   ' + ' | '.join(row) + '   *')
            if index < 2:
                print('*  ---|---|---  *')
        print('*' * 17)

    def update_board(self, position, symbole):
        row, col = position
        self.board[row][col] = symbole

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.game_status = None
        self.last_played = None

    def player_input(self, player):
        while True:
            try:
                position = input(
                    f"{player.name} ({player.symbole}), enter your move (row,col): "
                )
                row, col = map(int, position.split(','))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    raise ValueError("Row and column must be between 0 and 2.")
                if self.board.board[row][col] != ' ':
                    raise ValueError("This position is already taken.")
                self.board.update_board((row, col), player.symbole)
                player.move((row, col))
                return row, col
            except ValueError as error:
                print(f"Invalid input: {error}. Please try again.")

    def check_win(self, player):
        board = self.board.board
        lines = board + [
            [board[row][col] for row in range(3)]
            for col in range(3)
        ] + [
            [board[index][index] for index in range(3)],
            [board[index][2 - index] for index in range(3)],
        ]
        if any(all(cell == player.symbole for cell in line) for line in lines):
            self.game_status = 'win'
            return True
        return False

    def check_tie(self):
        if (
            self.game_status != 'win'
            and all(cell != ' ' for row in self.board.board for cell in row)
        ):
            self.game_status = 'tie'
            return True
        return False

    def switch_player(self):
        if self.last_played == self.player1:
            return self.player2
        return self.player1

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




