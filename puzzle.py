from math import cos
import numpy as np
import numpy

class Puzzle:


    def __init__(self, input="", cost=0, puzzle=None):
        self.row = 2
        self.col = 4

        if input!='':
            inputList = input.split(" ")
            npMatrix = np.split(np.array(inputList), self.row)
            self.puzzle = np.vstack(npMatrix)
        
        if puzzle is not None:
            self.puzzle = puzzle

        self.cost = cost
        
    def print(self):
        print(self.puzzle)
        print("Cost: "+ str(self.cost))

    def getMoves(self):
        moves = []
        zero = self.getPosition('0')
        # self.isCorner(zero)

        downMove = self.moveDown(zero)
        if downMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, downMove), cost=1))

        upMove = self.moveUp(zero)
        if upMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, upMove), cost=1))

        leftMove = self.moveLeft(zero)
        if leftMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, leftMove), cost=1))

        rightMove = self.moveRight(zero)
        if rightMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, rightMove), cost=1))
        
        wrapMove = self.moveWrapper(zero)
        if wrapMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, wrapMove), cost=2))

        diagonalMove = self.moveDiagonal(zero)
        if diagonalMove is not None:
            moves.append(Puzzle(puzzle=self.swapPosition(zero, diagonalMove), cost=3))


        for m in  moves:
            print(m.puzzle)

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
# todo
    def moveDiagonal(self, pos):
        return None
# todo
    def moveWrapper(self, pos):
        return None

    # def isCorner(self, pos):
    #     r = pos[0]
    #     c = pos[1]

    #     print(str(r) + ","+str(c))
    #     if (pos == [0,0]).all():
    #         print(str(r) + ","+str(c))
    #     elif (pos == [self.row - 1,0]).all():
    #         print(str(r) + ","+str(c))
    #     elif (pos == [0 , self.col-1]).all():
    #         print(str(r) + ","+str(c))
    #     elif (pos == [self.row - 1, self.col -1]).all():
    #         print(str(r) + ","+str(c))


input = "0 6 2 7 4 1 3 5"

puzzle = Puzzle(input=input, cost=0)
puzzle.print()
puzzle.getMoves()

