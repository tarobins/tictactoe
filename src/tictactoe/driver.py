from tf_agents.drivers import py_driver
from tf_agents.policies import random_py_policy
from tictactoe.tf_environment import TicTacToeEnv, action_spec

def play_game(env, x_policy, o_policy):
    x_buffer = []
    o_buffer = []

    x_driver = py_driver.PyDriver(env = env,
                                    policy = x_policy,
                                    observers = [x_buffer.append],
                                    max_steps = 1)
    
    o_driver = py_driver.PyDriver(env = env,
                                    policy = o_policy,
                                    observers = [o_buffer.append],
                                    max_steps = 1)

    x_policy_state = x_policy.get_initial_state()
    o_policy_state = o_policy.get_initial_state()

    time_step = env.reset()

    turn = 0
    while True:
        time_step, x_policy_state = x_driver.run(
            time_step, policy_state=x_policy_state)
        if time_step.is_last():
            break
        time_step, o_policy_state = o_driver.run(
            time_step, policy_state=o_policy_state)
        if time_step.is_last():
            break

    return x_buffer, o_buffer
