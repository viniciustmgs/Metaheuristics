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
    initialSolution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return initialSolution

# Hill-Climbing

def hillClimbing (function, domain):
    initialSolution = generateInitialSolution(domain)
    
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
print(resultsHillClimbing)
print(resultsILS)