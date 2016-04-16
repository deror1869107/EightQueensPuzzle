import util
from eightqueens import Actions

class Agent:
    def get_action(self, state):
        util.raiseNotDefined()

class HillClimbingAgent(Agent):
    def get_action(self, state):
        input()
        state.print_board()
        next_action = (0, Actions.STOP, 0, state.collision());
        for queen_index in range(state.get_queen_num()):
            for (action, distance) in state.get_legal_queen_actions(queen_index):
                if action != Actions.STOP:
                    for next_dis in range(1, distance + 1):
                        s = state.generator_successor(queen_index, action, next_dis)
                        heuristic = s.collision()
                        #heuristic = state.generator_successor(queen_index, action, next_dis).collision()
                        #print(heuristic)
                        if heuristic < next_action[3]:
                            next_action = (queen_index, action, distance, heuristic)
        print(next_action[3])
        return next_action[0:3]
        util.raiseNotDefined()

class OneSolutionAgent(Agent):
    def __init__(self):
        self.solution = [(0, Actions.UP, 5), (1, Actions.UP, 2), (2, Actions.UP, 4), (3, Actions.DOWN, 3), (4, Actions.UP, 3), (5, Actions.DOWN, 4), (6, Actions.DOWN, 2), (7, Actions.DOWN, 5)]
        self.step_count = -1

    def get_action(self, state):
        self.step_count += 1
        return self.solution[self.step_count]
