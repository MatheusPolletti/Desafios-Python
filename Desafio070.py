'''
print('\033[33m')
print('-'*13)
print('\033[34m', end='')
print('Loja Polletti', end='')
print('\033[m')
print('\033[33m', end='')
print('-'*13, '\033[m\n')

cont = produtos = valorTotal = 0

while True:
    nome = str(input('\nDigite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto R$'))
    if cont == 0 or preco < maisBaratoPreco:
        maisBaratoPreco = preco
        maisBaratoNome = nome
        cont += 1
    if preco > 1000:
        produtos += 1
    valorTotal += preco
    print('-'*20)
    continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    while True:
            if continuar not in 'sn':
                print('-'*20)
                continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
            else:
                break
    if continuar in 'n':
        break

print('\n\033[32m--------------- Fim Do programa ---------------\033[m')
print(f'O valor total gasto na sua compra foi de R${valorTotal}.\nExistem {produtos} que custam mais de R$1.000,00.\nO produto mais barato é o {maisBaratoNome}.')
'''

# Guanabará

menor = cont = totMil = total = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Digite o preço R$'))
    cont += 1
    total += preco
    resp = ' '
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total do produto é R${total:.2f}')
print(f'Temos {totMil} produtos custando mais de mil reais')
print(f'O menor preço é de R${menor} que é o produto {barato}')