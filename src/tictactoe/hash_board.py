import numpy as np

def hash_board(board):
    return hash(tuple(board.flatten()))