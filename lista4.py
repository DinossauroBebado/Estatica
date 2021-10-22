from estatica import *
import math
import numpy as np


def exercicio_2():
    A = Vector(0, 0, 3)
    B = Vector(2, 1.25, 0)
    C = Vector(2, -1.25, 0)
    D = Vector(-1, 0, 0)

    peso_tanque = 8000

    AB = B - A
    AC = C - A
    AD = D - A

    print(AB, AC, AD)
    print(AB.modulo(), AC.modulo(), AD.modulo())

    print(math.degrees(math.asin(3/AD.modulo())))
    print(math.degrees(math.asin(3/AC.modulo())))

    eq = np.array([[2*math.sin(math.radians(51.83)), math.sin(math.radians(71.56))],
                   [2*(math.cos(math.radians(51.83))*math.sin(math.radians(58))
                       ), -math.cos(math.radians(71.56))]])
    solv = np.array([peso_tanque, 0])

    solução = np.linalg.solve(eq, solv)

    print(solução)


if __name__ == "__main__":
    exercicio_2()
