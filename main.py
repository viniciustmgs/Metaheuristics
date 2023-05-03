import random
import matplotlib.pyplot as plt
from functions import Function1, Function2   
from hillClimbing import hillClimbing
from iteratedLocalSearch import iteratedLocalSearch

# iniciando a execução das meta-heurísticas em um loop, cada uma das 2 é executada
# 30 vezes para cada um dos domínios 
# gerador de solução inicial

def generateInitialSolution (domain):
    solution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return solution

def plot(resultsHillClimbing, resultsILS):
    dataHillClimbing = []
    dataIteratedLocalSearch = []
    for x in range(4):
        data1 = []
        data2 = []
        for y in range(30):
            data1.append(resultsHillClimbing[x][y][1])
            data2.append(resultsILS[x][y][1])
        dataHillClimbing.append(data1)
        dataIteratedLocalSearch.append(data2)    
    #print(iteratedLocalSearch(function2, domains[3], generateInitialSolution(domains[3])))
    #fig = plt.figure(figsize =(10, 7))
    fig1 = plt.figure(figsize=(10, 7))
    fig2 = plt.figure(figsize=(10, 7))
    ax1 = fig1.add_axes([0, 0, 1, 1])
    ax2 = fig2.add_axes([0, 0, 1, 1])
    ax1.boxplot(dataHillClimbing)
    ax2.boxplot(dataIteratedLocalSearch)
    plt.show()

def main():
    function1 = Function1
    function2 = Function2
    domains = [[-5, 5], [-2, 2], [-512, 512], [400, 512]]
    resultsILS = []
    resultsHillClimbing = []
    percentage = 0
    for i in range(4):
        executionILS = []
        executionHillClimbing = []
        for j in range(30):
            if (i < 2):
                # entra nesse if se for os domínios A e B, portanto executa as meta-heurísticas
                # para a função 1
                initialSolution = generateInitialSolution(domains[i])
                executionHillClimbing.append(hillClimbing(function1, domains[i], 1000, initialSolution))
                initialSolution = generateInitialSolution(domains[i])
                executionILS.append(iteratedLocalSearch(function1, domains[i], initialSolution))
            else:
                # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
                # para a função 2
                
                initialSolution = generateInitialSolution(domains[i])
                executionHillClimbing.append(hillClimbing(function2, domains[i], 1000, initialSolution))
                initialSolution = generateInitialSolution(domains[i])
                executionILS.append(iteratedLocalSearch(function2, domains[i], initialSolution))
            percentage += 1
            print("{:.2f}".format((percentage/120)*100), "%", end="\r")    
        resultsHillClimbing.append(executionHillClimbing)
        resultsILS.append(executionILS)

    # valores finais salvos em vetores, agora os resultados são impressos, e um boxplot é feito
    
    plot(resultsHillClimbing, resultsILS)

main()