import numpy as np

from tf_agents.drivers import py_driver
from tictactoe.q_table_policy import QTablePolicy
from tictactoe.tf_environment import TicTacToeEnv, action_spec
from tictactoe.driver import play_game
from tictactoe.hash_board import hash_board

def test_q_table_policy_driver():
    env = TicTacToeEnv()
    q_table_policy = QTablePolicy(time_step_spec=env.time_step_spec(), 
                                  action_spec=env.action_spec())
    
    driver = py_driver.PyDriver(env = env,
                                policy = q_table_policy,
                                observers = [],
                                max_steps = 1)
    
    policy_state = q_table_policy.get_initial_state()

    time_step = env.reset()

    time_step, policy_state = driver.run(time_step, policy_state=policy_state)

    expected = np.zeros(18)
    expected[0] = 1

    assert (time_step.observation == expected).all()

def test_train_one_turn():
    env = TicTacToeEnv()
    x_policy = QTablePolicy(time_step_spec=env.time_step_spec(), 
                                  action_spec=env.action_spec())
    
    o_policy = QTablePolicy(time_step_spec=env.time_step_spec(),
                            action_spec=env.action_spec())
    
    
    x_history, o_history = play_game(env, x_policy, o_policy)

    x_policy.train(x_history)
    o_policy.train(o_history)

    assert x_policy.q[hash_board(x_history[0].observation)][x_history[0].action] == 1
    assert o_policy.q[hash_board(o_history[0].observation)][o_history[0].action] == -100

def test_train_two_turn_game():
    env = TicTacToeEnv()
    x_policy = QTablePolicy(time_step_spec=env.time_step_spec(), 
                                  action_spec=env.action_spec())
    
    o_policy = QTablePolicy(time_step_spec=env.time_step_spec(),
                            action_spec=env.action_spec())
    
    
    x_history, o_history = play_game(env, x_policy, o_policy)

    x_policy.train(x_history)
    o_policy.train(o_history)

    x_history, o_history = play_game(env, x_policy, o_policy)

    x_policy.train(x_history)
    o_policy.train(o_history)

    assert x_policy.q[hash_board(x_history[-1].observation)][x_history[-1].action] == -99
    assert o_policy.q[hash_board(o_history[-1].observation)][o_history[-1].action] == 1

    