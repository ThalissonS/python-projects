'''Faça um programa que leia quatro notas, mostre as notas e a média na tela'''

notas = list()
media = 0

for c in range(1, 5):
    nota = float(input('Digite sua {}° nota: '.format(c)))
    notas.append(nota)

for c in notas:
    media += c

media /= 4
notas.sort(reverse=False)
print('As suas notas foram:')
print(notas)
print('E sua média final foi: {:.1f}'.format(media))