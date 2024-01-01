from tictactoe.driver import drive
from tictactoe.tf_environment import TicTacToeEnv, action_spec
from tf_agents.policies import scripted_py_policy

def test_driver_x_wins():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 1), (1, 2)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 3), (1, 4)])
    
    env = TicTacToeEnv()

    x_history, _ = drive(env, x_policy, o_policy)

    assert x_history[-1].reward == 11
    assert x_history[-1].is_last()


def test_driver_cats():
    x_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 0), (1, 2), (1, 4), (1, 5), (1, 7)])
    
    o_policy = scripted_py_policy.ScriptedPyPolicy(
        time_step_spec=None, 
        action_spec=action_spec, action_script=[(1, 1), (1, 3), (1, 6), (1, 8)])
    
    env = TicTacToeEnv()

    x_history, o_history = drive(env, x_policy, o_policy)

    assert x_history[-1].reward == 1
    assert x_history[-1].is_last()

    assert o_history[-1].reward == 1
    assert not o_history[-1].is_last()