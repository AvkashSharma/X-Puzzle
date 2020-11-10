from math import cos
import numpy as np
from state import State

class GBFS:
    def __init__(self, input="", heuristic="", steps=0, openList = [], closedList = [], goalState1 = None, goalState2 = None):
        self.steps = steps
        self.openList = openList
        self.closedList = closedList

        if goalState1 is not None:
            self.goalState1 = State(input=goalState1)

        if goalState2 is not None:
            self.goalState2 = State(input=goalState2)

        if input!="" and heuristic !="":
            self.state = State(input=input, heuristic=heuristic, goalState1=self.goalState1, goalState2=self.goalState2)
        
        self.openList.append(self.state)

    def IsGoalState(self):
        # Is It Goal State
        if (self.state.puzzle == self.goalState1.puzzle).all():
            print('goal1 found')
            return True
        elif (self.state.puzzle == self.goalState2.puzzle).all():
            print('goal2 found')
            return True

        return False

    def stateExists(self, stateToCheck, listToCheck):
        for st in listToCheck:
            if (st.puzzle == stateToCheck.puzzle).all():
                return True
        return False

    def getNextState(self):
        
        nextStates = self.state.getMoves()
        
        for nState in  nextStates:
            if (not(self.stateExists(nState, self.closedList)) and not(self.stateExists(nState, self.openList))):
                self.openList.append(nState)
            
        self.openList = sorted(self.openList, key=lambda x: x.h, reverse=False)

        print("Closed List: ~~~~~~~~~~~~~~~~~~~~~~~")
        for cState in self.closedList:
            cState.print()

        print("Open List: ~~~~~~~~~~~~~~~~~~~~~~~")
        for oState in self.openList:
            oState.print()

        return self.openList[0]

    def startGBFS(self):
        while(True):
            self.steps = self.steps + 1
            print("Iteration: " + str(self.steps))
            print("Visited State: ~~~~~~~~~~~~~~~~~~~~~~~")
            self.state.print()
            self.closedList.append(self.state)
            self.openList.remove(self.state)
            if(self.IsGoalState()):
                break
            self.state = self.getNextState()
            # putting a temporary break to prevent long results for now
            if(self.steps == 10):
                break


# Visited State
input = "4 2 3 1 5 6 7 0"
input2 = "1 2 3 4 5 6 7 0"
input3 = "1 2 3 4 5 6 0 7"

goalstate1 = "1 2 3 4 5 6 7 0"

goalstate2 = "1 3 5 7 2 4 6 0"

gbfs = GBFS(input = input, heuristic="h2", goalState1=goalstate1, goalState2=goalstate2)

gbfs.startGBFS()
