from estatica import *
import math
import numpy as np


def ex1():

    Fce = Vector(0.18, 0.7, -0.45)
    print(Fce.unitario())
    Fcd = Vector(-1, 0.7, -0.45)
    print(Fcd.unitario())

    T = -166.725/(-0.369 - 0.2385)
    print(T)

    A = Vector(0.91, 0, 0.45)

    s = A.produto_vetorial(Vector(0.2114, 0.822, -0.5285))*T
    j = A.produto_vetorial(Vector(-0.7687, 0.5381, -0.3459))*T
    k = Vector(0.59-0.09, 0, 0.225).produto_vetorial(Vector(0, -741, 0))
    print(s + j + k)
    print(s, j, k)
    print(T*0.21 - T*0.76)
    print(472.1 + T*0.82 + T + 0.53 - 1)
    print(534.07-T*0.52-T*0.34)


def ex2():
    ...


if __name__ == "__main__":
    ex1()
    ex2()
