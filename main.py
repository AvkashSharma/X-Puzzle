import os
from math import cos
import time as time
import random
import common
from state import State
#from astar import Astar
from gbfs import GBFS

inputPath="randomInput.txt"

def generateRandomPuzzle():
    with open("randomInput.txt", "w") as file:
        for i in range(0, 50):
            print(i)
            r = random.sample(range(8), 8)
            file.write(common.stateToString(r)+"\n")



def runAlgorithm(algo):
    print("~~~~~~~~~~~~~~NEW ALGORITHM CALL~~~~~~~~~~~~~~~~~~~~~~")
    file = open("samplePuzzles.txt","r")

    goalstate1 = "1 2 3 4 5 6 7 0"
    goalstate2 = "1 3 5 7 2 4 6 0"

    averageLengthOfSolution = 0
    averageLengthOfSearch = 0
    averageNumberOfNoSolution = 0
    averageCost = 0
    averageExecutionTime = 0
    counter = 0

    i = 0
    for line in file:
        #input = "4 2 3 1 5 6 7 0"
        #input2 = "1 2 3 4 5 6 7 0"
        #input3 = "1 2 3 4 5 6 0 7"
        print("~~~~~~ Puzzle: " + str(i) + " ~~~~~~~")

        start = 0
        end = 0
        lengthOfSolution = 0
        lengthOfSearch = 0

        if(algo == ufc):
            print("UFC: ")
            # same shit
            break
        if(algo == gbfsH0):
            print("GBFS H0: ")
            start = time.time()
            gbfs = GBFS(num = i, input = line.strip(), heuristic="h0",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2)
            gbfs.startGBFS()
            end = time.time()
            duration = end - start
            lengthOfSolution = gbfs.solutionFile(duration)
            lengthOfSearch = gbfs.searchFile()
            if(gbfs.foundState is not None):
                counter = counter + 1
                averageCost = gbfs.foundState.totalG
        if(algo == gbfsH1):
            print("GBFS H1: ")
            start = time.time()
            gbfs = GBFS(num = i, input = line.strip(), heuristic="h1", openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2)
            gbfs.startGBFS()
            end = time.time()
            duration = end - start
            lengthOfSolution = gbfs.solutionFile(duration)
            lengthOfSearch = gbfs.searchFile()
            if(gbfs.foundState is not None):
                counter = counter + 1
                averageCost = gbfs.foundState.totalG
        if(algo == gbfsH2):
            print("GBFS H2: ")
            start = time.time()
            gbfs = GBFS(num = i, input = line.strip(), heuristic="h2",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2)
            gbfs.startGBFS()
            end = time.time()
            duration = end - start
            lengthOfSolution = gbfs.solutionFile(duration)
            lengthOfSearch = gbfs.searchFile()
            if(gbfs.foundState is not None):
                counter = counter + 1
                averageCost = gbfs.foundState.totalG
        if(algo == astarH0):
            # same shit
            print("ASTAR H0: ")
            break
        if(algo == astarH1):
            print("ASTAR H1: ")
            # same shit
            break
        if(algo == astarH2):
            print("ASTAR H2: ")
            # same shit
            break
        
        averageExecutionTime = averageExecutionTime + duration
        averageLengthOfSearch = averageLengthOfSearch + lengthOfSearch
        if (lengthOfSolution != 0):
            averageLengthOfSolution = averageLengthOfSolution + lengthOfSolution
        else:
            averageNumberOfNoSolution = averageNumberOfNoSolution + 1

        i = i + 1
    print("~~~~~~~~~~~~~~~~~~~~\nTotal of : " + str(i) + " Puzzles\n~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Cost: " + str(averageCost))
    print("Total Execution Time: " + str(averageExecutionTime))
    print("Total Length of Search: " + str(averageLengthOfSearch))
    print("Total Length of Solution: " + str(averageLengthOfSolution))
    print("Total Number of No Solution: " + str(averageNumberOfNoSolution))

    if(i != 0 and counter != 0):
        averageCost = averageCost/counter
        averageExecutionTime = averageExecutionTime/counter
        averageLengthOfSearch = averageLengthOfSearch/i
        averageLengthOfSolution = averageLengthOfSolution/counter
        averageNumberOfNoSolution = averageNumberOfNoSolution/i

    print("~~~~~~~~~~~~~~~~~~~~\nAverage of : " + str(i) + " Puzzles\n~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Average Cost: " + str(averageCost))
    print("Average Execution Time: " + str(averageExecutionTime))
    print("Average Length of Search: " + str(averageLengthOfSearch))
    print("Average Length of Solution: " + str(averageLengthOfSolution))
    print("Average Number of No Solution: " + str(averageNumberOfNoSolution))

    file.close()

ufc = "ufc"
gbfsH0 = "gbfsH0"
gbfsH1 = "gbfsH1"
gbfsH2 = "gbfsH2"
astarH0 = "astarH0"
astarH1 = "astarH1"
astarH2 = "astarH2"

# runAlgorithm(ufc)
# runAlgorithm(gbfsH0)
# runAlgorithm(gbfsH1)
# runAlgorithm(gbfsH2)
# runAlgorithm(astarH0)
# runAlgorithm(astarH1)
# runAlgorithm(astarH2)


generateRandomPuzzle()