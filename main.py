import random
import matplotlib as plt
from functions import Function1, Function2   
from hillClimbing import hillClimbing
from iteratedLocalSearch import iteratedLocalSearch

# iniciando a execução das meta-heurísticas em um loop, cada uma das 2 é executada
# 30 vezes para cada um dos domínios 
# gerador de solução inicial

def generateInitialSolution (domain):
    solution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return solution

def main():
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
                executionHillClimbing.append(hillClimbing(function1, domains[i], 1000, initialSolution))
                executionILS.append(j)
            else:
                # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
                # para a função 2
                
                initialSolution = generateInitialSolution(domains[i])
                executionHillClimbing.append(hillClimbing(function2, domains[i], 1000, initialSolution))
                executionILS.append(j)
        #resultsHillClimbing.append(executionHillClimbing)
        #resultsILS.append(executionILS)

    # valores finais salvos em vetores, agora os resultados são impressos, e umboxplot é feito

    print(iteratedLocalSearch(function2, domains[3], generateInitialSolution(domains[3])))

main()