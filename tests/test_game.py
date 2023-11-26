import numpy as np

from tictactoe.game import Game

def test_game_start():
    g = Game()
    assert g.turn == 'X'
    assert g.board.winner() is None
    assert g.value('X') == 0
    assert g.value('O') == 0

def test_game_play():
    g = Game()
    assert g.turn == 'X'
    assert g.play_rc(0,0)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(1,0)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(0,1)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(1,1)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(0,2) == (10, 'X')
    assert g.value('X') == 10
    assert g.value('O') == -10

def test_catsgame():
    g = Game()
    assert g.turn == 'X'
    assert g.play_rc(0,0)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(0,1)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(0,2)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(1,0)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(1,1)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(2,0)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(1,2)[1] is None
    assert g.turn == 'O'
    assert g.play_rc(2,2)[1] is None
    assert g.turn == 'X'
    assert g.play_rc(2,1) == (5, 'C')
    assert g.winner() == 'C'
    assert g.value('X') == 5
    assert g.value('O') == 5

def test_badplay_o():
    g = Game()
    assert g.turn == 'X'
    assert g.play_rc(0,0) == (0, None)
    assert g.turn == 'O'
    assert g.play_rc(0,0) == (-100, 'E')
    assert g.turn == 'X'
    assert g.play_rc(0,1) == (0, 'E')
    assert g.value('O') == -100
    assert g.value('X') == 0

def test_badplay_o_not_x():
    g = Game()
    assert g.turn == 'X'
    assert g.play_rc(0,0) == (0, None)
    assert g.turn == 'O'
    assert g.play_rc(0,0) == (-100, 'E')
    assert g.turn == 'X'
    assert g.play_rc(0,0) == (0, 'E')
    assert g.turn == 'O'
    assert g.play_rc(0,0) == (0, 'E')
    assert g.value('O') == -100
    assert g.value('X') == 0

def test_play_index():
    g = Game()
    assert g.turn == 'X'
    assert g.play_index(0)[1] is None
    assert g.turn == 'O'
    assert g.play_index(1)[1] is None
    assert g.turn == 'X'
    assert g.play_index(3)[1] is None
    assert g.turn == 'O'
    assert g.play_index(4)[1] is None
    assert g.winner() is None
    assert g.turn == 'X'
    assert g.play_index(6) == (10, 'X')
    assert g.winner() == 'X'
    assert g.value('X') == 10
    assert g.value('O') == -10

def test_get_board_as_vector():
    g = Game()
    g.play_index(0)
    g.play_index(1)
    g.play_index(3)
    np.testing.assert_array_equal(g.get_board_as_vector(), [1, -1, 0, 1, 0, 0, 0, 0, 0])