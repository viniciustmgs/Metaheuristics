import random
import math

# criando a classe de cada F.O.

class Function1:
    def __init__(self) -> None:
        pass
    def caculate(x, y):
        result = x^2+y^2+25*((math.sin(x))^2+(math.sin(y))^2)
        return result

class Function2:
    def __init__(self) -> None:
        pass
    def calculate(x, y):
        result = -(y+47)*math.sin(math.sqrt(math.fabs(y+0.5*y+47)))-x*math.sin(math.sqrt(math.fabs(x-(y+47))))
        return result

#definindo a função da meta-heurística ILS

def iteratedLocalSearch (function, domain):
    print("teste")

# aqui será definida a função para a segunda meta-heurística, mas ainda não decidi qual será

#criando uma instância das F.O.'s, para que possam ser passadas como parâmetro para as meta-heurísticas

function1 = Function1
function2 = Function2

#colocando os domínios que serão utilizados pelas meta-heurísticas em um vetor

domains = [[-5, 5], [-2, 2], [-512, 512], [400, 512]]

# iniciando a execução das meta-heurísticas em um loop, cada uma das 2 é executada
# 30 vezes para cada um dos domínios

for i in range(2):
    for j in range(4):
        for k in range(30):
            if(j < 2):
                # entra nesse if se for os domínios A e B, portanto executa as meta-heurísticas
                # para a função 1
                print("executar a primeira função")
            else:
                # entra nesse if se for os domínios C e D, portanto executa as meta-heurísticas
                # para a função 2
                print("executar a segunda função")    

# valores finais serão salvos em vetores, no final exibir o resultado final e plotar em boxplot