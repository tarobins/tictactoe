from tictactoe.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'
        self.penalized_player = None

    def play(self, row, col):
        player = self.turn
        if self.board[row, col] is not None:
            if self.penalized_player is None:
                self.penalized_player = player
            self.turn = 'X' if self.turn == 'O' else 'O'
            return self.value(player), 'E'
        if self.penalized_player is not None:
            return self.value(player), 'E'
        self.board[row, col] = player
        self.turn = 'X' if player == 'O' else 'O'
        return self.value(player), self.board.winner()

    def value(self, player):
        if self.penalized_player == player:
            return -100
        elif self.board.winner() == player:
            return 10
        elif self.board.winner() == 'C':
            return 5
        elif self.board.winner() is None:
            return 0
        else:
            return -10