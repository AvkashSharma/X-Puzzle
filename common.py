
def stateExists(state, list):
    if any((x.puzzle == state.puzzle).all() for x in list):
        return True
    return False

def getStateFromList(state, list):
    i = 0
    for s in list:
        if (state.puzzle == s.puzzle).all():
            return s, i
        i = i+1

def stateToString(state):
    format = str(state).replace('[','').replace(']','').replace('\n','').replace('\'','').replace(',','')
    return format