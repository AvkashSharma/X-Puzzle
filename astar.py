import numpy as np
from puzzle import Puzzle

class Node:
    def __init__(self, parent=None, puzzle=None, cost=0):
        self.parent = parent
        self.puzzle = puzzle
        self.cost = cost

def getItemFromList(arr, puzzle):
    for a in arr:
        if (a.puzzle == puzzle).all():
            return a

class Astar:
    openList = []
    closedList = []

    def __init__(self, initial):
        # intitalize lists
        np.array(self.openList, dtype=Puzzle)
        np.array(self.closedList, dtype=Puzzle)
        self.goal1 = Puzzle(input='1 2 3 4 5 6 7 0', g=0, f=0)
        self.goal2 = Puzzle(input='1 3 5 7 2 4 6 0', g=0, f=0)
        
        self.initial = initial
        self.openList.append(self.initial)

        i = 0
        while len(self.openList) != 0:
            print("Epoch :" + str(i))
            # sort open list
            self.openList.sort(key=lambda x:x.f)
            
            # print('openList')
            # print(self.openList)
            # print('closedList')
            print(self.closedList)
            for c in self.closedList:
                c.print()

            # get first item
            currentNode = self.openList.pop()
            # print('CurrentNode: ')
            # currentNode.print()
            self.closedList.append(currentNode);

            # compare with goal
            if (currentNode.puzzle == self.goal1.puzzle).all():
                print('goal1 found');
                break;

            if (currentNode.puzzle == self.goal2.puzzle).all():
                print('goal2 found');
                break;

            children = currentNode.getMoves()
            for child in children:
                # check if child in closedList
                if any((x.puzzle == child.puzzle).all() for x in self.closedList):
                    # if exist skip the rest of the loop
                    continue

                
                # print(str(currentNode.g) +" "+ str(child.g))
                # g = currentNode.g + distance between child and current
                child.g = currentNode.g + child.g
                # h = huristic function
                child.h = 0
                # f = g+h
                child.f = child.g + child.h

                # check if child in openList
                if any((x.puzzle == child.puzzle).all() for x in self.openList):
                    # check if child.g is higher then openlist g 
                    print('Child is in openList')
                    openNode = getItemFromList(self.openList, child.puzzle)
                    if child.g > openNode.g:
                        continue
                
                 # add child to openlist
                self.openList.append(child)

               
            # print(children)
            # break;
            i = i+1
            
            # if i == 20:
            #     break;
        # sort the list



        # put initial state in openList
        # f = 0

        # while loop until openList is not empty
        # currentNode = n with least f value
        # remove currentNode from openlist
        # add currentNode to closedList

        # check currentNode is goal

        # if not then get children node
        # 




input = "1 2 3 4 0 5 6 7"
# input = '1 3 5 7 2 4 6 0'

puzzle = Puzzle(input=input, g=0, f=0)
# puzzle.print()
# puzzle.getMoves()

a = Astar(puzzle)