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
        self.goal1 = Puzzle(input='1 2 3 4 5 6 7 0', cost=0, f=0)
        self.goal2 = Puzzle(input='1 3 5 7 2 4 6 0', cost=0, f=0)
        
        self.initial = initial
        self.openList.append(self.initial)


        while len(self.openList) != 0:
            # sort open list
            self.openList.sort(key=lambda x:x.f)
            # get first item
            currentNode = self.openList.pop()
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
                # if exist skip use continue

                # get f, g, h of child
                # g = currentNode.g + distance between child and current
                # h = huristic function
                # f = g+h

                # if child in openList
                #   if child.g is higher than the openList node.g
                        # continue 

                # add child to openlist
            # print(children)
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

puzzle = Puzzle(input=input, cost=0, f=0)
# puzzle.print()
# puzzle.getMoves()

a = Astar(puzzle)