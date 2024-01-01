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

    winner, x_history, y_history = drive(env, x_policy, o_policy)

    assert winner == 'X'
    print(x_history)
    print(y_history)

