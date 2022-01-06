#Objetivo:
#Faça um programa que gere um numero de 1 a 6 e o usuário tente adivinha-lo


#imports
import random

#main
class Program:
    def __init__(self):
        self.user = 0
        self.numero_gerado = random.randint(1, 6)
        self.tentativas = 0
        self.erros = 0
        self.run = True

    def main(self):
        self.mensagem('Chute o número que o computador gerou (1 ao 6)', 50)

        while self.run:
            self.pergunta()
            self.verificador()

    def verificador(self):
        if self.user > 6 or self.user < 0:
            print('Resposta Inválida! Por Favor digite um número de 1 ao 6.')
            print('')
            self.pergunta()

        if self.user > self.numero_gerado:
            self.erros += 1
            print('Tente um número menor')
            print('')
        if self.user < self.numero_gerado:
            self.erros += 1
            print('Tente um número maior')
            print('')

        if self.user == self.numero_gerado:
            print('=' * 50)
            if self.tentativas > 1:
                print('Parabéns! Você acertou em {} tentativas.'.format(self.tentativas))
            else:
                print('Parabéns! Você acertou em {} tentativa.'.format(self.tentativas))
            if self.erros > 1 or self.erros == 0:
                print('E você errou {} vezes'.format(self.erros))
            else:
                print('E você errou {} vez'.format(self.erros))
            print('=' * 50)
            self.jogar_novamente()

    def jogar_novamente(self):
        try:
            print('')
            sair = str(input('Deseja ir novamente? ')).upper()[0]

            if sair not in 'SN':
                print('Por favor, responda apenas com sim ou não.')
                self.jogar_novamente()
            if sair == 'S':
                self.numero_gerado = random.randint(1, 6)
                self.erros = self.tentativas = self.user = 0
                self.main()
            if sair == 'N':
                print('')
                print('Obrigado por participar!! Volte sempre.')
                self.run = False
        except ValueError:
            print('Por favor, responda apenas com sim ou não.')
            self.jogar_novamente()
        except IndexError:
            print('Por favor, responda apenas com sim ou não.')
            self.jogar_novamente()


    def mensagem(self, msg:str, n=0, enfeite=True):
        if enfeite:
            print('=' * n)
            print(msg)
            print('=' * n)
        else:
            print(msg)

    def pergunta(self):
        try:
            self.tentativas += 1
            self.user = int(input('Qual número o computador escolheu? '))
        except ValueError:
            print('Resposta Inválida! Por Favor digite um número de 1 ao 6.')
            print('')
            self.pergunta()

#output
if __name__ == '__main__':
    program = Program()
    program.main()