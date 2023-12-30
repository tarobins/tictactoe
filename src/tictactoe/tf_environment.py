import numpy as np

from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import StepType
from tf_agents.trajectories import time_step as ts

import tictactoe

observation_spec = array_spec.ArraySpec(
        shape=(9,), dtype=np.int32,  name='observation')
action_spec = array_spec.BoundedArraySpec(
        shape=(), dtype=np.int32, minimum=0, maximum=8, name='action')

class TicTacToeEnv(py_environment.PyEnvironment):
  def __init__(self):
    self._action_spec = action_spec
    self._observation_spec = observation_spec
    self._state = tictactoe.Game()
    self.x_policy = None        
    self.x_policy_state = None
    self.o_policy = None
    self.o_policy_state = None
    self.reset()

  def action_spec(self):
    return self._action_spec

  def observation_spec(self):
    return self._observation_spec

  def _reset(self):
    self._state = tictactoe.Game()
    self.x_policy_state = None
    self.o_policy_state = None
    self._auto_step()
    return ts.restart(np.array(self._state.get_board_as_vector(dtype=np.int32), dtype=np.int32))

  def _step(self, action):
    turn = self._state.next_turn
    if not hasattr(self, '_current_time_step') or self.current_time_step().step_type == StepType.LAST:
      res = self.reset()
      return res
    reward, winner = self._state.play_index(action)
    auto_winner = None
    if self._state.winner() is None:
      auto_winner = self._auto_step()

    if winner == None and auto_winner == None:
      return ts.transition(np.array(self._state.get_board_as_vector(dtype=np.int32), dtype=np.int32 ), reward=reward)
    else:
      return ts.termination(np.array(self._state.get_board_as_vector(dtype=np.int32), dtype=np.int32), reward=reward)

  def _auto_step(self):
    if self.x_policy != None and self.x_policy_state == None:
      self.x_policy_state = self.x_policy.get_initial_state()
    if self.o_policy != None and self.o_policy_state == None:
      self.o_policy_state = self.o_policy.get_initial_state()
    if self._state.next_turn == 'X' and self.x_policy != None:
      x_action = self.x_policy.action(self.current_time_step(), self.x_policy_state)
      self.x_policy_state = x_action.state
      _, winner = self._state.play_index(x_action.action)
      return winner
    if self._state.next_turn == 'O' and self.o_policy != None:
      o_action = self.o_policy.action(self.current_time_step(), self.o_policy_state)
      self.o_policy_state = o_action.state
      _, winner = self._state.play_index(o_action.action)
      return winner
