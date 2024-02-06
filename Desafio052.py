print('\n\n\n')
print('-'*21)
print('\033[34mAnalisar Número Primo\033[m')
print('-'*21)

num = int(input('\nDigite um número inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{0} '.format(c), end='')

print('\033[m')

print('\nO número {0} foi dividido {1} vezes\n'.format(num, total))

if total == 2:
    print('\033[35mEsse número é primo\033[m\n')
else:
    print('\033[35mEsse número não é primo\033[m\n')

'''
Como eu tentei fazer
for n in range(2, num):
    x = num % n
    print(n)
    if x == 0:
        c = 'não é primo'
    else:
        c = 'é primo'

print('Esse número {0}'.format(c))
'''