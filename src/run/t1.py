from tictactoe.driver import battle
from tictactoe.tf_environment import TicTacToeEnv
from tictactoe.q_table_policy import QTablePolicy
from tf_agents.policies import random_py_policy

env = TicTacToeEnv()

x_policy = QTablePolicy(time_step_spec=env.time_step_spec(), 
                                action_spec=env.action_spec())

o_policy = QTablePolicy(time_step_spec=env.time_step_spec(),
                        action_spec=env.action_spec())

random_py_policy = random_py_policy.RandomPyPolicy(
    time_step_spec=env.time_step_spec(), action_spec=env.action_spec())

# x_rewards, o_rewards = battle(env, x_policy, o_policy, 100)
# print(f'x_q vs o_q before training x: {x_rewards} o: {o_rewards}')

train_episodes = 10

x_rewards, o_rewards, x_wins, o_winds = battle(env, x_policy, o_policy, 100)
print(f'>>>> x_q vs o_q before training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_winds}')

x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, random_py_policy, 100)
print(f'>>>> x_q vs random before training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_wins}')

def train(x_history, o_history):
    x_policy.train(x_history)

for i in range(1000):

    x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, random_py_policy, train_episodes, train)
    if i % 100 == 0:
        x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, random_py_policy, 100) 
        print(f'x_q vs random after {i * train_episodes} x: {x_rewards} o: {o_rewards}')


x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, o_policy, 100)
print(f'>>>> x_q vs o_q after training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_wins}')

x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, random_py_policy, 100)
print(f'>>>> x_q vs random after training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_wins}')

def train(x_history, o_history):
    x_policy.train(x_history)
    o_policy.train(o_history)

for i in range(1000):

    x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, o_policy, train_episodes, train)
    if i % 100 == 0:
        x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, o_policy, 100) 
        print(f'x_q vs o_q after {i * train_episodes} x: {x_rewards} o: {o_rewards}')


x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, o_policy, 100)
print(f'>>>> x_q vs o_q after training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_wins}')

x_rewards, o_rewards, x_wins, o_wins = battle(env, x_policy, random_py_policy, 100)
print(f'>>>> x_q vs random after training x: {x_rewards} o: {o_rewards} x_wins: {x_wins} o_wins: {o_wins}')

# for i in range(1000):

#     x_rewards, o_rewards = battle(env, o_policy, x_policy, train_episodes, train)
#     if i % 100 == 0:
#         x_rewards, o_rewards = battle(env, o_policy, x_policy, 100) 
#         print(f'o_q vs x_q after {i * train_episodes} x: {x_rewards} o: {o_rewards}')   

# x_rewards, o_rewards = battle(env, x_policy, o_policy, 100)
# print(f'x_q vs o_q after training x: {x_rewards} o: {o_rewards}')

# x_rewards, o_rewards = battle(env, x_policy, random_py_policy, 100)
# print(f'x_q vs random after training x: {x_rewards} o: {o_rewards}')

# x_rewards, o_rewards = battle(env, o_policy, x_policy, 100)
# print(f'o_q vs x_q after training x: {x_rewards} o: {o_rewards}')

# x_rewards, o_rewards = battle(env, x_policy, x_policy, 100)
# print(f'x_q vs x_q after training x: {x_rewards} o: {o_rewards}')
