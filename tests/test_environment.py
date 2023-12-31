import numpy as np  

from tf_agents.policies import scripted_py_policy
from tictactoe.tf_environment import TicTacToeEnv, action_spec

def test_no_auto_x_wins():
    env = TicTacToeEnv()
    state = env.reset()
    assert state.step_type == 0
    assert state.reward == 0
    assert state.discount == 1
    assert (state.observation == np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])).all()

    # X
    state = env.step(6)
    assert state.step_type == 1
    assert state.reward == 1
    assert state.discount == 1
    assert (state.observation == np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])).all()
    
    # O
    state = env.step(0)
    assert (state.observation == np.array([0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0])).all()

    # X
    state = env.step(7)
    assert (state.observation == np.array([0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0])).all()

    # O
    state = env.step(1)
    assert (state.observation == np.array([0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0])).all()
    assert state.reward == 1

    # X
    state = env.step(8)
    assert (state.observation == np.array([0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0])).all()
    assert state.step_type == 2
    assert state.reward == 11

def test_no_auto_0_wins():
    env = TicTacToeEnv()
    state = env.reset()
    assert state.step_type == 0
    assert state.reward == 0
    assert state.discount == 1
    assert (state.observation == np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])).all()

    # X
    state = env.step(6)
    assert state.step_type == 1
    assert state.reward == 1
    assert state.discount == 1
    assert (state.observation == np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])).all()
    
    # O
    state = env.step(0)
    assert (state.observation == np.array([0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0])).all()

    # X
    state = env.step(7)
    assert (state.observation == np.array([0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0])).all()

    # O
    state = env.step(1)
    assert (state.observation == np.array([0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0])).all()
    assert state.reward == 1

    # X
    state = env.step(5)
    assert (state.observation == np.array([0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0])).all()
    assert state.step_type == 1
    assert state.reward == 1

    # # O
    # assert state.step_type == 2
    # assert state.reward == 11

def test_bad_play():
    env = TicTacToeEnv()
    state = env.reset()

    state = env.step(0)
    state = env.step(0)

    assert state.reward == -100

def test_autoplay_x():
    env = TicTacToeEnv()

    script = [(1,0),(1,1),(1,2)]
    scripted_x_policy = scripted_py_policy.ScriptedPyPolicy(time_step_spec=None, action_spec=action_spec, action_script=script)
    env.x_policy = scripted_x_policy

    state = env.reset()
    assert (state.observation == np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])).all()
    state = env.step(6)
    assert (state.observation == np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])).all()

def test_autoplay_o():
    env = TicTacToeEnv()

    script = [(1,0),(1,1),(1,3)]
    scripted_o_policy = scripted_py_policy.ScriptedPyPolicy(time_step_spec=None, action_spec=action_spec, action_script=script)
    env.o_policy = scripted_o_policy

    state = env.reset()
    state = env.step(6)
    assert (state.observation == np.array([0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0])).all()


