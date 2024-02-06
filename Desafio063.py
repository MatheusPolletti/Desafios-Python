# Sequência de Fibonacci
'''
print('\033[35m')
print('-'*22,end='')
print('\033[m', end='')
print('\033[34m')
print('Sequência de Fibonacci',end='')
print('\033[m',end='')
print('\033[35m')
print('-'*22)
print('\033[m')

fim = int(input('Quantos termos você quer para sua sequência? '))

penultimo = cont = termo = 0
ultimo = 1
print('Fibonaci = ',end='')

while cont != fim:
    print('{0}'.format(termo), end='')
    print(' --> ' if cont != fim - 1 else ' --> Fim', end='')
    if cont == 1:
        termo = 1
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    cont += 1
'''

print('\033[35m')
print('-'*22,end='')
print('\033[m', end='')
print('\033[34m')
print('Sequência de Fibonacci',end='')
print('\033[m',end='')
print('\033[35m')
print('-'*22)
print('\033[m')

n = int(input('Quantos termos você quer para sua sequência? '))

t1 = 0
t2 = 1
cont = 3

print('{0} --> {1}'.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' --> {0}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
    
print(' --> Fim')