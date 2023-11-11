import numpy as np

class Board:
    def __init__(self):
        self._board = np.array([[None, None, None], [None, None, None], [None, None, None]])

    def __str__(self):
        return str(self._board)

    def __repr__(self):
        return str(self._board)
    
    def __getitem__(self, key):
        return self._board[key[0]][key[1]]
    
    def __setitem__(self, key, value):
        self._board[key[0]][key[1]] = value

    def __array__(self, dtype=object):
        return self._board.copy().astype(dtype)
    
    def winner(self):

        """Returns the winner of the given Tic-Tac-Toe board, or None if there is no winner."""

        # Check for horizontal wins.
        for row in range(3):
            if self._board[row][0] == self._board[row][1] == self._board[row][2] and self._board[row][0] is not None:
                return self._board[row][0]

        # Check for vertical wins.
        for col in range(3):
            if self._board[0][col] == self._board[1][col] == self._board[2][col] and self._board[0][col] is not None:
                return self._board[0][col]

        # Check for diagonal wins.
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[0][0] is not None:
            return self._board[0][0]
        elif self._board[0][2] == self._board[1][1] == self._board[2][0] and self._board[0][2] is not None:
            return self._board[0][2]
        
        # Check for cat's game.
        if not None in self._board:
            return 'C'

        # If there are no winners, return None.
        return None
