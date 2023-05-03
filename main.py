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
    
    #fig1 = plt.figure(figsize=(10, 7))
    #fig2 = plt.figure(figsize=(10, 7))
    #ax1 = fig1.add_axes([0, 0, 1, 1])
    #ax2 = fig2.add_axes([0, 0, 1, 1])
    #fig1 = plt.figure()
    #ax1 = fig1.add_axes([0, 0, 1, 1])
    #fig2 = plt.figure()
    #ax2 = fig2.add_axes([0, 0, 1, 1])
    #fig3 = plt.figure()
    #ax3 = fig3.add_axes([0, 0, 1, 1])
    #fig4 = plt.figure()
    #ax4 = fig4.add_axes([0, 0, 1, 1])

    plt.boxplot(dataFunction1HC)
    plt.show()
    plt.boxplot(dataFunction1ILS)
    plt.show()
    plt.boxplot(dataFunction2HC)
    plt.show()
    plt.boxplot(dataFunction2ILS)
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