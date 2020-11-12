from math import cos
import numpy as np
from state import State
import time as time
import os

class GBFS:
    def __init__(self, num = 0, initialState=None, input="", heuristic="", steps=0, openList = [], closedList = [], goalState1 = None, goalState2 = None, state=None, foundState=None):
        self.num = num
        self.steps = steps
        self.openList = openList
        self.closedList = closedList
        self.foundState = foundState

        if goalState1 is not None:
            self.goalState1 = State(input=goalState1)

        if goalState2 is not None:
            self.goalState2 = State(input=goalState2)

        if input!="" and heuristic !="":
            self.heuristic = heuristic
            self.state = State(input=input, heuristic=heuristic, goalState1=self.goalState1, goalState2=self.goalState2)
            self.initialState = self.state

        self.openList.append(self.state)

    def IsGoalState(self):
        # Is It Goal State
        if (self.state.puzzle == self.goalState1.puzzle).all():
            print('Found Goal 1')
            return True
        elif (self.state.puzzle == self.goalState2.puzzle).all():
            print('Found Goal 2')
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

        #print("Closed List: ~~~~~~~~~~~~~~~~~~~~~~~")
        #for cState in self.closedList:
            #cState.print()

        #print("Open List: ~~~~~~~~~~~~~~~~~~~~~~~")
        #for oState in self.openList:
            #oState.print()

        return self.openList[0]

    def startGBFS(self):
        while(True):
            self.steps = self.steps + 1
            #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nIteration: " + str(self.steps))
            #print("Visited State: ~~~~~~~~~~~~~~~~~~~~~~~")
            #self.state.print()
            self.closedList.append(self.state)
            self.openList.remove(self.state)
            if(self.IsGoalState()):
                self.foundState = self.state
                break
            self.state = self.getNextState()
            # putting a temporary break to prevent long results for now
            if(self.steps == 100):
                break

    def solutionFile(self, timeDuration):
        f= open("output/{num}_gbfs-{h}_solution.txt".format(num=self.num, h=self.heuristic),"w+")
        totalLengthOfSolution = 0
        if (self.foundState is not None):
            solutionPath = []
            currentStateOfSolutionPath = self.foundState
            solutionPath.append(currentStateOfSolutionPath)
            
            while (((currentStateOfSolutionPath.puzzle) != (self.initialState.puzzle)).any() and currentStateOfSolutionPath.parent is not None):
                currentStateOfSolutionPath = currentStateOfSolutionPath.parent
                solutionPath.append(currentStateOfSolutionPath)
                
            solutionPath.reverse()
            for i in range(0,len(solutionPath)):
                s = str(solutionPath[i].tileToMove) + " " + str(solutionPath[i].g) + " " + str(solutionPath[i].puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
                f.write(s+'\n')
            s = str(self.foundState.totalG) + " " + str(timeDuration)
            f.write(s+'\n')
            print('Found Solution')
            totalLengthOfSolution = len(solutionPath)
        else:
            f.write("No Solution")
            print("No Solution")
        
        f.close()

        return totalLengthOfSolution

    def searchFile(self):
        totalLengthOfSearch = 0
        f= open("output/{num}_gbfs-{h}_search.txt".format(num=self.num, h=self.heuristic),"w+")
        totalLengthOfSearch = len(self.closedList)
        for i in self.closedList:
            s = "0 0 " + str(i.h) + " "+ str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')
            f.write(s+'\n')
        print('Found Search')
        f.close()

        return totalLengthOfSearch

