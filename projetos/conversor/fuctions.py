class Radiano:
    def __init__(self, grau):
        self.grau = grau
        self.rad = 0

    def conversao(self):
        self.rad = self.grau / 180

        return self.rad

class Grau:
    def __init__(self, rad):
        self.rad = rad
        self.grau = 0

    def conversao(self):
        self.grau = 180 * self.rad

        return self.grau