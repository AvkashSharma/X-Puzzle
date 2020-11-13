import os
from math import cos
import time as time
import random
import common
from state import State
from astar import Astar
from gbfs import GBFS

# inputPath="randomInput.txt"
inputPath="samplePuzzles.txt"

def generateRandomPuzzle():
    with open("randomInput.txt", "w") as file:
        for i in range(0, 50):
            print(i)
            r = random.sample(range(8), 8)
            file.write(common.stateToString(r)+"\n")


def analysis():
    aFile = open("analysis.csv","w+")
    aFile.write("algo, totLengthOfSolution, avgLenghtOfSolution, totNoSolution, avgNoSolution, totExec, avgExec, optimality")
    file = open(inputPath,"r")
    pNum = 0
    for line in file:
        algoAnalysis(Astar(puzzleNumber=pNum, input=line, heuristic="h1"))
        
    aFile.close()


def algoAnalysis(algorithm):
    start = time.time()
    algo = algorithm
    algo.start()
    end = time.time()
    duration = end-start
    heuristic = algorithm.heuristic
    lenOfSolution = algo.solutionFile(duration)
    lenOfSearch = algo.searchFile()
    noSolution = 1
    cost = 0
    if algo.foundState is not None:
        noSolution = 0
        cost = algo.foundState.totalG

    return heuristic, lenOfSolution, lenOfSearch, noSolution, cost, duration


def runAlgorithm(algo):
    file = open(inputPath,"r")
    afile = open("analysis.csv","a")
    afile.write("\nAlgorithm, Puzzle, Cost, Length Of Solution, Length Of Search, Execution, No Solution, Optimality\n")

    goalstate1 = "1 2 3 4 5 6 7 0"
    goalstate2 = "1 3 5 7 2 4 6 0"

    totalLengthOfSolution = 0
    totalLengthOfSearch = 0
    totalNoSolution = 0
    totalCost = 0
    totalExecutionTime = 0
    counter = 0

    averageCost = averageExecutionTime = averageLengthOfSearch = averageLengthOfSolution = averageNoSolution = 0

    i = 0
    for line in file:
        lengthOfSolution = 0
        lengthOfSearch = 0
        duration = 0
        analysis = None

        # if algo == ufc:
        #     analysis = algoAnalysis(GBFS(num = i, input = line.strip(), heuristic="h0",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2))
        #     break;

        if algo == gbfsH0:
            analysis = algoAnalysis(GBFS(num = i, input = line.strip(), heuristic="h0",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2))
        
        if algo == gbfsH1:
            analysis = algoAnalysis(GBFS(num = i, input = line.strip(), heuristic="h1",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2))

        if algo == gbfsH2:
            analysis = algoAnalysis(GBFS(num = i, input = line.strip(), heuristic="h2",  openList = [], closedList = [], goalState1=goalstate1, goalState2=goalstate2))

        if algo == astarH0:
            analysis = algoAnalysis(Astar(puzzleNumber = i, input = line.strip(), heuristic="h0"))
        
        if algo == astarH1:
            analysis = algoAnalysis(Astar(puzzleNumber = i, input = line.strip(), heuristic="h1"))
        
        if algo == astarH2:
            analysis = algoAnalysis(Astar(puzzleNumber = i, input = line.strip(), heuristic="h2"))

        duration = analysis[5]
        lengthOfSolution = analysis[1]
        lengthOfSearch = analysis[2]
        
        if analysis[3] == 0:
            totalCost = analysis[4]
            counter = counter + 1
        
        totalExecutionTime = totalExecutionTime + duration
        totalLengthOfSearch = totalLengthOfSearch + lengthOfSearch
        if lengthOfSolution != 0:
            totalLengthOfSolution = totalLengthOfSolution + lengthOfSolution
        else:
            totalNoSolution = totalNoSolution + 1

        afile.write(algo +", "+ str(i)+", "+str(totalCost)+", "+str(lengthOfSolution)+", "+str(lengthOfSearch)+", "+str(duration)+","+str(analysis[3])+",,"+line.strip()+"\n")
        i = i + 1
       
    afile.write("Total-"+algo+","+str(i)+" , "+str(totalLengthOfSolution)+", "+str(totalLengthOfSearch)+", "+str(totalExecutionTime)+","+str(totalNoSolution)+"\n")

    if(i != 0 and counter != 0):
        averageCost = totalCost/counter
        averageExecutionTime = totalExecutionTime/counter
        averageLengthOfSearch = totalLengthOfSearch/i
        averageLengthOfSolution = totalLengthOfSolution/counter
        averageNoSolution = totalNoSolution/i

    afile.write("Average-"+algo+", , "+str(averageCost)+","+str(averageLengthOfSolution)+", "+str(averageLengthOfSearch)+", "+str(averageExecutionTime)+","+str(averageNoSolution)+"\n")

    file.close()

ufc = "ufc"
gbfsH0 = "gbfsH0"
gbfsH1 = "gbfsH1"
gbfsH2 = "gbfsH2"
astarH0 = "astarH0"
astarH1 = "astarH1"
astarH2 = "astarH2"

# runAlgorithm(ufc)
runAlgorithm(gbfsH0)
runAlgorithm(gbfsH1)
runAlgorithm(gbfsH2)
runAlgorithm(astarH0)
runAlgorithm(astarH1)
runAlgorithm(astarH2)
