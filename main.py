import random
import matplotlib.pyplot as plt
from functions import Function1, Function2   
from hillClimbing import hillClimbing
from iteratedLocalSearch import iteratedLocalSearch
from results import Results

# gerador de solução inicial

def generateInitialSolution (domain):
    solution = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
    return solution

def printResults(resultsHillClimbing, resultsILS):
    resultsHC1 = Results(resultsHillClimbing[0][0])
    resultsHC2 = Results(resultsHillClimbing[1][0])
    resultsHC3 = Results(resultsHillClimbing[2][0])
    resultsHC4 = Results(resultsHillClimbing[3][0])

    resultsILS1 = Results(resultsILS[0][0])
    resultsILS2 = Results(resultsILS[1][0])
    resultsILS3 = Results(resultsILS[2][0])
    resultsILS4 = Results(resultsILS[3][0])

    allResultsHC = [resultsHC1, resultsHC2, resultsHC3, resultsHC4]
    allResultsILS = [resultsILS1, resultsILS2, resultsILS3, resultsILS4]
    
    for idResult, result in enumerate(allResultsHC):
        for x in range(30):
            result.insert(resultsHillClimbing[idResult][x])

    for idResult, result in enumerate(allResultsILS):
        for x in range(30):
            result.insert(resultsILS[idResult][x])       

    allResults = allResultsHC + allResultsILS

    for result in allResults:
        result.calculate()
    
    print("\nHill Climbing, Função 1, Domínio A: \n")
    allResults[0].printResults()
    print("\nHill Climbing, Função 1, Domínio B: \n")
    allResults[1].printResults()
    print("\nHill Climbing, Função 2, Domínio C: \n")
    allResults[2].printResults()
    print("\nHill Climbing, Função 2, Domínio D: \n")
    allResults[3].printResults()
    print("\nIterated Local Search, Função 1, Domínio A: \n")
    allResults[4].printResults()
    print("\nIterated Local Search, Função 1, Domínio B: \n")
    allResults[5].printResults()
    print("\nIterated Local Search, Função 2, Domínio C: \n")
    allResults[6].printResults()
    print("\nIterated Local Search, Função 2, Domínio D: \n")
    allResults[7].printResults()
    
def plot(resultsHillClimbing, resultsILS):
    dataFunction1HC = []
    dataFunction1ILS = []
    dataFunction2HC = []
    dataFunction2ILS = []
    for x in range(4):
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        for y in range(30):
            if (x < 2):    
                data1.append(resultsHillClimbing[x][y][1])
                data2.append(resultsILS[x][y][1])
            else:
                data3.append(resultsHillClimbing[x][y][1])
                data4.append(resultsILS[x][y][1])    
        if (x < 2):
            dataFunction1HC.append(data1)
            dataFunction1ILS.append(data2)
        else:
            dataFunction2HC.append(data3)
            dataFunction2ILS.append(data4) 

    plt.boxplot(dataFunction1HC, labels=["Domínio A", "Domínio B"])
    plt.title("Função 1: Hill Climbing")
    plt.show()
    plt.boxplot(dataFunction1ILS, labels=["Domínio A", "Domínio B"])
    plt.title("Função 1: Iterated Local Search")
    plt.show()
    plt.boxplot(dataFunction2HC, labels=["Domínio C", "Domínio D"])
    plt.title("Função 2: Hill Climbing")
    plt.show()
    plt.boxplot(dataFunction2ILS, labels=["Domínio C", "Domínio D"])
    plt.title("Função 2: Iterated Local Search")
    plt.show()

# iniciando a execução das meta-heurísticas em um loop, cada uma das 2 é executada
# 30 vezes para cada um dos domínios 

def main():
    function1 = Function1
    function2 = Function2
    domains = [[-5, 5], [-2, 2], [-512, 512], [400, 512]]
    resultsILS = []
    resultsHillClimbing = []
    percentage = 0
    print("\nAguarde a execução do programa (isso pode demorar vários minutos): \n")
    for i in range(4):
        executionILS = []
        executionHillClimbing = []
        for j in range(30):
            if (i < 2):
                # entra nesse if se for os domínios A e B, portanto executa as meta-heurísticas
                # para a função 1
                initialSolution = generateInitialSolution(domains[i])
                executionHillClimbing.append(hillClimbing(function1, domains[i], 100000, initialSolution))
                initialSolution = generateInitialSolution(domains[i])
                executionILS.append(iteratedLocalSearch(function1, domains[i], initialSolution))
            else:
                # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
                # para a função 2
                
                initialSolution = generateInitialSolution(domains[i])
                executionHillClimbing.append(hillClimbing(function2, domains[i], 100000, initialSolution))
                initialSolution = generateInitialSolution(domains[i])
                executionILS.append(iteratedLocalSearch(function2, domains[i], initialSolution))
            percentage += 1
            print("{:.2f}".format((percentage/120)*100), "%", end="\r")    
        resultsHillClimbing.append(executionHillClimbing)
        resultsILS.append(executionILS)

    # valores finais salvos em vetores, agora os resultados são impressos, e um boxplot é feito
    print("Resultados: \n")
    printResults(resultsHillClimbing, resultsILS)
    plot(resultsHillClimbing, resultsILS)
    
main()