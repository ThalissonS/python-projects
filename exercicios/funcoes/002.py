'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.'''

def reverseNumber():
    try:
        numero = int(input('Digite um número inteiro: '))
        numero = str(numero)
        lista = list()

        for c in range(len(numero)):
            lista.append(numero[c])

        lista.reverse()
        print('O reverso de {} é '.format(numero), end='')
        for c in lista:
            print(c, end='')
        print('!')

    except ValueError:
        print('Valor inválido!')
        reverseNumber()

reverseNumber()