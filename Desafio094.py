# Meu

'''lista = list()

pessoa = dict()

mulheres = totalIdade = contador = 0

while True:
    resp = ' '
    pessoa['Nome'] = str(input('Digite seu nome: ')).strip().capitalize()
    pessoa['Sexo'] = ' '
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Digite seu Gênero: [M/F]: ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Digite sua idade: '))
    lista.append(pessoa.copy())
    contador += 1
    totalIdade += pessoa['Idade']
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

mediaIdade = totalIdade / contador

print(f'\nForam cadastradas um total de {contador} pessoas.')
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'As mulheres cadastradas foram: ', end='')

for opcao in lista:
    if opcao['Sexo'] in 'F':
        print(opcao['Nome'], end=' ')

print(f'\n\nAs pessoas que estão com acima da média de idade são: ', end='')

for opcao in lista:
    if opcao['Idade'] > mediaIdade:
        print(f'Nome = {opcao['Nome']}; ', end='')
        print(f'Sexo = {opcao['Sexo']}; ', end='')
        print(f'Idade = {opcao['Idade']}', end='')
        print('\n')

print('<==== Processo Finalizado ====>')'''

# Guanabará

pessoa = dict()

galera = list()

soma = media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Digite M ou F!')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar(S/N)? ')).upper()[0]
        if resp in 'SN': 
            break
        print('Erro! Digite S ou N!')
    if resp == 'N':
        break

print(f'\n{galera}\n')

print(f'A todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f}')
print(f'As mulheres cadastradas são: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']} ', end='')
print()
print('A lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print(f'')
        for chave, valor in p.items():
            print(f'{chave} = {valor}; ', end='')
        print()

print('\n--Fim--')