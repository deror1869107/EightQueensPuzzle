import util
import agent as Agent

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

    def get_legal_Actions(self):
        legal_Actions = [Actions.UP, Actions.DOWN, Actions.STOP]
        if self.y == 0:
            legal_Actions.remove(Actions.DOWN)
        elif self.y == self.GameInfo.get_boardsize() - 1:
            legal_Actions.remove(Actions.UP)
        return legal_Actions

    def action(self, action, distance=1):
        if action in self.get_legal_Actions():
            if action == Actions.UP:
                self.y += distance
            elif action == Actions.DOWN:
                self.y -= distance

class GameState:
    def __init__(self, boardsize, prev_state = None):
        if prev_state == None:
            self.GameInfo = GameInfo(boardsize)
            self.queens = [Queen(pos = (x, x), GameInfo = self.GameInfo) for x in range(self.GameInfo.get_boardsize())]
        else:
            self.GameInfo = prev_state.GameInfo
            self.queens = list(prev_state.queens)

    def is_queen(self, pos):
        if pos in [q.get_queen_pos() for q in self.queens]:
            return True
        else:
            return False

    def collision(self):
        queens = list(self.queens)
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
        board = [['X' for x in range(self.GameInfo.get_boardsize())] for x in range(self.GameInfo.get_boardsize())]
        for q in self.queens:
            x, y = q.get_queen_pos()
            board[x][y] = 'Q'
        return board

    def print_board(self):
        for line in self.get_board():
            print(line)

    def get_queen_num(self):
        return self.GameInfo.get_boardsize()

    def queen_action(self, queen_index, action, distance):
        self.queens[queen_index].action(action, distance)

    def generator_successor(self, queen_index, action):
        state = GameState(prev_state=self)
        state.queen_action(queen_index, action)
        return state

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
    agent = Agent.OneSolutionAgent()
    problem = Problem(agent=agent)
    problem.solve()

if __name__ == '__main__':
    main()
