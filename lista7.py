from estatica import *
import math
import numpy as np


def ex1():
    print("Exercicio 1")
    F_one = Vector(10, -15, -40)
    F_two = Vector(-15, -20, -30)

    A = Vector(0, 250, 100)
    B = Vector(150, 25, 40)

    M_one = F_one.produto_vetorial(A)
    M_two = F_two.produto_vetorial(B)

    M = M_two + M_one

    F_resultante = F_two+F_one

    print(f"M: {M}  \nFr: {F_resultante}")


def ex2():
    """
    C ------ D 
    |        |
    |   FR   |
    |        |
    B--------A

    """
    print("Exercicio 2")
    Fc = -30
    Fd = -20
    Fr = -90

    A = Vector(5.75, 6.75, 0)
    B = Vector(5.75, 0.75, 0)
    C = Vector(0.75, 0.75, 0)
    D = Vector(0.75, 6.75, 0)
    FR = Vector(3.25, 3.75, 0)

    Força_result = Fc+Fd+Fr
    Frel = -Força_result
    print(f"(I) Fr = {Frel} + Fa + Fb")

    # Momento em y
    consty = -(Fc*C.y + Fd*D.y + Fr*FR.y)/FR.y

    print(f"(II) Fr = {B.y/FR.y}Fb + {A.y/FR.y}Fa + {consty}")

    # Momento em x

    constx = -(Fc*C.x + Fd*D.x + Fr*FR.x)/FR.x

    print(f"(III) Fr = {B.x/FR.x:.4f}Fb + {A.x/FR.x:.4f}Fa + {constx:.4f}")

    eq = np.array([[1,     1, -1],
                   [1.8, 0.2, -1],
                   [1.7, 1.7, -1]])

    solv = np.array([-140, -132, -101.5385])

    solução = np.linalg.solve(eq, solv)

    print(f"Fa: {solução[0]}\nFb: {solução[1]}\nFr: {solução[2]} ")


if __name__ == "__main__":
    ex1()
    ex2()
