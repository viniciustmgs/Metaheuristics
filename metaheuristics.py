import random
import math

# criando a classe de cada F.O.

class Function1:
    def __init__(self) -> None:
        pass

    def calculate(x, y):
        result = x**2+y**2+25*((math.sin(x))**2+(math.sin(y))**2)
        return result


class Function2:
    def __init__(self) -> None:
        pass

    def calculate(x, y):
        result = -(y+47)*math.sin(math.sqrt(math.fabs(y+0.5*y+47))) - x*math.sin(math.sqrt(math.fabs(x-(y+47))))
        return result
    
# gerador de solução inicial

def generateInitialSolution (domain):
    solution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return solution

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

# ILS

def acceptanceCriteria(function, solution, modifiedSolution, memory):
    bestResult = function.calculate(memory[0][0], memory[0][1])
    solutionResult = function.calculate(solution[0], solution[1])
    modifiedResult = function.calculate(modifiedSolution[0], modifiedSolution[1])
    if(int(solutionResult) == int(modifiedResult)):
        memory[2] += 1
        print("não melhorou!")
        return memory
    else:
        if(modifiedResult < solutionResult):
            memory[1] = modifiedSolution
            memory[2] += 1
            print("solução atual melhor que anterior")
            if(modifiedResult < bestResult):
                memory[0] = modifiedSolution
                memory[2] = 0
                print("solução atual é melhor de todas!")
            return memory
        else:
            memory[1] = modifiedSolution
            memory[2] += 1
            print("solução atual não é melhor")
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

def iteratedLocalSearch(function, domain):
    initialSolution = generateInitialSolution(domain)
    solution = hillClimbing(function, domain, 100, initialSolution)[0]
    stopCondition = 0
    memory = [solution, solution, stopCondition]
    print("solução inicial: ", function.calculate(solution[0], solution[1]))
    print("\ncondiçãode parada: ", stopCondition, "\nEntrenado no while\n\n")
    while(memory[2] < 10000):
        print("solução atual", function.calculate(solution[0], solution[1]))
        modifiedSolution = iteratedLocalSearchNoise(solution, domain)
        optModifiedSolution = hillClimbing(function, domain, 100, modifiedSolution)[0]
        print("solução modificada: ", function.calculate(optModifiedSolution[0], optModifiedSolution[1]))
        memory = acceptanceCriteria(function, solution, optModifiedSolution, memory)
        solution = memory[1]
        print("condição de parada: ",memory[2])
    solution = memory[0]    
    result = function.calculate(solution[0], solution[1])
    return [solution, result]    

# iniciando a execução das meta-heurísticas em um loop, cada uma das 2 é executada
# 30 vezes para cada um dos domínios 

function1 = Function1
function2 = Function2
domains = [[-5, 5], [-2, 2], [-512, 512], [400, 512]]
resultsILS = []
resultsHillClimbing = []

for i in range(4):
    executionILS = []
    executionHillClimbing = []
    for j in range(30):
        if (i < 2):
            # entra nesse if se for os domínios A e B, portanto executa as meta-heurísticas
            # para a função 1

            initialSolution = generateInitialSolution(domains[i])
            #executionHillClimbing.append(hillClimbing(function1, domains[i], 10000, initialSolution))
            executionILS.append(j)
        else:
            # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
            # para a função 2
            
            initialSolution = generateInitialSolution(domains[i])
            #executionHillClimbing.append(hillClimbing(function2, domains[i], 10000, initialSolution))
            executionILS.append(j)
    #resultsHillClimbing.append(executionHillClimbing)
    #resultsILS.append(executionILS)

# valores finais serão salvos em vetores, no final exibir o resultado final e plotar em boxplot
#print(resultsHillClimbing)
#print(resultsILS)
#print("dominio A:\n", resultsHillClimbing[0])
#print("dominio B:\n", resultsHillClimbing[1])
#print("dominio C:\n", resultsHillClimbing[2])
#print("dominio D:\n", resultsHillClimbing[3])
#iteratedLocalSearch(function1, domains[0])
print(iteratedLocalSearch(function2, domains[3]))