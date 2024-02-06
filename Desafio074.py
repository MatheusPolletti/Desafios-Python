# Meu

'''
from random import randint

a = (randint(1, 10))
b = (randint(1, 10))
c = (randint(1, 10))
d = (randint(1, 10))
e = (randint(1, 10))
 
junto = a, b, c, d, e

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
organizado = sorted(tupla)

print(f'Os valores sorteados foram: {tupla[0]}, {tupla[1]}, {tupla[2]}, {tupla[3]}, {tupla[4]}')
print(f'O menor valor é: {organizado[0]}\nO maior valor é: {organizado[-1]}')
'''

# Guanabará

from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Eu sorteei os valores {n}')

print(f'O maior sorteado foi {max(n)}\nO menor sorteado foi {min(n)}')