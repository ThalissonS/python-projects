'''Faça um programa que leia um vetor de 5 números e mostre-os'''

vetores = list()

for c in range(1, 6):
    numero = int(input(('Digite {}° número inteiro: '.format(c))))
    vetores.append(numero)

print('Os valores digitados foram:')
print(vetores)