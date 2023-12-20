import numpy as np

class Board:
    def __init__(self):
        self._board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def __str__(self):
        return str(np.array(self, dtype=object))

    def __repr__(self):
        return str(np.array(self, dtype=object))
    
    def __getitem__(self, key):
        if self._board[key[0]][key[1]] == 1:
            return 'X'
        elif self._board[key[0]][key[1]] == -1:
            return 'O'
        else:
            return None
        
    def __setitem__(self, key, value):
        if value == 'X':
            self._board[key[0]][key[1]] = 1
        elif value == 'O':
            self._board[key[0]][key[1]] = -1

    def __array__(self, dtype=object):
        if not np.issubdtype(dtype, np.number):
            board = self._board.astype(object)
            board[board == 1] = 'X'
            board[board == -1] = 'O'
            board[board == 0] = None
            return board
        return self._board.astype(dtype)
    
    def winner(self):

        """Returns the winner of the given Tic-Tac-Toe board, or None if there is no winner."""

        # Check for horizontal wins.
        for row in range(3):
            if self._board[row][0] == self._board[row][1] == self._board[row][2] and self._board[row][0] != 0:
                return _to_name(self._board[row][0])

        # Check for vertical wins.
        for col in range(3):
            if self._board[0][col] == self._board[1][col] == self._board[2][col] and self._board[0][col] != 0:
                return _to_name(self._board[0][col])

        # Check for diagonal wins.
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[0][0] != 0:
            return _to_name(self._board[0][0])
        elif self._board[0][2] == self._board[1][1] == self._board[2][0] and self._board[0][2] != 0:
            return _to_name(self._board[0][2])
        
        # Check for cat's game.
        if not 0 in self._board:
            return 'C'

        # If there are no winners, return None.
        return None

def _to_name(int_rep):
    if int_rep == 1:
        return 'X'
    elif int_rep == -1:
        return 'O'
    else:
        return None