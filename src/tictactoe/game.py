from tictactoe.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.next_turn = 'X'
        self.penalized_player = None
        self._x_plays = 0
        self._o_plays = 0

    def play_rc(self, row, col):
        turn = self.next_turn
        self.next_turn = 'X' if self.next_turn == 'O' else 'O'
        if self.penalized_player is not None:
            return 0, 'E'
        if turn == 'X':
            self._x_plays += 1
        else:
            self._o_plays += 1
        if self.board[row, col] is not None:
            if self.penalized_player is None:
                self.penalized_player = turn
                if turn == 'X':
                    self._x_plays -= 1
                else:
                    self._o_plays -= 1
                return self.value(turn), 'E'
            else:
                return 0, 'E'
        self.board[row, col] = turn
        if self.board.winner() is None:
            return 1, None
        else:
            if self.board.winner() == turn:
                return 11, self.board.winner()
            else:
                return 1, self.board.winner()
    
    def play_index(self, index):
        return self.play_rc(index // 3, index % 3)
    
    def get_board_as_vector(self, dtype=int):
        return self.board.__array__(dtype=dtype).flatten()

    def winner(self):
        if self.penalized_player is not None:
            return 'X' if self.penalized_player == 'O' else 'X'
        return self.board.winner()

    def value(self, player):
        if player == 'X':
            plays = self._x_plays
        else:
            plays = self._o_plays
        if self.penalized_player == player:
            return -100 + plays
        elif self.board.winner() == player:
            return 10 + plays
        elif self.board.winner() == 'C':
            return plays
        elif self.board.winner() is None:
            return plays
        else:
            return -10 + plays