numeros = list()
numeros_par = list()
numeros_impar = list()

for c in range(1, 21):
    numero = int(input('Digite o {}° número: '.format(c)))
    if not numero in numeros:
        numeros.append(numero)

        if numero % 2 == 0:
            numeros_par.append(numero)
        else:
            numeros_impar.append(numero)

print('Todos os valores:')
print(numeros)
print('Apenas os ímpares:')
print(numeros_impar)
print('Apenas os pares:')
print(numeros_par)