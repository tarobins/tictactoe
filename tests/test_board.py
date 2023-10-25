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