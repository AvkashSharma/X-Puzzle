from puzzle import Puzzle
from astar import Astar

input = "0 2 3 1 5 6 7 4"

puzzle = Puzzle(input=input, g=0, f=0)


a = Astar(puzzle)
# print(len(a.openList))
# print(a.openList[0].print())