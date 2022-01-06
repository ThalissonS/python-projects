class Comprimento:
    def __init__(self, raio, pi=3.14):
        self.raio = raio
        self.comprimento = 0
        self.pi = pi

    def calculo(self):
        self.comprimento = 2 * self.pi * self.raio

        return self.comprimento

class Raio:
    def __init__(self, comprimento, pi=3.14):
        self.pi = pi
        self.comprimento = comprimento
        self.raio = 0

    def calculo(self):
        self.raio = (2 * self.pi) / self.comprimento

        return self.raio

class Arco:
    def __init__(self, raio, angulo, pi=3.14):
        self.raio = raio
        self.angulo = angulo
        self.pi = pi
        self.arco = 0

    def calculo(self):
        self.arco = ((2*self.pi*self.raio) * self.angulo) / 360

        return self.arco

class Area:
    def __init__(self, raio, pi=3.14):
        self.raio = raio
        self.pi = pi
        self.area = area

    def calculo(self):
        self.area = self.pi * (self.raio**2)

        return self.area