import numpy as np
from puzzle import Puzzle

class Node:
    def __init__(self, parent=None, puzzle=None, cost=0):
        self.parent = parent
        self.puzzle = puzzle
        self.cost = cost

    