from tictactoe.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    def play(self, row, col):
        self.board[row, col] = self.turn
        self.turn = 'X' if self.turn == 'O' else 'O'
        return self.board.winner()
