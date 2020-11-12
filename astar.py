import numpy as np
import common 
from state import State

class Astar:
    openList = [] #openList, States to visit
    closedList = [] #closedList, States we already visited
    step = 0 #number of states visited

    def __init__(self, input, puzzleNumber, heuristic="h0"):
        self.puzzleNumber = puzzleNumber #puzzle number used for outputing solution
        self.heuristic = heuristic #used to determine the type heuristic function to use

        # intitalize lists
        np.array(self.openList, dtype=State)
        np.array(self.closedList, dtype=State)
        self.goal1 = State(input='1 2 3 4 5 6 7 0')
        self.goal2 = State(input='1 3 5 7 2 4 6 0')
        
        if heuristic !="":
            state = State(input=input, heuristic=heuristic, goalState1=self.goal1, goalState2=self.goal2)
            self.initialState = state

        self.openList.append(self.initialState)
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
                # child.totalG = currentState.g + child.g #compute g
                if common.stateExists(child, self.openList): # check if child in openList
                    existingState = common.getStateFromList(child, self.openList) 
                    if child.totalG > existingState.totalG: #compare existing state g with child g
                        continue # if child g is bigger then skip loop

                child.f = child.totalG + child.h #compute f

                child.parent = currentState # add the parentState=currentState for the child
                self.openList.append(child) # add childState to openlist

            self.step = self.step+1 #increment step to track iteration
            
            # if self.step == 10:
            #     break;

    def solutionFile(self):
        f= open("output/{num}_astar-{h}_solution.txt".format(num=self.puzzleNumber, h=self.heuristic),"w+")
        solutionPath =[]
        backTrackState = self.closedList[len(self.closedList)-1] # get last state from closed list
        solutionPath.append(backTrackState)
        while (backTrackState.puzzle != self.initialState.puzzle).any():
            backTrackState = backTrackState.parent
            solutionPath.append(backTrackState)

        solutionPath.reverse()

        for i in solutionPath:
            if i.parent is not None:
                s = str(i.parent.g)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            else: 
                s = str(i.g)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            f.write(s+'\n')
        s = str(self.closedList[len(self.closedList)-1].totalG) + " " + str("time here goes")
        f.write(s+'\n')
        f.close()


    def searchFile(self):
        f= open("output/{num}_astar-{h}_search.txt".format(num=self.puzzleNumber, h=self.heuristic),"w+")
        for i in self.closedList:
            s = str(i.f)+" "+str(i.g)+" "+str(i.h)+" "+str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            f.write(s+'\n')
        f.close()

input = '4 2 3 1 5 6 0 7'

a = Astar(input=input, puzzleNumber=0, heuristic="h1")
# a.printClosedList()
a.searchFile()
a.solutionFile()
