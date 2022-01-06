#Objetivo:
#Faça um programa que gere um numero de 1 a 6 e o usuário tente adivinha-lo

import random

#fuctions
def deco(n):
    print(n * '-')
def space():
    print('')
def verificacion():
    global erros, chute, numero_gerado, tentativas
    if chute == numero_gerado:
        deco(50)
        if tentativas == 1:
            print(f'Parabéns! Você ganhou em {tentativas} tentativa')
        if tentativas > 1:
            print(f'Parabéns! Você ganhou em {tentativas} tentativas')
        if erros == 1:
            print(f'E você errou {erros} vez')
        else:
            print(f'E você errou {erros} vezes')
        deco(50)
        leave()
    if chute > 6 or chute < 0:
        print('Chute um número de 1 a 6')
        tentativas -= 1
    else:
        if chute > numero_gerado:
            print('Tente um número menor')
            erros += 1
        if chute < numero_gerado:
            print('Tente um número maior')
            erros += 1
def leave():
    global run, numero_gerado, erros, chute, tentativas
    user = str(input('Deseja jogar novamente? ')).lower()[0]

    if user not in 'sn':
        leave()
    if user[0] == 's':
        numero_gerado = random.randint(1, 6)
        erros = chute = tentativas = 0

        while run:
            tentativas += 1
            chute = int(input('Qual número o computador escolheu? '))
            verificacion()
    if user[0] == 'n':
        run = False

#objects
numero_gerado = random.randint(1, 6)
erros = chute = tentativas = 0
run = True

#main
while run:
    try:
        tentativas += 1
        chute = int(input('Qual número o computador escolheu? '))
        verificacion()
    except ValueError:
        tentativas += 1
        chute = int(input('Isto não é um número. Qual número o computador escolheu? '))
        verificacion()