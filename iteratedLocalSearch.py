import random
import math
from hillClimbing import  hillClimbing

def acceptanceCriteria(function, solution, modifiedSolution, memory):
    bestResult = function.calculate(memory[0][0], memory[0][1])
    solutionResult = function.calculate(solution[0], solution[1])
    modifiedResult = function.calculate(modifiedSolution[0], modifiedSolution[1])
    if(int(solutionResult) == int(modifiedResult)):
        memory[2] += 1
        return memory
    else:
        if(modifiedResult < solutionResult):
            memory[1] = modifiedSolution
            memory[2] += 1
            if(modifiedResult < bestResult):
                memory[0] = modifiedSolution
                memory[2] = 0
            return memory
        else:
            memory[1] = modifiedSolution
            memory[2] += 1
            return memory

def iteratedLocalSearchNoise(solution, domain):
    newSolution = []
    domainSize = math.fabs(domain[1]-domain[0])
    noiseRange = [domainSize*0.07, domainSize*0.2]
    for i in range(2):
        isFinished = False
        while(isFinished == False):
            noise = random.uniform(noiseRange[0], noiseRange[1])
            modification = noise if random.choice([0, 1]) == 0 else -noise
            if (solution[i] + modification >= domain[0] and solution[i] + modification <= domain[1]):
                newSolution.append(solution[i] + modification)
                isFinished = True
    return newSolution            

def iteratedLocalSearch(function, domain, initialSolution):
    solution = hillClimbing(function, domain, 100, initialSolution)[0]
    stopCondition = 0
    memory = [solution, solution, stopCondition]
    while(memory[2] < 10000):
        modifiedSolution = iteratedLocalSearchNoise(solution, domain)
        optModifiedSolution = hillClimbing(function, domain, 100, modifiedSolution)[0]
        memory = acceptanceCriteria(function, solution, optModifiedSolution, memory)
        solution = memory[1]
    solution = hillClimbing(function, domain, 100000, memory[0])[0]    
    result = function.calculate(solution[0], solution[1])
    return [solution, result]    