'''
Como eu fiz: 
from time import sleep

num = int(input('Digite um número para ver seu fatorial: '))
fatorial = 1

print('\nCalculando o fatorial de {0}! ...\n'.format(num))
sleep(2)

while num != 0:
    print('{0} * '.format(num), end='')
    fatorial *= num
    num -= 1

print(' = {0}\n'.format(fatorial))

num = int(input('Digite um número para ver seu fatorial: '))
fatorial = 1

for c in range(num, 1, -1):
    fatorial *= num
    num -= 1


print('O fatorial dele é: {}'.format(fatorial))
'''

'''
Como o guanabará fez:

from math import factorial
n = int(input('Digite o número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {0} é {1}'.format(n, f))


n = int(input('Digite o número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando o fatorial de {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('O fatorial de {0} é {1}'.format(n, f))
'''

# Meu código 2 com for

num = int(input('Digite um número para ver seu fatorial: '))
f = 1

for c in range (num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c != 1 else ' = ', end='')
    f *= c

print(f)
print('\nO fatorial de {0}! é {1}'.format(num, f))