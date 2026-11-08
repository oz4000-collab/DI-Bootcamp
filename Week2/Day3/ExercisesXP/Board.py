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
