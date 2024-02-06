# Meu
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = (n1, n2, n3, n4)

print(f'\nVocê digitou os valores: {tupla[0]}, {tupla[1]}, {tupla[2]} e {tupla[3]}')

print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')

print('\nOs valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end='')
'''

# Guanabará

num = (int(input('Digite um número: ')),
 int(input('Digite outro número: ')),
 int(input('Digite mais um número: ')),
 int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')