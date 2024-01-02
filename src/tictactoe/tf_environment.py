import numpy as np

from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import StepType
from tf_agents.trajectories import time_step as ts

import tictactoe

observation_spec = array_spec.ArraySpec(
        shape=(18,), dtype=np.uint8,  name='observation')
action_spec = array_spec.BoundedArraySpec(
        shape=(), dtype=np.int32, minimum=0, maximum=8, name='action')

class TicTacToeEnv(py_environment.PyEnvironment):
  def __init__(self):
    self._action_spec = action_spec
    self._observation_spec = observation_spec
    self._state = tictactoe.Game()
    self.reset()

  def action_spec(self):
    return self._action_spec

  def observation_spec(self):
    return self._observation_spec

  def _reset(self):
    self._state = tictactoe.Game()
    return ts.restart(np.array(self._state.get_board_as_bit_vector(), dtype=np.int32))

  def _step(self, action):
    turn = self._state.next_turn
    if not hasattr(self, '_current_time_step') or self.current_time_step().step_type == StepType.LAST:
      res = self.reset()
      return res
    reward, winner = self._state.play_index(action)

    if winner == None:
      return ts.transition(np.array(self._state.get_board_as_bit_vector(), dtype=np.int32 ), reward=reward)
    else:
      return ts.termination(np.array(self._state.get_board_as_bit_vector(), dtype=np.int32), reward=reward)
