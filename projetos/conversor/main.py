import fuctions

def linha(n):
    print('-' * n)
def space():
    print('')
def main():
    print('''Converter para:
[ 1 ] Radiano
[ 2 ] Grau
[ 0 ] Sair''')
def escolha(m):
    global run

    if m == 0:
        print('Obrigado! Volte novamente.')
        run = False
    if m == 1:
        grau = float(input('Informe o grau: '))

        fuction = fuctions.Radiano(grau)
        radiano = fuction.conversao()

        linha(25)
        print('O valor de {}° é {:.2f}π rad'.format(grau, radiano))

    if m == 2:
        radiano = float(input('Informe o radiano: '))

        fuction = fuctions.Grau(radiano)
        grau = fuction.conversao()

        linha(25)
        print('O valor de {}π rad é {:.2f}° em graus'.format(radiano, grau))

run = True
while run:
    linha(25)
    main()
    m = int(input('>>> '))
    escolha(m)