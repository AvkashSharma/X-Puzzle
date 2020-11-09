import os
from state import State
from astar import Astar

file = open("samplePuzzles.txt","r")

i = 0
for line in file:
    print("puzzle"+str(i))
    puzzle = State(input=line.strip(), g=0, f=0)
    puzzle.print()

    astarH0 = Astar(initial=puzzle, puzzleNumber=i, h_type="h0")
    astarH1 = Astar(initial=puzzle, puzzleNumber=i, h_type="h1")
    i=i+1
file.close()



# input = "0 2 3 1 5 6 7 4"

# puzzle = State(input=input, g=0, f=0)


# a = Astar(puzzle,  puzzleNumber=0, h_type="h0")