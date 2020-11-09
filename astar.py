import numpy as np
from puzzle import Puzzle

class Node:
    def __init__(self, parent=None, puzzle=None, cost=0):
        self.parent = parent
        self.puzzle = puzzle
        self.cost = cost

    
class Astar:
    openList = []
    closedList = []

    def __init__(self, initial):
        # intitalize lists
        np.array(self.openList,dtype=Puzzle)
        np.array(self.closedList,dtype=Puzzle)
        self.goal1 = Puzzle(input='1 2 3 4 5 6 7 0', g=0, f=0)
        self.goal2 = Puzzle(input='1 3 5 7 2 4 6 0', g=0, f=0)
        
        self.initial = initial
        self.openList.append(self.initial)

        a = Puzzle(input='0 2 3 1 5 6 7 4', g=0, f=2)
        a.print()
        for c in a.getMoves():
            c.print()
        self.openList.append(Puzzle(input='0 2 3 1 5 6 7 4', g=0, f=2))

        # i = 0
        while len(self.openList) != 0:
            # sort open list
            self.openList.sort(key=lambda x:x.f)
            for c in self.openList:
                c.print()

            # get first item
            currentNode = self.openList.pop()
            print('CurrentNode: ')
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

                print(child.puzzle)

                # check if child in closedList
                if any((x.puzzle == child.puzzle).all() for x in self.closedList):
                    # if exist skip the rest of the loop
                    continue

                
                print(str(currentNode.g) +" "+ str(child.g))
                # g = currentNode.g + distance between child and current
                child.g = currentNode.g + child.g
                # h = huristic function
                child.h = 0
                # f = g+h
                child.f = child.g + child.h

                # check if child in openList
                if any((x.puzzle == child.puzzle).all() for x in self.openList):
                    # check if child.g is higher then openlist g 
                    openListNode = np.where(self.openList == child.puzzle)
                    print(openListNode)
                    continue

                #   if child.g is higher than the openList node.g
                        # continue 

                # add child to openlist
            # print(children)
            break;
            i = i+1
            print("Epoch :" + str(i))
            if i == 2:
                break;
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




input = "4 2 3 1 5 6 7 0"
# input = '1 3 5 7 2 4 6 0'

puzzle = Puzzle(input=input, g=0, f=0)
# puzzle.print()
# puzzle.getMoves()

a = Astar(puzzle)