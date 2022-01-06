import sqlite3 as sq

dados = sq.connect('registros.db')
cursor = dados.cursor()

#tabela: registros

class Cadastro:
    def __init__(self):
        self.username = None
        self.password = None
        self.opcao = None
        self.run = True

    def main(self):
        while self.run:
            self.menu()
            self.menu_verficacao()

    def linha(self, x=1):
        if x == 1:
            print('-' * 50)
        if x == 2:
            print('=' * 50)

    def menu(self):
        try:
            print('=' * 50)
            print('''Opções:
[ 1 ] Login
[ 2 ] Register
[ 0 ] Exit''')
            print('=' * 50)
            self.opcao = int(input('>>> '))
            self.linha()
        except ValueError:
            self.linha()
            print('ERROR! Valor desconhecido. Por favor insira apenas os valores citados!')
            self.menu()

    def menu_verficacao(self):
        if self.opcao > 2 or self.opcao < 0:
            print('ERROR! Valor desconhecido. Por favor insira apenas os valores citados!')
            self.menu()
        if self.opcao == 1:
            pass
        if self.opcao == 2:
            self.username = str(input('E-mail: ')).lower()
            self.password = str(input('Senha 4 digitos: '))

            while len(self.password) != 4:
                self.password = str(input('Senha 4 digitos: '))

            cursor.execute('INSERT INTO registros VALUES("'+self.username+'", "'+self.password+'")')
            self.linha()
            print('Registrado com sucesso!')
        if self.opcao == 0:
            print('Volte sempre!')
            self.linha()
            self.run = False

cadastro = Cadastro()
cadastro.main()

dados.commit()
dados.close()