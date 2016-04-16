import util
import agent as Agent
import copy

class Actions:
    UP = 'Up'
    DOWN = 'Down'
    STOP = 'Stop'

class GameInfo:
    def __init__(self, boardsize):
        self.boardsize = boardsize

    def get_boardsize(self):
        return self.boardsize

class Queen:
    def __init__(self, GameInfo, pos = (0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.GameInfo = GameInfo

    def set_queen_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_queen_pos(self):
        return (self.x, self.y)

    def get_legal_actions(self):
        legal_actions = [(Actions.STOP, 0)]
        if self.y != 0:
            legal_actions.append((Actions.DOWN, self.y))
        if self.y != self.GameInfo.get_boardsize() - 1:
            legal_actions.append((Actions.UP, self.GameInfo.get_boardsize() - 1 - self.y))
        return legal_actions

    def action(self, action, distance=1):
        if action in [action for (action, distance) in self.get_legal_actions()]:
            if action == Actions.UP:
                self.y += distance
            elif action == Actions.DOWN:
                self.y -= distance

class GameStateData:
    def __init__(self, boardsize, prev_state = None):
        self.GameInfo = GameInfo(boardsize)
        if prev_state == None:
            self.queens = [Queen(pos = (x, x), GameInfo = self.GameInfo) for x in range(self.GameInfo.get_boardsize())]
        else:
            self.queens = copy.deepcopy(prev_state.queens)

class GameState:
    def __init__(self, boardsize, prev_state = None):
        if prev_state == None:
            self.data = GameStateData(boardsize)
        else:
            self.data = GameStateData(boardsize, prev_state.data)

    def is_queen(self, pos):
        if pos in [q.get_queen_pos() for q in self.queens]:
            return True
        else:
            return False

    def collision(self):
        queens = list(self.data.queens)
        count = 0
        while not len(queens) == 1:
            q = queens.pop()
            q_x, q_y = q.get_queen_pos()
            for other_queen in queens:
                o_x, o_y = other_queen.get_queen_pos()
                if q_x == o_x or q_y == o_y:
                    count += 1
                elif abs(q_x - o_x) == abs(q_y - o_y):
                    count += 1
        return count

    def get_board(self):
        board = [['X' for x in range(self.data.GameInfo.get_boardsize())] for x in range(self.data.GameInfo.get_boardsize())]
        for q in self.data.queens:
            x, y = q.get_queen_pos()
            board[x][y] = 'Q'
        return board

    def get_boardsize(self):
        return self.data.GameInfo.get_boardsize()

    def print_board(self):
        for line in self.get_board():
            print(line)

    def get_queen_num(self):
        return self.data.GameInfo.get_boardsize()

    def set_queen_pos(self, queen_index, pos):
        self.data.queens[queen_index].set_queen_pos(pos)

    def queen_action(self, queen_index, action, distance):
        self.data.queens[queen_index].action(action, distance)

    def generator_successor(self, queen_index, action, distance):
        state = GameState(boardsize=self.data.GameInfo.get_boardsize(),prev_state=self)
        state.queen_action(queen_index, action, distance)
        return state

    def get_legal_queen_actions(self, queen_index):
        return self.data.queens[queen_index].get_legal_actions()

    def is_win(self):
        if self.collision() == 0:
            return True
        else:
            return False

class Problem:
    def __init__(self, agent, boardsize=8):
        self.state = GameState(boardsize=boardsize)
        self.agent = agent

    def solve(self):
        while not self.state.is_win():
            queen_index, action, distance = self.agent.get_action(self.state)
            self.state.queen_action(queen_index, action, distance)
        print("Solution:")
        self.state.print_board()

def test():
    g = GameState()
    print(g.is_queen((0,0)))
    print(g.is_queen((0,1)))
    print(g.collision())
    g.print_board()
    newg = g.generator_successor(0, Actions.UP)
    newg.print_board()

def main():
    #test()
    agent = Agent.HillClimbingAgent()
    problem = Problem(agent=agent)
    problem.solve()

if __name__ == '__main__':
    main()
