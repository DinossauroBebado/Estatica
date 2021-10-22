from estatica import *
import math
import numpy as np


def ex1():
    r = Vector(0.2*math.cos(math.radians(45)), -
               -0.05,
               - 0.2*math.sin(math.radians(45)))

    F = Vector(-16*math.cos(math.radians(30)),
               0,
               16*math.sin(math.radians(30))
               )
    momento = (r.produto_vetorial(F)).produto_escalar(plano_y)

    print(f"Mo: {momento}")


def ex2():
    ra = Vector(200, 300, 0)
    rb = Vector(300, 800, 0)

    F_one = Vector(0, 0, -80)

    F_two = Vector(0, 0, 80)

    m_one = ra.produto_vetorial(F_one)

    m_two = rb.produto_vetorial(F_two)

    print(m_one)
    print(m_two)

    result = m_one + m_two
    print(Força(result))


if __name__ == "__main__":
    ex1()
    ex2()
