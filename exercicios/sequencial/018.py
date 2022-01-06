"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

class Programa:
    def __init__(self):
        self.arquivo = 0
        self.velocidade = 0
        self.estimativa = 0

    def main(self):
        self.download_arquivo() #responsável por receber o tamanho do arquivo
        self.download_velocidade() #responsável por receber a velocidade de Mpbs
        self.calc_estimativo() #faz a estimativa de download
        self.resultado() #imprime a resposta ao usuário

    def download_arquivo(self):
        try:
            self.arquivo = float(input('Tamanho do arquivo para download: (Mb) '))
        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.download_arquivo()

    def download_velocidade(self):
        try:
            self.velocidade = float(input('Velocidade de Internet: (Mbps) '))
        except ValueError:
            print('Valor inválido! Tente novamente.')
            self.download_velocidade()

    def calc_estimativo(self):
        try:
            self.estimativa = (self.arquivo * 1000 / self.velocidade)
            self.estimativa /= 60
        except ValueError:
            print('Erro inesperado! Tente novamente.')
            self.main()

    def resultado(self):
        print('-' * 50)
        print('Tempo estimado em {:.2f}m'.format(self.estimativa))
        print('-' * 50)

if __name__ == '__main__':
    programa = Programa()
    programa.main()