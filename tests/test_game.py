import sys

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
    assert g.play(0,0) is None
    assert g.turn == 'O'
    assert g.play(1,0) is None
    assert g.turn == 'X'
    assert g.play(0,1) is None
    assert g.turn == 'O'
    assert g.play(1,1) is None
    assert g.turn == 'X'
    assert g.play(0,2) == 'X'
    assert g.value('X') == 10
    assert g.value('O') == -10

