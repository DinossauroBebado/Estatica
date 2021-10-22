from estatica import *
import math
import numpy as np


def ex1():

    print("Exercicio 1")
    Tb = 2243
    Tc = Tb/2

    angulo = math.degrees(math.acos((math.cos(math.radians(20))*Tc)/Tb))
    print(f"angulo:{angulo}")

    Td = Tb*math.sin(math.radians(angulo)) + Tc*math.sin(math.radians(20))

    print(f"Td :{Td}")


def ex2():
    print("Exercicio 2")
    A = Vector(0, 0, 10)
    B = Vector(12, -6, 0)
    C = Vector(5, 6, 0)
    D = Vector(-12, 2, 0)

    F = -485
    AB = B-A
    AC = C - A
    AD = D - A

    Tab = AB.unitario()
    print(f"Tab:{Tab}")

    Tac = AC.unitario()
    print(f"Tac:{Tac}")

    Tad = AD.unitario()
    print(f"Tad:{Tad}")

    eq = np.array([[Tab.x, Tac.x, Tad.x],
                   [Tab.y, Tac.y, Tad.y],
                   [Tab.z, Tac.z, Tad.z]])
    solv = np.array([0, 0, F])

    solução = np.linalg.solve(eq, solv)

    print(f"Tab: {solução[0]} lb\nTac: {solução[1]} lb\nTad: {solução[2]} lb ")


def ex3():
    print("Exercicio 3")
    """
        ----B  
     A---   |
     |        |
    |          |
    C----------D
    """
    dx = (-30*0 + -60*4 - 51*12 - 61*15)/-202
    print(dx)
    dy = (-30*10 - 60*4 - 51*0 - 61*10)/-202
    print(dy)


if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
