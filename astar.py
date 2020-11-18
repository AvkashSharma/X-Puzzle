import numpy as np
import common 
from state import State
import time

class Astar:
    step = 0 #number of states visited
    foundState = None
    def __init__(self, input, puzzleNumber, heuristic="h0", goalState1 = None, goalState2 = None, monotonic=False):
        self.puzzleNumber = puzzleNumber #puzzle number used for outputing solution
        self.heuristic = heuristic #used to determine the type heuristic function to use
        self.monotonic = monotonic #used to determine wheather to iterate in the closed list
        # intitalize lists
        self.openList = [] #openList, States to visit
        self.closedList = [] #closedList, States we already visited
        if goalState1 is not None:
            self.goal1 = State(input=goalState1)

        if goalState2 is not None:
            self.goal2 = State(input=goalState2)

        # self.goal1 = State(input='1 2 3 4 5 6 7 0')
        # self.goal2 = State(input='1 3 5 7 2 4 6 0')
        
        if heuristic !="":
            state = State(input=input, heuristic=heuristic, goalState1=self.goal1, goalState2=self.goal2)
            self.initialState = state

        self.openList.append(self.initialState)

        
    def start(self):
        startTime = time.time()
        while len(self.openList) > 0:
            self.openList = sorted(self.openList, key=lambda x:x.f, reverse=False)  # sort openList sort by f'
            currentState = self.openList[0]     # get state with smallest f from openlist
            currentState.f = currentState.totalG + currentState.h
            
            self.openList.remove(currentState)  # remove currentState from openList
            self.closedList.append(currentState);# add currentState to closedList
            
            if (currentState.puzzle == self.goal1.puzzle).all():
                print('Astar - goal1 found');
                self.foundState = currentState
                break;

            elif (currentState.puzzle == self.goal2.puzzle).all():
                print('Astar - goal2 found');
                self.foundState = currentState
                break;

            #get all possible states for currentState
            # check if states are in open or closed list
            for child in currentState.getMoves() :
                child.parent = currentState
                child.f = child.totalG + child.h    #compute f
                if common.stateExists(child, self.closedList) and not self.monotonic:
                    inClosed = common.getStateFromList(child, self.closedList)
                    inClosedState = inClosed[0]
                    inClosedIndex  = inClosed[1]
                    if inClosedState.f > child.f:
                        self.closedList.pop(inClosedIndex)
                        self.openList.append(child)
                    else:
                        continue

                elif common.stateExists(child, self.openList):
                    inOpen = common.getStateFromList(child, self.openList)
                    inOpenState = inOpen[0]
                    inOpenIndex = inOpen[1]
                    if inOpenState.f > child.f:
                        self.openList[inOpenIndex] = child
                    else: continue

                else:
                    self.openList.append(child) # add childState to openlist

            self.step = self.step+1 #increment step to track iteration
            
            if time.time() > startTime+ 60: # stop after 60
                break;
            # if(self.step == 100):
            #     break

    def solutionFile(self, duration):
        f= open("output/{num}_astar-{h}_solution.txt".format(num=self.puzzleNumber, h=self.heuristic),"w+")
        lengthOfSolution = 0
        if self.foundState is not None:
            solutionPath=[]
            backTrackState = self.foundState # get last state from closed list
            solutionPath.append(backTrackState)
            
            while (backTrackState.puzzle != self.initialState.puzzle).any() and backTrackState.parent is not None:
                backTrackState = backTrackState.parent
                solutionPath.append(backTrackState)

            solutionPath.reverse()
            for i in solutionPath:
                f.write(str(i.tileToMove)+" "+ str(i.totalG) +" "+common.stateToString(i.puzzle)+"\n")

            f.write(str(self.closedList[len(self.closedList)-1].totalG) + " " + str(duration)+"\n")
            lengthOfSolution = len(solutionPath)
        else:
            f.write("No Solution")
        f.close()

        return lengthOfSolution


    def searchFile(self):
        f= open("output/{num}_astar-{h}_search.txt".format(num=self.puzzleNumber, h=self.heuristic),"w+")
        for i in self.closedList:
            f.write(str(i.f)+" "+str(i.totalG)+" "+str(i.h)+" "+common.stateToString(i.puzzle)+'\n')
        f.close()
        return len(self.closedList)

