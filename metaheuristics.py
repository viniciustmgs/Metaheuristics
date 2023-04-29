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
    
# geração de solução inicial

def generateInitialSolution (domain):
    solution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return solution

# Hill-Climbing

def hillClimbingNoise (solution, domain):
    newSolution = []
    for i in range(2):
        isFinished = False
        noiseRange = math.fabs(solution[i]*0.05)
        #TEM QUE ARRUMAR O RANGE
        while(isFinished == False):
            noise = random.uniform(0, noiseRange)
            modification = random.uniform(-noise, noise)
            if (solution[i] + modification >= domain[0] and solution[i] + modification <= domain[1]):
                newSolution.append(solution[i] + modification)
                isFinished = True
                print("adicionou noise")
    return newSolution

def hillClimbing (function, domain):
    solution = generateInitialSolution(domain)
    result = function.calculate(solution[0], solution[1])
    print("X: ", solution[0], "Y: ", solution[1])
    print("inicial: ", result)
    limitCounter = 0
    while(limitCounter < 30):
        modifiedSolution = hillClimbingNoise(solution, domain)
        modifiedResult = function.calculate(modifiedSolution[0], modifiedSolution[1])
        print("X: ", modifiedSolution[0], "Y: ", modifiedSolution[1])
        print("modificado: ", modifiedResult)
        if (modifiedResult < result):
            result = modifiedResult
            limitCounter = 0
            print("alterou")
        else:
            limitCounter += 1
            print("não melhorou", limitCounter)
    return result        

# ILS

def iteratedLocalSearch(function, domain):
    initialSolution = generateInitialSolution(domain)
    #faz um hill climbing na solução inicial

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
            executionHillClimbing.append(j)
            executionILS.append(j)
        else:
            # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
            # para a função 2
            executionHillClimbing.append(j)
            executionILS.append(j)
    resultsHillClimbing.append(executionHillClimbing)
    resultsILS.append(executionILS)

# valores finais serão salvos em vetores, no final exibir o resultado final e plotar em boxplot
#print(resultsHillClimbing)
#print(resultsILS)
print(hillClimbing(function1, domains[0]))