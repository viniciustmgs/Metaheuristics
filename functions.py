import math

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