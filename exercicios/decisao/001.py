'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'w', 'y', 'z', 'ç']

letra = str(input('Digite uma letra: ')).strip().lower()[0]

if letra in numeros:
    print('Pedi para digitar uma letra não um número!!')
elif letra in vogais:
    print('A letra {} que você digitou é uma vogal!!'.format(letra))
elif letra in consoantes:
    print('A letra {} que você digitou é uma consoante'.format(letra))