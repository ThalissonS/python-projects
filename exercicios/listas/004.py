'''Faça um programa que leia um vetor de 10 caracteres, e diga quantas vogais foram lidas. Imprima as consoantes'''

lista = list()
vogais = ['a', 'e', 'i', 'o', 'u']
vogais_quantidade = 0

vetor = str(input('Digite um vetor com 10 caracteres: ')).lower()
lista.append(vetor)

for c in vogais:
    if c in lista[0]:
        print(c, end=', ')
        vogais_quantidade += 1

print('foram ao total {} vogais presentes'.format(vogais_quantidade))