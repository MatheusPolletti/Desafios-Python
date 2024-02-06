# Meu

'''lista = list()

while True:
    resp = ' '
    num = int(input('Digite seu número para ser adicionado: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Esse valor já foi adicionado!')
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break

lista.sort()
print(f'\n\033[34mOs valores digitados foram {lista}\033[m')'''

# Guanabará

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já cadastrado.')
    r = str(input('Quer continuar? [s/n] ')).lower().strip()[0]
    if r in 'n':
        break

numeros.sort()
print(f'Você digitou os números {numeros}')
