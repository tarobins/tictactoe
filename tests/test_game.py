import numpy as np

from tictactoe.game import Game

def test_game_start():
    g = Game()
    assert g.next_turn == 'X'
    assert g.board.winner() is None
    assert g.value('X') == 0
    assert g.value('O') == 0

def test_game_play():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_rc(0,0) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(1,0) == (1, None)
    assert g.next_turn == 'X'
    assert g.play_rc(0,1) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(1,1) == (1, None)
    assert g.next_turn == 'X'
    assert g.play_rc(0,2) == (11, 'X')
    assert g.value('X') == 13
    assert g.value('O') == -8

def test_catsgame():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_rc(0,0)[1] is None
    assert g.next_turn == 'O'
    assert g.play_rc(0,1)[1] is None
    assert g.next_turn == 'X'
    assert g.play_rc(0,2)[1] is None
    assert g.next_turn == 'O'
    assert g.play_rc(1,0)[1] is None
    assert g.next_turn == 'X'
    assert g.play_rc(1,1)[1] is None
    assert g.next_turn == 'O'
    assert g.play_rc(2,0)[1] is None
    assert g.next_turn == 'X'
    assert g.play_rc(1,2)[1] is None
    assert g.next_turn == 'O'
    assert g.play_rc(2,2)[1] is None
    assert g.next_turn == 'X'
    assert g.play_rc(2,1) == (1, 'C')
    assert g.winner() == 'C'
    assert g.value('X') == 5
    assert g.value('O') == 4

def test_badplay_o():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_rc(0,0) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(0,0) == (-100, 'E')
    assert g.next_turn == 'X'
    assert g.play_rc(0,1) == (0, 'E')
    assert g.winner() is 'X'
    assert g.value('O') == -100
    assert g.value('X') == 1

def test_badplay_o_second_turn():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_rc(0,0) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(1,0) == (1, None)
    assert g.next_turn == 'X'
    assert g.play_rc(1,1) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(0,0) == (-99, 'E')
    assert g.next_turn == 'X'
    assert g.play_rc(0,1) == (0, 'E')
    assert g.winner() is 'X'
    assert g.value('O') == -99
    assert g.value('X') == 2

def test_badplay_o_not_x():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_rc(0,0) == (1, None)
    assert g.next_turn == 'O'
    assert g.play_rc(0,0) == (-100, 'E')
    assert g.winner() == 'X'
    assert g.next_turn == 'X'
    assert g.play_rc(0,0) == (0, 'E')
    assert g.next_turn == 'O'
    assert g.play_rc(0,0) == (0, 'E')
    assert g.value('O') == -100
    assert g.value('X') == 1

def test_play_index():
    g = Game()
    assert g.next_turn == 'X'
    assert g.play_index(0)[1] is None
    assert g.next_turn == 'O'
    assert g.play_index(1)[1] is None
    assert g.next_turn == 'X'
    assert g.play_index(3)[1] is None
    assert g.next_turn == 'O'
    assert g.play_index(4)[1] is None
    assert g.winner() is None
    assert g.next_turn == 'X'
    assert g.play_index(6) == (11, 'X')
    assert g.winner() == 'X'
    assert g.value('X') == 13
    assert g.value('O') == -8

def test_get_board_as_vector():
    g = Game()
    g.play_index(0)
    g.play_index(1)
    g.play_index(3)
    np.testing.assert_array_equal(g.get_board_as_vector(), [1, -1, 0, 1, 0, 0, 0, 0, 0])