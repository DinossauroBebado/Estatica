from estatica import *
import math
import numpy as np


def ex1():
    print("Ex1")
    r1 = Vector(0.05, 0.4, 0)
    f1 = Vector(0, 4000, 0)
    f2 = Vector(-800, 0, 0)
    print(r1.produto_vetorial(f2))


def ex2():
    print("EX2")
    r1 = Vector(200*math.sin(math.radians(15)),
                200*math.cos(math.radians(15)),
                75)

    F = Vector(-20*math.sin(math.radians(75)),
               20*math.cos(math.radians(75)),
               0)

    resposta = r1.produto_vetorial(F)
    print(f"Mo: {resposta}")


if __name__ == "__main__":
    ex1()
    ex2()
