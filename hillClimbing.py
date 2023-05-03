import random
import math

# Hill-Climbing

def hillClimbingNoise (solution, domain):
    newSolution = []
    noise = math.fabs((domain[1]-domain[0])*0.01)
    for i in range(2):
        isFinished = False
        while(isFinished == False):
            modification = random.uniform(-noise, noise)
            if (solution[i] + modification >= domain[0] and solution[i] + modification <= domain[1]):
                newSolution.append(solution[i] + modification)
                isFinished = True
    return newSolution

def hillClimbing (function, domain, stopCondition, initialSolution):
    solution = initialSolution
    result = function.calculate(initialSolution[0], initialSolution[1])
    limitCounter = 0
    while(limitCounter < stopCondition):
        modifiedSolution = hillClimbingNoise(solution, domain)
        modifiedResult = function.calculate(modifiedSolution[0], modifiedSolution[1])
        if (modifiedResult < result):
            solution = modifiedSolution
            result = modifiedResult
            limitCounter = 0
        else:
            limitCounter += 1
    return [solution, result]       
