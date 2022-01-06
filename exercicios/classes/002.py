'''Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do lado, retornar valor do dado e calcular área'''

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        self.area = None

    def mudar_lado(self):
        self.tamanho_lado = float(input('Digite o novo valor do lado: '))
    def retorna_lado(self):
        print('Lado do dado: ')
        print(self.tamanho_lado)
    def calcula_area(self):
        self.area = self.tamanho_lado ** 2
        print(self.area)

if __name__ == '__main__':
    modelar = Quadrado(5)
    modelar.mudar_lado()
    modelar.calcula_area()
    modelar.retorna_lado()