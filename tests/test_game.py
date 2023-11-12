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

def test_catsgame():
    g = Game()
    assert g.turn == 'X'
    assert g.play(0,0) is None
    assert g.turn == 'O'
    assert g.play(0,1) is None
    assert g.turn == 'X'
    assert g.play(0,2) is None
    assert g.turn == 'O'
    assert g.play(1,0) is None
    assert g.turn == 'X'
    assert g.play(1,1) is None
    assert g.turn == 'O'
    assert g.play(2,0) is None
    assert g.turn == 'X'
    assert g.play(1,2) is None
    assert g.turn == 'O'
    assert g.play(2,2) is None
    assert g.turn == 'X'
    assert g.play(2,1) == 'C'
    assert g.value('X') == 5
    assert g.value('O') == 5

def test_badplay_x():
    g = Game()
    assert g.turn == 'X'
    assert g.play(0,0) is None
    assert g.turn == 'O'
    assert g.play(0,0) == 'E'
    assert g.turn == 'X'
    assert g.play(0,1) is 'E'
    assert g.value('X') == -100
    assert g.value('O') == 0