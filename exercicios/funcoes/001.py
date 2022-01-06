'''Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida'''

def data():
    data_numero = str(input('Digite sua data de nascimento (com /): '))

    if len(data_numero) == 10:
        try:
            if data_numero.count('/') == 2:
                data_numero = data_numero.split('/')
                dia = data_numero[0]
                mes = data_numero[1]
                ano = data_numero[2]

                dias = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis', 'vinte e sete', 'vinte e oito', 'vinte e nove', 'trinta', 'trinta e um']
                meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

                dia = dias[int(dia)-1]
                mes = meses[int(mes)-1]

                print('Você nasceu dia {} de {} do ano de {}'.format(dia, mes, ano))
        except ValueError:
            print('Valor inválido!')
            data()

    else:
        print('Valor inválido!')
        data()

data()