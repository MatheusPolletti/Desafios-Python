'''
mulheres = homens = pessoasAdultas = 0

while True:
    print('\033[34m')
    print('-'*20, end='')
    print('\033[m')
    print('\033[35m', end='')
    print('Cadastre uma pessoa')
    print('\033[m', end='')
    print('\033[34m', end='')
    print('-'*20)
    print('\033[m')
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu gênero [M/F]: ')).strip().upper()[0]
    while True:
        if sexo not in 'MF':
            print('\033[31mNão reconhecemos esse caracter\033[m')
            sexo = str(input('Digite o seu gênero [M/F]: ')).strip().upper()[0]
        else:
            break
    print('-'*20)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while True:
        if continuar not in 'SN':
            print('-'*20)
            print('\033[31mNão reconhecemos esse caracter\033[m')
            continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        else:
            break
    if idade >= 18:
        pessoasAdultas += 1
    if sexo in 'M':
        homens += 1
    elif sexo in 'F' and idade < 20:
        mulheres += 1
    if continuar in 'N':
        break

print(f'\n\033[36mA quantia de pessoas com mais de 18 anos é de {pessoasAdultas}.\nExistem {homens} homens cadastrados.\nExistem {mulheres} mulheres com menos de 20 anos cadastradas\033[m\n')
'''
totM = totH = tot18 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    resp = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: M/F ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Total de homens cadastrados é {totH}')
print(f'Total de mulheres com menos de 20 é {totM}')