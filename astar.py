import numpy as np
from numpy.lib import utils
from numpy.lib.type_check import common_type
import common 
from state import State



class Astar:
    openList = [] #openList, States to visit
    closedList = [] #closedList, States we already visited
    step = 0 #number of states visited

    def __init__(self, initialState, puzzleNumber, h_type):
        self.puzzleNumber = puzzleNumber #puzzle number used for outputing solution
        self.h_type = h_type #used to determine the type heuristic function to use

        # intitalize lists
        np.array(self.openList, dtype=State)
        np.array(self.closedList, dtype=State)
        self.goal1 = State(input='1 2 3 4 5 6 7 0', g=0, f=0)
        self.goal2 = State(input='1 3 5 7 2 4 6 0', g=0, f=0)
        
        self.initial = initialState
        self.openList.append(self.initial)

        self.start()
    
    def start(self):
        while len(self.openList) > 0:
            print("Steps:" + str(self.step)) #print iteration number
             
            self.openList = sorted(self.openList, key=lambda x:x.f, reverse=False)  # sort openList sort by f'
            print("Closed List: ~~~~~~~~~~~~~~~~~~~~~~~")
            for cState in self.closedList:
                cState.print()

            print("Open List: ~~~~~~~~~~~~~~~~~~~~~~~")
            for oState in self.openList:
                oState.print()
            
            currentState = self.openList[0]     # get state with smallest f from openlist
            self.openList.remove(currentState)  # remove currentState from openList
            self.closedList.append(currentState);# add currentState to closedList

            # compare with goals
            if (currentState.puzzle == self.goal1.puzzle).all():
                print('goal1 found');
                break;

            elif (currentState.puzzle == self.goal2.puzzle).all():
                print('goal2 found');
                break;

            children = currentState.getMoves() #get all possible states for currentState
            # check if states are in open or closed list
            for child in children:
                if common.stateExists(child, self.closedList): # check if child in closedList
                    continue     # if exist skip the rest of the loop

                # g = currentNode.g + distance between child and current
                # g* cost of lowest cost path from start to node n
                child.g = currentState.g + child.g #compute g

                if common.stateExists(child, self.openList): # check if child in openList
                    existingState = common.getStateFromList(self.openList, child) 
                    if child.g > existingState.g: #compare existing state g with child g
                        continue # if child g is bigger then skip loop

                if self.h_type =="h0": child.h = child.h0()
                elif self.h_type =="h1": child.h = child.h1()
                elif self.h_type =="h2": child.h = child.h2() #compute h
                child.f = child.g + child.h #compute f


                child.parent = currentState # add the parentState=currentState for the child
                self.openList.append(child) # add childState to openlist

            self.step = self.step+1 #increment step to track iteration
            
                # if self.step == 10:
                #     break;

    def printClosedList(self):
        for i in self.closedList:
            print("\n\n")
            i.print()
            if i.parent is not None:
                print("parent: ")
                i.parent.print()

    def solutionFile(self):
        f= open("output/{num}_astar-{h}_solution.txt".format(num=self.puzzleNumber, h=self.h_type),"w+")
        for i in self.closedList:
            if i.parent is not None:
                s = str(i.g -i.parent.g)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            else: 
                s = str(i.g)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            f.write(s+'\n')
        print('solution')
        f.close()

    def searchFile(self):
        f= open("output/{num}_astar-{h}_search.txt".format(num=self.puzzleNumber, h=self.h_type),"w+")
        for i in self.closedList:
            s = str(i.f)+" "+str(i.g)+" "+str(i.h)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            f.write(s+'\n')
        print('search')
        f.close()





input = '1 2 0 3 5 6 7 4'

puzzle1 = State(input=input, g=0, f=0)
puzzle2 = State(input=input, g=0, f=6)
puzzle3 = State(input=input, g=0, f=3)


# l=[]
# l.append(puzzle1)
# l.append(puzzle2)
# l.append(puzzle3)
# for i in l:
#     print(i.f)

# l  = sorted(l, key=lambda x:x.f, reverse=False)

# for i in l:
#     print(i.f)

# l.pop()
# print("..........")

# for i in l:
#     print(i.f)


# e = any((x.f == 3) for x in l)
# print(e)
a = Astar(initialState=puzzle1, puzzleNumber=0, h_type="h0")
a.printClosedList()
a.searchFile()
a.solutionFile()

# a = '1 2 0 3 5 6 7 4'
# p = State(input=a, g=0, f=0)
# p.print()
# m = p.getMoves()
# for mi in m:
#     mi.print()
