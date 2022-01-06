'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

class Crime:
    def __init__(self):
        self.telefonou = None
        self.local_crime = None
        self.mora_perto = None
        self.devia = None
        self.trabalhou = None
        self.pontos = 0
        self.participacao = 'inocente'

    def main(self):
        try:
            print('Responda as perguntas a seguir com apenas sim ou não!')
            print('')

            self.quest1()
            self.quest2()
            self.quest3()
            self.quest4()
            self.quest5()

            self.pontos_verificacao()
            print('Você se classifica como', self.participacao)
        except ValueError:
            print('ERROR! Programa está reiniciando...')
            self.main()

    def pontos_verificacao(self):
        if self.pontos == 2:
            self.participacao = 'suspeito(a)'
        if self.pontos > 2 <= 4:
            self.participacao = 'cúmplice'
        if self.pontos == 5:
            self.participacao = 'assassino(a)'

    def quest1(self):
        try:
            self.telefonou = str(input('Você telefonou para a vitima? ')).lower()[0]

            if not self.telefonou in 'sn':
                print('Valor inválido. Por favor digite apenas sim ou não!')
                self.quest1()

            if self.telefonou == 's':
                self.pontos += 1
        except ValueError:
            print('Valor inválido. Por favor digite apenas sim ou não!')
            self.quest1()

    def quest2(self):
        try:
            self.local_crime = str(input('Esteve no local do crime? ')).lower()[0]

            if not self.local_crime in 'sn':
                print('Valor inválido. Por favor digite apenas sim ou não!')
                self.quest2()

            if self.local_crime == 's':
                self.pontos += 1
        except ValueError:
            print('Valor inválido. Por favor digite apenas sim ou não!')
            self.quest2()

    def quest3(self):
        try:
            self.mora_perto = str(input('Mora perto da vítima? ')).lower()[0]

            if not self.mora_perto in 'sn' :
                print('Valor inválido. Por favor digite apenas sim ou não!')
                self.quest3()

            if self.mora_perto == 's':
                self.pontos += 1
        except ValueError:
            print('Valor inválido. Por favor digite apenas sim ou não!')
            self.quest3()

    def quest4(self):
        try:
            self.devia = str(input('Devia para a vítima? ')).lower()[0]

            if not self.devia in 'sn':
                print('Valor inválido. Por favor digite apenas sim ou não!')
                self.quest4()

            if self.devia == 's':
                self.pontos += 1
        except ValueError:
            print('Valor inválido. Por favor digite apenas sim ou não!')
            self.quest4()

    def quest5(self):
        try:
            self.trabalhou = str(input('Já trabalhou com a vítima? ')).lower()[0]

            if not self.trabalhou in 'sn':
                print('Valor inválido. Por favor digite apenas sim ou não!')
                self.quest5()

            if self.trabalhou == 's':
                self.pontos += 1
        except ValueError:
            print('Valor inválido. Por favor digite apenas sim ou não!')
            self.quest5()

if __name__ == '__main__':
    crime = Crime()
    crime.main()