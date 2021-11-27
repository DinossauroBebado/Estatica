from estatica import *
import math
import numpy as np


def ex1():
    P = 741
    angulo = 41
    t = (P*3)/(math.sin(math.radians(angulo))*3 + 6)
    print(t)
    Ax = math.cos(math.radians(angulo))*t

    Ay = (-t*math.sin(math.radians(angulo)) + P - t)

    Ve = (-t*math.sin(math.radians(angulo)) - t)

    Ne = Ax

    Vf = P - t

    print(f"t:{t}, Ax: {Ax}, Ay: {Ay},Ve: {Ve},Ne: {Ne},Vf: {Vf}")


def ex2():
    r = 21
    a = r/2

    xone = (4*r)/(3*math.pi)
    print(xone)
    xtwo = a/2
    print(xtwo)
    print(xone-xtwo)


def ex3():
    a = 6
    b = a*2
    c = a*3
    A = (math.pi*(18.97366596101)/2)*(18.97366596101)
    print(A)
    B = math.pi*12*12
    C = math.pi*40*24

    Som = 2*A + B + C
    print(Som)

    area = (b + c/2)*(c*b) + 2*((b+(c/3))*((a*c)/2))
    v = 2*math.pi*area

    print(v)


if __name__ == "__main__":
    # ex1()
    ex2()
    ex3()
