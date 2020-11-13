import numpy as np
from state import State


class UniformCostSearch:

  def __init__(self, puzzleNumber, initial, goal_state1, goal_state2):
    self.puzzle_number = puzzleNumber 
    self.input_state = State(initial, g = 0)
    self.open_list = []
    self.closed_list = []
    self.goal1 = State(input = goal_state1, g = 0)
    self.goal2 = State(input = goal_state2, g = 0)
    self.step_count = 0
    self.open_list.append(self.input_state)
    self.foundState = None
    
    


  def isGoalState(self, state):
    if (state.puzzle == self.goal1.puzzle).all():
      print('Goal1 Found')
      self.foundState = state
      print(self.foundState.puzzle)
      return True
    if (state.puzzle == self.goal2.puzzle).all():
      print('Goal2 Found')
      self.foundState = state
      print(self.foundState.puzzle)
      return True
    return False

  def getLowestCostState(self):
    self.open_list = sorted(self.open_list, key=lambda x: x.totalG, reverse=False)
    return self.open_list.pop(0)
  

  def stateExists(self, stateToCheck, listToCheck):
    for st in listToCheck:
      if (st.puzzle == stateToCheck.puzzle).all():
        return True
    return False


  def updateIfLowerCost(self,stateToCheck):
    for state in self.open_list:
      if ((state.puzzle == stateToCheck.puzzle).all() and (state.totalG > stateToCheck.totalG)):
        state = stateToCheck

  
  def solve(self):
    while True:
      self.step_count += 1
      #print("Iteration: " + str(self.step_count))

      # if open list is empty -> break
      if not self.open_list:
        print("Failure")
        break
      
      # choose the lowest cost state from the open list
      current_state = self.getLowestCostState()
      # current_state.print()
      
      self.closed_list.append(current_state)
    

      # check if current_state is goal_state
      if self.isGoalState(current_state):
        
        break
      
      next_states = current_state.getMoves()
      # print("curr " + str(current_state.g))

      for state in next_states:
        if not(self.stateExists(state, self.closed_list)) and not(self.stateExists(state, self.open_list)):
          self.open_list.append(state)
        elif not (self.stateExists(state, self.closed_list)) and (self.stateExists(state, self.open_list)):
          self.updateIfLowerCost(state)

      
      if(self.step_count == 100):
        break 
    


  def get_solution_path(self):
    path =[]
    state = self.foundState
    while self.input_state.puzzle.all  != state.puzzle.all:
      path.append(state)
      state = state.parent
    path.append(self.input_state)
    return path
  
  
  def solution_file(self, execution_time):
    f = open("output/{puzzle_number}_ucs_solution.txt".format(puzzle_number=self.puzzle_number), "w+")
    
    if(self.foundState is not None):
      solution_path = self.get_solution_path()   
      solution_path.reverse()
      
      for i in range(0,len(solution_path)):
        s = str(solution_path[i].tileToMove) + " " + str(solution_path[i].g) + " " + str(solution_path[i].puzzle).replace('[','').replace(']','').replace('\n','').replace('\'','')   
        f.write(s+ '\n')
    
      s = str(self.foundState.totalG) + " " + str(execution_time)
      f.write(s+'\n')
      return len(solution_path)
    else:
      f.write("no Solution")
      print("No Solution was Found")
      return 0

    f.close()
    


  def search_file(self):
    f = open("output/{puzzle_number}_ucs_search.txt".format(puzzle_number=self.puzzle_number), "w+")
    for i in self.closed_list:
      s = str(0)+ " "+ str(i.g)+ " "+ str(0)+ " " +str(i.puzzle).replace('[','').replace(']','').replace('\n','').replace("'",'')
      f.write(s+'\n')
    # print('Search')
    f.close()
    length_of_closed_list = len(self.closed_list)
    return length_of_closed_list






#input = "4 2 3 1 5 6 7 0"

#goalstate1 = "1 2 3 4 5 6 7 0"
#goalstate2 = "1 3 5 7 2 4 6 0"

#ucs = UniformCostSearch(input,goalstate1,goalstate2,puzzleNumber = 0)
#ucs.search_file()
#ucs.solution_file()
