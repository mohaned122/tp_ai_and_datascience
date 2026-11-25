class MazeEnv:
    SIZE = 5
    OBSTACLES = {(0, 3), (1, 1), (1, 3), (2, 1), (3, 2), (3, 3), (4, 0)}
    START = (0, 0)
    GOAL = (4, 4)
    DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))  # haut, bas, gauche, droite

    def __init__(self):
        self.position = self.START

    @staticmethod
    def to_state(position):
        row, col = position
        return 5 * row + col

    def reset(self):
        self.position = self.START
        return self.to_state(self.position)

    def step(self, action):
        if action not in range(4):
            raise ValueError('Action invalide')
        dr, dc = self.DELTAS[action]
        row, col = self.position
        new = (row + dr, col + dc)
        if (not (0 <= new[0] < 5 and 0 <= new[1] < 5)) or new in self.OBSTACLES:
            return self.to_state(self.position), -10., False
        self.position = new
        reached = new == self.GOAL
        return self.to_state(new), (100. if reached else -1.), reached

    def render(self):
        for r in range(5):
            print(' '.join('R' if (r,c)==self.position else
                           'G' if (r,c)==self.GOAL else
                           'X' if (r,c) in self.OBSTACLES else '.'
                           for c in range(5)))
        print()