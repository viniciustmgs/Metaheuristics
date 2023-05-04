import numpy as np

class Results:
    
    def __init__(self, solution) -> None:
        self.best = solution
        self.worst = solution
        self.results = []
        self.avarage = 0
        self.standardDeviation = 0

    def insert(self, solution):
        if (solution[1] < self.best[1]):
            self.best = solution
        if (solution[1] > self.worst[1]):
            self.worst = solution
        self.results.append(solution[1])
        print(self.results)
    
    def calculate(self):
        self.avarage = np.mean(self.results)
        self.standardDeviation = np.std(self.results)
    
    def printResults(self):
        print("Melhor resultado: X = ", self.best[0][0], ", Y = ", self.best[0][1], ", resultado = ", self.best[1])
        print("Pior resultado: X = ", self.worst[0][0], ", Y = ", self.worst[0][1], ", resultado = ", self.worst[1])
        print("Média dos resultados: ", self.avarage)
        print("Desvio padrão: ", self.standardDeviation)