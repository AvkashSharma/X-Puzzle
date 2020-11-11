
def stateExists(state, list):
    if any((x.puzzle == state.puzzle).all() for x in list):
        return True
    return False

def getStateFromList(state, list):
    for s in list:
        if (s.puzzle == state.puzzle).all():
            return s

def isGoal1(state, goalState):
    if (state.puzzle == goalState.puzzle).all():
        return state
    return None

def isGoal2():
    print()

