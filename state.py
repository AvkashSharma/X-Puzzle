from math import cos
import numpy as np

class State:
    def __init__(self, input="", puzzle=None, f=0, g=0, totalG=0, h=0, heuristic="", goalState1=None, goalState2=None):
        self.row = 2
        self.col = 4
        self.f = f
        self.g = g
        self.totalG = totalG
        self.heuristic = heuristic
        self.goalState1 = goalState1
        self.goalState2 = goalState2

        if input!="":
            inputList = input.split(" ")
            npMatrix = np.split(np.array(inputList), self.row)
            self.puzzle = np.vstack(npMatrix)
        
        if puzzle is not None:
            self.puzzle = puzzle

        if heuristic == "h0":
            self.h = self.h0()
        elif heuristic == "h1":
            self.h = self.h1()
        elif heuristic == "h2":
            self.h = self.h2()
        else:
            self.h = h
        
    def print(self):
        print(self.puzzle)
        print("Cumalative G(N)" + str(self.totalG))
        print("G(N): "+ str(self.g))
        print("H(N): "+ str(self.h))

    def getMoves(self):
        moves = []
        zero = self.getPosition('0')

        downMove = self.moveDown(zero)
        if downMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, downMove), g=1, totalG = self.totalG + 1, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))

        upMove = self.moveUp(zero)
        if upMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, upMove), g=1, totalG = self.totalG + 1, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))

        leftMove = self.moveLeft(zero)
        if leftMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, leftMove), g=1, totalG = self.totalG + 1, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))

        rightMove = self.moveRight(zero)
        if rightMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, rightMove), g=1, totalG = self.totalG + 1, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))
        
        wrapMove = self.moveWrapper(zero)
        if wrapMove is not None:
            moves.append(State(puzzle=self.swapPosition(zero, wrapMove), g=2, totalG = self.totalG + 2, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))

        diagonalMove = self.moveDiagonal(zero)
        if diagonalMove is not None:
            for diag in diagonalMove:
                moves.append(State(puzzle=self.swapPosition(zero, diag), g=3, totalG = self.totalG + 3, heuristic=self.heuristic, goalState1=self.goalState1, goalState2=self.goalState2))

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

    def h0(self):
        pos = self.getPosition('0')
        if(pos == [self.row-1, self.col-1]).all():
            return 0
        else:
            return 1

    def h1(self):
        counter = 0
        for i in range(self.row):
            for j in range(self.col):
                if (self.puzzle[i, j] != self.goalState1.puzzle[i, j] and self.puzzle[i, j] != 0):
                    counter = counter + 1

        return counter

    def h2(self):
        counter = 0
        singleArrayPuzzle = self.puzzle.flatten()
        singleArrayGoalPuzzle1 = self.goalState1.puzzle.flatten()
        for i in singleArrayPuzzle:
            counter = self.findMissPlaceTiles(i, singleArrayPuzzle, singleArrayGoalPuzzle1)
            
        return counter

    def findMissPlaceTiles(self, index, puzzle, goalPuzzle):
        counter = 0
        for index in range(self.row * self.col - 1):
            if (puzzle[index] != goalPuzzle.puzzle[index] and puzzle[index] != 0):
                counter = counter + 1
        return counter
