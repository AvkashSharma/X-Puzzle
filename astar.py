import numpy as np
from state import State

def getItemFromList(arr, puzzle):
    for a in arr:
        if (a.puzzle == puzzle).all():
            return a

class Astar:
    openList = []
    closedList = []

    def __init__(self, initial, puzzleNumber, h_type):
        self.puzzleNumber = puzzleNumber
        self.h_type = h_type

        # intitalize lists
        np.array(self.openList, dtype=State)
        np.array(self.closedList, dtype=State)
        self.goal1 = State(input='1 2 3 4 5 6 7 0', g=0, f=0)
        self.goal2 = State(input='1 3 5 7 2 4 6 0', g=0, f=0)
        
        self.initial = initial
        self.openList.append(self.initial)

        self.start()
       

    def start(self):
        i = 0
        while len(self.openList) > 0:
            print("Epoch :" + str(i))

            currentNode = self.openList[0]
            currentI = 0

            # sort open list
            # self.openList.sort(key=lambda x:x.f)
            # iterate through 
            for index, item in enumerate(self.openList):
                if item.f < currentNode.f:
                    currentNode = item
                    currentI = index
            
            # print('openList')
            # print(self.openList)
            # print('closedList')
            # print(self.closedList)
            # for c in self.closedList:
            #     c.print()

            # get first item
            
            # print('CurrentNode: ')
            # currentNode.print()
            self.openList.pop(currentI)
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

                # g = currentNode.g + distance between child and current
                # g* cost of lowest cost path from start to node n
                child.g = currentNode.g + child.g
                # h = huristic function
                if self.h_type =="h0": child.h = child.h0()
                elif self.h_type =="h1": child.h = child.h1()
                elif self.h_type =="h2": child.h = child.h2()
                # f = g+h
                child.f = child.g + child.h
                # print(child.f)

                # check if child in openList
                if any((x.puzzle == child.puzzle).all() for x in self.openList):
                    # check if child.g is higher then openlist g 
                    # print('Child is in openList')
                    openNode = getItemFromList(self.openList, child.puzzle)
                    if child.g > openNode.g:
                        continue
                
                    # add child to openlist
                self.openList.append(child)

                
                # print(children)
                # break;
                i = i+1
                
                # if i == 10:
                #     break;

    def solutionFile(self):
        print('solution')

    def searchPath(self):
        print('search')





input = '1 0 3 6 5 2 7 4'

puzzle = State(input=input, g=0, f=0)
# print(puzzle.h0())
# puzzle.print()
# puzzle.getMoves()

a = Astar(initial=puzzle, puzzleNumber=0, h_type="h0")