
# puzzle dimension must be scalable

# state = seqence of number (ex: 3, 0, 1, 4, 2, 6, 5, 7)
from ast import NodeTransformer


3 0 1 4 2 6 5 7

2x4 = 8 in total
1x4


4x4
# look posibilities(pass the state)
# use numpy matrix to represnt state

#   find zero
#       isCorner?
#           [rXc] = [2x4]
#           [0,0] is corner
#           [r-1, 0] is corner [1, 0]
#           [0, c-1] is corner [0,3]
#           [r-1,c-1] is corner [1, 3]

find position of 0 -> [0,1]
GetPosiblities(p):
    is p isCorner? False
    is p isFirstColumm? False
    Is p isLastColumn? False
    Is p isFirstRow? True
    is p isLastRow? false
    else isMiddle?

# a function where you pass the whole list[0 3 1 4 2 6 5 7] 
    # return of possible list[]


[3 0 1 4] = [0,0] [0,1] [0,2] [0,3]
[2 6 5 7] = [1,0] [1,1] [1,2] [1,3]

Open: [3 0 1 4 2 6 5 7][][]
Close:

Open: [0 3 1 4 2 6 5 7] [3 6 1 4 2 0 5 7] [3 1 0 4 2 6 5 7]
Close: [3 0 1 4 2 6 5 7]



#       Is first row?
#       Is last row?
#       IS first coloumn?
#       is last column?
#       rest is all normal moves 
      
#       yes: all wrap
#       Check position and get posibile moves


# 2.4 Analysis




# goal function

# board states

# moves

# positions

# search functions

# input output

# node
# parent node
# puzzle
# cost
# f(n)
# h(n)



# star