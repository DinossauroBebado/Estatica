import math


class Vector:
    """
    Cria um vetor em 3 dimensões e cobre a maioria das operações 
    com vetor como soma, substração , modulo e multiplicação
    Além de produto escalar e vetorial 
    TODO Difenciar o sinal de * para int e vetor 
                no momento o sinal so pode ser usada para multiplicar um vetor por um inteiro 
                e a ordem esta alterando o resultado
         Criar um sinal proprio para multiplicação vetorial

    """

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x:.4f} ,{self.y:.4f}, {self.z:.4f} )"

    def __add__(self, other) -> int:
        i = self.x + other.x
        j = self.y + other.y
        z = self.z + other.z

        return Vector(i, j, z)

    def __sub__(self, other) -> int:
        i = self.x - other.x
        j = self.y - other.y
        k = self.z - other.z

        return Vector(i, j, k)

    def __mul__(self, escalar):
        i = self.x*escalar
        j = self.y*escalar
        k = self.z*escalar
        return Vector(i, j, k)

    def modulo(self) -> int:
        sum = self.x**2 + self.y**2 + self.z**2
        return math.sqrt(sum)

    def unitario(self):
        i = self.x/self.modulo()
        j = self.y/self.modulo()
        k = self.z/self.modulo()
        return Vector(i, j, k)

    def produto_escalar(self, other):
        i = self.x*other.x
        j = self.y*other.y
        k = self.z*other.z
        return i+j+k

    def produto_vetorial(self, other):
        k = self.x*other.y - self.y*other.x
        i = self.y*other.z - self.z*other.y
        j = self.z*other.x - self.x*other.z
        return Vector(i, j, k)

    def achar_angulo(self, other):
        "Calcula o angulo entre dois vetores "
        divisao = (self.produto_escalar(other) / (self.modulo() *
                   other.modulo()))  # produto escalar / mult modulos
        angulo = math.acos(divisao)
        return math.degrees(angulo)


class Força(Vector):
    """
    Transforma um vetor qualquer em um vetor de uma força 
    tento informações de forma mais direta alem de coisa unicas 
    como o angulo estre as componentes 

    """

    def __init__(self, vector) -> None:
        self.resultante = vector.modulo()
        self.vector = vector
        self.angulos()

    def __repr__(self) -> str:

        return f"Vetor:{self.vector},Fr: {self.resultante:.4f}, alfa : {self.alfa:.4f} beta: {self.beta:.4f} teta: {self.teta:.4f}"

    def angulos(self):
        self.alfa = math.degrees(math.acos(self.vector.x/self.resultante))
        self.beta = math.degrees(math.acos(self.vector.y/self.resultante))
        self.teta = math.degrees(math.acos(self.vector.z/self.resultante))


plano_x = Vector(1, 0, 0)

plano_y = Vector(0, 1, 0)

plano_z = Vector(0, 0, 1)

g = 9.81
