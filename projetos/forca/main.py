#programador: Thalisson
#feito em 12/12/2021

#imports
import random

#variables
animais = ['formiga', 'elefante', 'baleia', 'leoa', 'vespa', 'abelha']
trabalhos = ['programador', 'frentista', 'dentista', 'taxista', 'coveiro']
objetos = ['cama', 'colher', 'garfo', 'prato', 'cadeira', 'pente', 'espelho']

palavras = [animais, trabalhos, objetos]

nword_ = random.choice(palavras)
nword = random.choice(nword_)
nword = [nword]
nword = nword[0]

dica = ''

#main
if nword in animais:
    dica = 'animal'
if nword in trabalhos:
    dica = 'trabalho'
if nword in objetos:
    dica = 'objeto'

print(nword)
print(dica)

palpite = str(input('>>> ')).lower()[0]

if palpite in nword:
    quantidade = nword.count(palpite)
    index = nword.index(palpite)

    for c in range(index):
        if index != 0:
            nword = nword[0:1+index:]

    print(nword)

else:
    print('EITA')

#output