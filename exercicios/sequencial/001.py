"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

class Programa:
    def __init__(self):
        self.regulamento = 50
        self.peso = 0
        self.excesso = 0
        self.multa = 0

    def main(self): #programa padrão
        self.peso_peixe() #reponsável por perguntar quanto de peso ao final deu
        self.calc_excesso() #reponsável por calcular o excesso exercido
        self.calc_multa() #responsável por calcular a multa exercida
        self.resultado() #imprime o resultado ao usuário

    def peso_peixe(self):
        try:
            self.peso = float(input('Peso dos peixes ao total: '))
        except ValueError:
            print('Valor inválido! Tente Novamente.')
            self.peso_peixe()

    def calc_excesso(self):
        try:
            if self.peso > self.regulamento:
                self.excesso = self.peso - self.regulamento
        except ValueError:
            print('Erro inesperado! Tente novamente.')
            self.main()

    def calc_multa(self):
        try:
            if self.peso > self.regulamento:
                self.multa = self.excesso  * 4 #o quatro equivale a multa a ser paga
        except ValueError:
            print('Erro inesperado! Tente novamente.')
            self.main()

    def resultado(self):
        print('=' * 50)
        print('Peso Total: {}K'.format(self.peso))
        print('Excesso: {}K'.format(self.excesso))
        print('-' * 50)
        print('Valor a se pagar: R${:.2f}'.format(self.multa))
        print('=' * 50)

if __name__ == '__main__':
    programa = Programa()
    programa.main()