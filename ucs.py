import numpy as np
from state import State


class UniformCostSearch:

  def __init__(self, initial, goal_state1, goal_state2):
    self.input_state = State(initial, g = 0)
    self.open_list = []
    self.closed_list = []
    self.goal1 = State(goal_state1, g = 0)
    self.goal2 = State(goal_state2, g = 0)
    self.step_count = 0
    self.open_list.append(self.input_state)
    self.solve()


  def isGoalState(self, state):
    if (state.puzzle == self.goal1.puzzle).all():
      print('goal1 found')
      return True
    if (state.puzzle == self.goal2.puzzle).all():
      print('goal2 found')
      return True
    return False

  def getLowestCostState(self):
    self.open_list = sorted(self.open_list, key=lambda x: x.g, reverse=False)

    print("Open List: ~~~~~~~~~~~~~~~~~~~~~~~")
    for o_list in self.open_list:
      o_list.print()
    return self.open_list.pop(0)
  

  def stateExists(self, stateToCheck, listToCheck):
    for st in listToCheck:
      if (st.puzzle == stateToCheck.puzzle).all():
        return True
    return False


  def updateIfLowerCost(self,stateToCheck):
    print('lower ')
    for st in self.open_list:
      if ((st.puzzle == stateToCheck.puzzle).all() and (st.g > stateToCheck.g).all()):
        self.open_list.g = stateToCheck.g

  
  def solve(self):
    while True:
      self.step_count += 1
      print("Iteration: " + str(self.step_count))

      # if open list is empty -> break
      if not self.open_list:
        print("Failure")
        break
      
      # choose the lowest cost state from the open list
      current_state = self.getLowestCostState()
      print("Visited State: ~~~~~~~~~~~~~~~~~~~~~~~")
      current_state.print()
      
      self.closed_list.append(current_state)
      print("Closed State: ~~~~~~~~~~~~~~~~~~~~~~~")
      for cl_item in self.closed_list:
        cl_item.print()

      # check if current_state is goal_state
      if self.isGoalState(current_state):
        break
      
      next_states = current_state.getMoves()
      # print("curr " + str(current_state.g))

      for state in next_states:
        #print("before")
        #print(state.g)
        state.g = current_state.g + state.g
        #print("after")
        #print(state.g)

        if not((self.stateExists(state, self.closed_list)) and not(self.stateExists(state, self.open_list))):
          self.open_list.append(state)
        elif not(self.stateExists(state, self.closed_list)) and self.stateExists(state, self.open_list):
          self.updateIfLowerCost(state)

      
      if(self.step_count == 10):
        break 
    


    




      




input = "4 2 3 1 5 6 7 0"

goalstate1 = "1 2 3 4 5 6 7 0"
goalstate2 = "1 3 5 7 2 4 6 0"

ucs = UniformCostSearch(input,goalstate1,goalstate2)
