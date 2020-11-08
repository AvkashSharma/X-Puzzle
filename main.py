from puzzle import Puzzle
from astar import Astar

input = "4 2 3 1 5 6 7 0"

puzzle = Puzzle(input=input, cost=0, f=0)
# puzzle.print()
# puzzle.getMoves()

a = Astar(puzzle)
# print(len(a.openList))
# print(a.openList[0].print())