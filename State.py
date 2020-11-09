from math import cos
import numpy as np

class State:
    def __init__(self, input="", puzzle=None, f=0, g=0, h=0, heuristic=""):
        self.row = 2
        self.col = 4
        self.f = f
        self.g = g
        self.heuristic = heuristic

        if input!="":
            inputList = input.split(" ")
            npMatrix = np.split(np.array(inputList), self.row)
            self.puzzle = np.vstack(npMatrix)
        
        if puzzle is not None:
            self.puzzle = puzzle

        if heuristic == "h0":
            self.h = self.h0(self)
        elif heuristic == "h1":
            self.h = self.h1(self)
        elif heuristic == "h2":
            self.h = self.h2(self)
        else:
            self.h = h
        
        
    def print(self):
        print(self.puzzle)
        print("G(N): "+ str(self.g))
        print("H(N): "+ str(self.h))

    def getMoves(self):
        moves = []
        zero = self.getPosition('0')

        downMove = self.moveDown(zero)
        if downMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, downMove), g=1, heuristic=self.heuristic))

        upMove = self.moveUp(zero)
        if upMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, upMove), g=1, heuristic=self.heuristic))

        leftMove = self.moveLeft(zero)
        if leftMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, leftMove), g=1, heuristic=self.heuristic))

        rightMove = self.moveRight(zero)
        if rightMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, rightMove), g=1, heuristic=self.heuristic))
        
        wrapMove = self.moveWrapper(zero)
        if wrapMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, wrapMove), g=2, heuristic=self.heuristic))

        diagonalMove = self.moveDiagonal(zero)
        if diagonalMove is not None:
            for diag in diagonalMove:
                moves.append(State(puzzle=self.swapPosition(zero, diag), g=3, heuristic=self.heuristic))

        

        return moves

# get position
    def getPosition(self, pos):
        return np.argwhere(self.puzzle == pos)[0]

# there is probabily a better way
    def swapPosition(self, posA, posB):
        toSwap = np.copy(self.puzzle)
        a = self.puzzle[posA[0],posA[1]]
        b = self.puzzle[posB[0],posB[1]]
        toSwap[posA[0],posA[1]] = b
        toSwap[posB[0],posB[1]] = a
        return toSwap

    def moveDown(self, pos):
        if pos[0]!=self.row-1: 
            return self.getPosition(self.puzzle[pos[0]+1][pos[1]])
        else: return None

    def moveUp(self, pos):
        if pos[0]!=0: 
            return self.getPosition(self.puzzle[pos[0]-1][pos[1]])
        else: return None

    def moveLeft(self, pos):
        if pos[1]!=0: 
            return self.getPosition(self.puzzle[pos[0]][pos[1]-1])
        else: return None

    def moveRight(self, pos):
        if pos[1]!=self.col-1: 
            return self.getPosition(self.puzzle[pos[0]][pos[1]+1])
        else: return None

    def moveWrapper(self, pos):
        if self.isCorner(pos):
            if pos[1] == 0:
                return self.getPosition(self.puzzle[pos[0]][self.col-1])
            elif pos[1] == self.col-1:
                return self.getPosition(self.puzzle[pos[0]][0])
        return None

    def moveDiagonal(self, pos):
        if self.isCorner(pos):
            # r1, c1 - adjacent
            # r2, c2 - opposite corner
            r1= c1= r2= c2 = 0

            # rows
            if pos[0] == 0:
                r1 = 1
                r2 = self.row -1
            elif pos[0] == self.row-1:
                r1 = self.row-2

            # cols
            if pos[1] == 0:
                c1 = 1
                c2 =self.col -1
            elif pos[1] == self.col-1:
                c1 = self.col-2
            
            return np.array([[r1, c1], [r2, c2]])
        return None


    def isCorner(self, pos):
        r = pos[0]
        c = pos[1]

        if (pos == [0,0]).all():
            return True
        elif (pos == [self.row - 1,0]).all():
            return True
        elif (pos == [0 , self.col-1]).all():
            return True
        elif (pos == [self.row - 1, self.col -1]).all():
            return True

    def h0(self, state):
        pos = state.getPosition('0')
        if(pos == [state.row-1, state.col-1]).all():
            return 0
        else:
            return 1
        print('Heuristic 0')

    def h1(self, state):
        pos = state.getPosition('0')
        if(pos == [state.row-1, state.col-1]).all():
            return 0
        else:
            return 1
        print('Heuristic 1')

    def h2(self, state):
        pos = state.getPosition('0')
        if(pos == [state.row-1, state.col-1]).all():
            return 0
        else:
            return 1
        print('Heuristic 2')


#Below is just a sample test

# Visited State
input = "4 2 3 1 5 6 7 0"
input2 = "1 2 3 4 5 6 7 0"
input3 = "1 2 3 4 5 6 0 7"

state = State(input=input, heuristic="h2")
state.print()

goalState1 = State(input='1 2 3 4 5 6 7 0')
goalState2 = State(input='1 3 5 7 2 4 6 0')

# Is It Goal State
if (state.puzzle == goalState1.puzzle).all():
    print('goal1 found')
elif (state.puzzle == goalState2.puzzle).all():
    print('goal2 found')
else:
    # Open List
    moves = state.getMoves()
    for m in  moves:
        print(m.puzzle)
        print("G(N): "+ str(m.g))
        print("H(N): "+ str(m.h))
    

