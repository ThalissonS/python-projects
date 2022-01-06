'''Crie uma classe capaz de modelar uma bola.
atrutos: cor, circunferência, material
metodos: trocarCor, mostraCor'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = str(input('Digite sua nova cor: '))
    def mostraCor(self):
        print('Cor selecionada:')
        print(self.cor)

if __name__ == '__main__':
    bola = Bola('vermelho', 30, 'couro')
    bola.trocaCor()