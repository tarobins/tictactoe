import numpy as np

from typing import Optional
from tf_agents.policies import py_policy
from tf_agents.policies.random_py_policy import RandomPyPolicy
from tf_agents.trajectories.policy_step import PolicyStep
from tf_agents.trajectories.time_step import TimeStep
from tf_agents.typing.types import NestedArray, Seed
from tictactoe.hash_board import hash_board

class QTablePolicy(py_policy.PyPolicy):

    def __init__(self,
                    time_step_spec: TimeStep,
                    action_spec: NestedArray,
                    q_init = 0.6,
                    learning_rate: float = 0.6,
                    name: str = None, ) -> None:
            self.q = {}
            self.eps = 0
            self.q_init = q_init
            self.learning_rate = learning_rate
            self._random = RandomPyPolicy(time_step_spec, action_spec)
            super().__init__(time_step_spec, action_spec)

    def _get_q(self, board_hash):
         if board_hash not in self.q:
             self.q[board_hash] = np.full(9, self.q_init)
         return self.q[board_hash]

    def _action(self, 
                time_step: TimeStep, 
                policy_state: NestedArray = (),
                seed: Seed | None = None) -> PolicyStep:
        # print(f'>>>>>>>>> {time_step} >>>>>>> {policy_state} >>>>>> {seed}')
        board_hash = hash_board(time_step.observation)
        if np.random.random() < self.eps:
            # print('random action')
            return self._random.action(time_step)
        q = self._get_q(board_hash)
        move = np.argmax(q)
        return PolicyStep(action=move, state=policy_state, info=())

    def train(self, experience):
        reversed_experience = experience[::-1]
        for i, exp in enumerate(reversed_experience):
            q = self._get_q(hash_board(exp.observation))
            if i == 0:
                q[exp.action] = exp.reward
            else:
                q[exp.action] = (1 - self.learning_rate) * q[exp.action] + exp.discount * self.learning_rate * next_max
            next_max = max(q)
        