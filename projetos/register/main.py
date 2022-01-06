print('=' * 50)
cadastre_email = str(input('E-mail: ')).lower().strip()
print('=' * 50)
emails = []
c = 0

with open('email.txt', 'r', encoding='utf-8') as arquivo:
    gmail = arquivo.readlines()

for linha in gmail:
    emails.append(linha)

while c < len(emails):
    for linha in emails:
        if '\n' in linha:
            emails.remove(linha)
            linha = linha[0:-1]
            emails.append(linha)
    c += 1

if cadastre_email in emails:
    print('E-mail já cadastrado!')
elif not cadastre_email in emails:
    print('E-mail cadastrado com sucesso!')

    with open('email.txt', 'a', encoding='utf-8') as arquivo:
        gmail = arquivo.write('\n{}'.format(cadastre_email))