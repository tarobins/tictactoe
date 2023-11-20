from tictactoe.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'
        self.penalized_player = None

    def play_rc(self, row, col):
        player = self.turn
        self.turn = 'X' if self.turn == 'O' else 'O'
        if self.board[row, col] is not None:
            if self.penalized_player is None:
                self.penalized_player = player
                return self.value(player), 'E'
            else:
                return 0, 'E'
        if self.penalized_player is not None:
            return self.value(player), 'E'
        self.board[row, col] = player
        return self.value(player), self.board.winner()
    
    def play_index(self, index):
        return self.play_rc(index // 3, index % 3)
    
    def get_board_as_vector(self, dtype=int):
        return self.board.__array__(dtype=dtype).flatten()

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