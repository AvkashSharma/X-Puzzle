from math import cos
import numpy as np
from state import State

class GBFS:
    def __init__(self, input="", puzzle=None, f=0, h=0, g=0):
        self.row = 2
        self.col = 4
        self.f = f
        self.h = h
        self.g = g

        if input!="":
            inputList = input.split(" ")
            npMatrix = np.split(np.array(inputList), self.row)
            self.puzzle = np.vstack(npMatrix)
        
        if puzzle is not None:
            self.puzzle = puzzle



# Visited State
input = "4 2 3 1 5 6 7 0"
input2 = "1 2 3 4 5 6 7 0"
input3 = "1 2 3 4 5 6 0 7"

state = State(input=input, heuristic="h2")


goalState1 = State(input='1 2 3 4 5 6 7 0')
goalState2 = State(input='1 3 5 7 2 4 6 0')

def IsGoalState(state):
    # Is It Goal State
    if (state.puzzle == goalState1.puzzle).all():
        print('goal1 found')
        return True
    elif (state.puzzle == goalState2.puzzle).all():
        print('goal2 found')
        return True

    return False

openList = []
openList.append(state)

closedList = []

def stateExists(stateToCheck, listToCheck):
    for st in listToCheck:
        if (st.puzzle == stateToCheck.puzzle).all():
            return True
    return False

def nextStep(openList):
    
    nextStates = state.getMoves()
    print("Closed List: ~~~~~~~~~~~~~~~~~~~~~~~")
    for nState in  nextStates:
        #print(nState.puzzle)
        #print("G(N): "+ str(nState.g))
        #print("H(N): "+ str(nState.h))
        if not((stateExists(nState, closedList)) and not(stateExists(nState, openList))):
            openList.append(nState)
        
    openList = sorted(openList, key=lambda x: x.h, reverse=False)

    for cState in closedList:
        cState.print()

    print("Open List: ~~~~~~~~~~~~~~~~~~~~~~~")

    for oState in openList:
        oState.print()


    return openList[0]

counter = 0

while(True):
    counter = counter + 1
    print("Iteration: ")
    print(counter)
    print("Visited State: ~~~~~~~~~~~~~~~~~~~~~~~")
    state.print()
    closedList.append(state)
    openList.remove(state)
    if(IsGoalState(state)):
        break
    state = nextStep(openList)
    

    
    if(counter == 10):
        break

    
    






