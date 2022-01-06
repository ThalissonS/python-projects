'''Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa'''

vetores = list()
for c in range(1, 11):
    numero = float(input('Digite o {}° número: '.format(c)))
    vetores.append(numero)

vetores.reverse()
print(vetores)