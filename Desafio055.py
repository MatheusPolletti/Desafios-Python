maior = 0
menor = 0

for p in range (1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

if maior == menor:
    print('O maior peso e o menor peso são iguais: {0:.2f}'.format(maior))
else:
    print('O maior peso foi de: {0:.2f}kg'.format(maior))
    print('O menor peso foi de: {0:.2f}kg'.format(menor))






'''
Código que eu fiz com defeito, só funcionaria usando menor com um número impossível

menor = maior = 0

for n in range (1, 6):
    peso = float(input('Digite o seu peso em kg: '))
    if peso > maior:
        maior = peso
    elif menor > peso:
        menor = peso

if maior == menor:
    print('O maior e menor peso são iguais: {0:.2f}kg'.format(maior))
else:
    print('\nO maior peso lido foi: {0:.2f}kg'.format(maior))
    print('\nO menor peso lido foi: {0:.2f}kg'.format(menor))
'''