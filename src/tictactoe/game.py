from tictactoe.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    def play(self, row, col):
        self.board[row, col] = self.turn
        self.turn = 'X' if self.turn == 'O' else 'O'
        return self.board.winner()

    def value(self, player):
        if self.board.winner() == player:
            return 10
        elif self.board.winner() == 'C':
            return 5
        elif self.board.winner() is None:
            return 0
        else:
            return -10