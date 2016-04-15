import util
from eightqueens import Actions

class Agent:
    def get_action(self, state):
        util.raiseNotDefined()

class HillClimbingAgent(Agent):
    def get_action(self, state):
        util.raiseNotDefined()

class OneSolutionAgent(Agent):
    def __init__(self):
        self.solution = [(0, Actions.UP, 5), (1, Actions.UP, 2), (2, Actions.UP, 4), (3, Actions.DOWN, 3), (4, Actions.UP, 3), (5, Actions.DOWN, 4), (6, Actions.DOWN, 2), (7, Actions.DOWN, 5)]
        self.step_count = -1

    def get_action(self, state):
        self.step_count += 1
        return self.solution[self.step_count]
