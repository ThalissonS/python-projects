'''Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 2 caracteres
b. Idade: entre 0 e 150
c. Salário: maior que zero ou igual
d. Sexo: "f" ou "m"
e. Estado Civil: "s", "c", "v", "d"'''

class Cadastro:
    def __init__(self):
        self.nome = None
        self.idade = 0
        self.salario = 0
        self.sexo = None
        self.estado_civil = None

    def main(self):
        try:
            self.nome_pergunta()
            self.idade_pergunta()
            self.salario_pergunta()
            self.sexo_pergunta()
            self.estado_pergunta()
            self.preparativos()
            self.resultado_final()
        except ValueError:
            print('ERRO! Programa detectou um erro, estamos reiniciando.')
            self.main()

    def nome_pergunta(self):
        try:
            self.nome = str(input('Nome: ')).capitalize().strip()

            if not len(self.nome) > 2:
                print('ERRO! Por favor digite um nome maior que 2 caracteres.')
                self.nome_pergunta()

        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.nome_pergunta()

    def idade_pergunta(self):
        try:
            self.idade = int(input('Idade: '))

            if not self.idade >= 0 <= 150:
                print('Idade inválida! Tente novamente.')
                self.idade_pergunta()

        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.idade_pergunta()

    def salario_pergunta(self):
        try:
            self.salario = float(input('Salário [0 para nada]: R$'))

            if self.salario < 0:
                print('Valor inválido! Tente novamente.')
                self.salario_pergunta()

        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.salario_pergunta()

    def sexo_pergunta(self):
        try:
            self.sexo = str(input('Sexo [F/M]: ')).lower().strip()[0]

            if not self.sexo in 'fm':
                print('Valor inválido! Tente novamente.')
                self.sexo_pergunta()

        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.sexo_pergunta()

    def estado_pergunta(self):
        try:
            self.estado_civil = str(input('Estado Civil: ')).strip().lower()[0]

            if not self.estado_civil in 'scdv':
                print('Valor inválido! Tente novamente.')
                self.estado_pergunta()

        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.estado_pergunta()

    def preparativos(self):
        if self.sexo == 'm':
            self.sexo = 'masculino'
            if self.estado_civil == 'c':
                self.estado_civil = 'casado'
            elif self.estado_civil == 's':
                self.estado_civil = 'solteiro'
            elif self.estado_civil == 'v':
                self.estado_civil = 'viúvo'
            elif self.estado_civil == 'd':
                self.estado_civil = 'divorciado'
        elif self.sexo == 'f':
            self.sexo = 'feminino'
            if self.estado_civil == 'c':
                self.estado_civil = 'casada'
            elif self.estado_civil == 's':
                self.estado_civil = 'solteira'
            elif self.estado_civil == 'v':
                self.estado_civil = 'viúva'
            elif self.estado_civil == 'd':
                self.estado_civil = 'divorciada'

    def resultado_final(self):
        print('=' * 50)

        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('Salário: R${:.2f}'.format(self.salario))
        print('Sexo:', self.sexo)
        print('Estado Civil:', self.estado_civil)

        print('=' * 50)

if __name__ == '__main__':
    cadastro = Cadastro()
    cadastro.main()