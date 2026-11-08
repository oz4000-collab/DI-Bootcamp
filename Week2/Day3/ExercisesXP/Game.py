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
