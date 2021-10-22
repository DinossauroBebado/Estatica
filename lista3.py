from estatica import Vector, Força, plano_x
import math


def exercicio_1():
    print("exercicio 1")
    ForcaAB = 900
    ForcaAC = 600
    A = Vector(0, 0, 6)
    B = Vector((9/4)*math.sqrt(2), -(9/4)*math.sqrt(2), 0)
    C = Vector(-3, -6, 0)

    AB = B-A
    AC = C - A

    print(AB)
    F_AB = AB.unitario()*ForcaAB
    print(AC)
    F_AC = AC.unitario()*ForcaAC
    print(F_AB, F_AC)
    F_Resultante = Força(F_AC+F_AB)
    print(F_Resultante)


def exercio_2():
    print("Ex 2-----------------")

    A = Vector(15, 0, 0)
    B = Vector(0, 3, 8)
    C = Vector(0, -8, 12)

    F = 55

    AC = C-A
    AB = B-A
    CB = B - A

    angulo = AB.achar_angulo(AC)

    f_ab = Força(AB)

    f_ac = Força(AC)
    print(f_ab.vector.unitario())
    print(f_ac.vector.unitario())

    f = f_ab.vector.unitario()*F
    print(f)
    print(f"FAC {f.produto_escalar(f_ac.vector.unitario())}")

    print(f"Fx {plano_x.produto_escalar(f)}")


if __name__ == "__main__":
    exercicio_1()
    exercio_2()
