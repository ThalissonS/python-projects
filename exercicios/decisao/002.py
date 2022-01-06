'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

def maiorMenor():
    try:
        numeros = list()

        for c in range(3):
            numero = int(input('Digite um número: '))
            numeros.append(numero)

        maior_numero = max(numeros)
        menor_numero = min(numeros)

        print('O maior número digitado foi:', maior_numero)
        print('E o menor número digitado foi:', menor_numero)

    except ValueError:
        print('Valor inválido!')
        maiorMenor()

if __name__ == '__main__':
    maiorMenor()