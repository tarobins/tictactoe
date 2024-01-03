from tictactoe.driver import play_game, battle
from tictactoe.tf_environment import TicTacToeEnv, action_spec
from tf_agents.policies import scripted_py_policy

def test_play_game_x_wins():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 1), (1, 2)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 3), (1, 4)])
    
    env = TicTacToeEnv()

    x_history, _ = play_game(env, x_policy, o_policy)

    assert x_history[-1].reward == 11
    assert x_history[-1].is_last()

def test_play_game_o_wins():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 1), (1, 6)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 3), (1, 4), (1, 5)])
    
    env = TicTacToeEnv()

    _, o_history = play_game(env, x_policy, o_policy)

    assert o_history[-1].reward == 11
    assert o_history[-1].is_last()

def test_play_game_o_bad():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0)])
    
    env = TicTacToeEnv()

    _, o_history = play_game(env, x_policy, o_policy)

    assert o_history[-1].reward == -100
    assert o_history[-1].is_last()

def test_play_game_cats():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 2), (1, 4), (1, 5), (1, 7)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 1), (1, 3), (1, 6), (1, 8)])
    
    env = TicTacToeEnv()

    x_history, o_history = play_game(env, x_policy, o_policy)

    assert x_history[-1].reward == 1
    assert x_history[-1].is_last()

    assert o_history[-1].reward == 1
    assert o_history[-1].is_mid()

def test_battle():
    x_policy_x_win = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 1), (1, 2)])
    
    o_policy_o_win = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 3), (1, 4)])
    
    env = TicTacToeEnv()

    x_rewards, o_rewards = battle(env, x_policy_x_win, o_policy_o_win, 100)

    assert x_rewards == 13
    assert o_rewards == 2

def test_battle_callback():
    x_policy_x_win = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 1), (1, 2)])
    
    o_policy_o_win = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 3), (1, 4)])
    
    env = TicTacToeEnv()

    num_calls = 0

    def callback(x_history, o_history):
        nonlocal num_calls
        num_calls = num_calls + 1

    x_rewards, o_rewards = battle(env, x_policy_x_win, o_policy_o_win, 100, callback)

    assert x_rewards == 13
    assert o_rewards == 2
    assert num_calls == 100
    