import numpy as np
from tictactoe.board import Board

def test_set_cell():
    b = Board()
    b[0,0] = 'X'
    assert b[0,0] == 'X'

def test_no_winner():
    b = Board()
    assert b.winner() is None

def test_row_winner():
    b = Board()
    b[0,0] = 'X'
    b[0,1] = 'X'
    b[0,2] = 'X'
    assert b.winner() == 'X'

def test_col_winner():
    b = Board()
    b[0,0] = 'X'
    b[1,0] = 'X'
    b[2,0] = 'X'
    assert b.winner() == 'X'

def test_diag_winner():
    b = Board()
    b[0,0] = 'X'
    b[1,1] = 'X'
    b[2,2] = 'X'
    assert b.winner() == 'X'

def test_other_diag_winner():
    b = Board()
    b[0,2] = 'X'
    b[1,1] = 'X'
    b[2,0] = 'X'
    assert b.winner() == 'X'

def test_no_winner():
    b = Board()
    b[0,0] = 'X'
    b[0,1] = 'O'
    b[0,2] = 'X'
    assert b.winner() is None

def test_catsgame():
    b = Board()
    b[0,0] = 'X'
    b[0,1] = 'O'
    b[0,2] = 'X'
    b[1,0] = 'O'
    b[1,1] = 'X'
    b[1,2] = 'O'
    b[2,0] = 'O'
    b[2,1] = 'X'
    b[2,2] = 'O'
    assert b.winner() == 'C'

def test_array():
    b = Board()
    b[1,1] = 'X'
    array = np.array(b)
    assert array[1,1] == 'X'
    assert array[0,0] is None

def test_array_int():
    b = Board()
    b[1,1] = 'X'
    b[0,0] = 'O'
    array = np.array(b, dtype=np.int16)
    assert array[1,1] == 1
    assert array[0,0] == -1
    assert array[0,1] == 0

def test__str__():
    b = Board()
    b[1,1] = 'X'
    b[0,0] = 'O'
    assert str(b) == "[['O' None None]\n [None 'X' None]\n [None None None]]"

def test__repr__():
    b = Board()
    b[1,1] = 'X'
    b[0,0] = 'O'
    assert repr(b) == "[['O' None None]\n [None 'X' None]\n [None None None]]"