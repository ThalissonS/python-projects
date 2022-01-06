import funcoes

def menu():
    print('''Menu:
[ 1 ] Comprimento
[ 2 ] Raio
[ 3 ] Arco
[ 4 ] Área
[ 0 ] Sair''')
def linha(n):
    print('-' * n)
def space():
    print('')
def escolha(m):
    global run

    if m == 0:
        print('Obrigado! Tenha um ótimo dia.')

        run = False
    if m == 1:
        raio = float(input('Raio: '))
        pi = float(input('Pi: '))

        fuction = funcoes.Comprimento(raio, pi)
        comprimento = fuction.calculo()

        linha(25)
        print('O comprimento da circunferência equivale à {:.2f}'.format(comprimento))

    if m == 2:
        comprimento = float(input('Comprimento: '))
        pi = float(input('Pi: '))

        fuction = funcoes.Raio(comprimento, pi)
        raio = fuction.calculo()

        linha(25)
        print('O raio da circunferência equivale à {:.2f}'.format(raio))

    if m == 3:
        raio = float(input('Raio: '))
        angulo = float(input('Ângulo: '))

        fuction = funcoes.Arco(raio, angulo)
        arco = fuction.calculo()

        linha(25)
        print('O arco da circunferência equivale à {:.2f}'.format(arco))

    if m == 4:
        raio = float(input('Raio: '))
        pi = float(input('Pi: '))

        fuction = funcoes.Area(raio, pi)
        area = fuction.calculo()

        linha(25)
        print('A área da circunferência equivale à {:.2f}'.format(area))

run = True
while run:
    linha(25)
    menu()
    m = int(input('>>> '))
    linha(25)
    escolha(m)