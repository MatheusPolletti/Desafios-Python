# Meu

'''from random import randint
from time import sleep

def sorteia():
    print('\033[35mSorteando 5 valores da lista:\033[m')
    sleep(1)
    for i in range(5):
        num = randint(1, 100)
        numeros.append(num)
    print('Os valores sorteados são: ', end='')
    for n in numeros:
        print(f'{n} ', end='')
    somaPar(numeros)


def somaPar(numeros):
    soma = 0
    print('\n\nSomando os valores para que estão em: ', end='')
    for i in range(len(numeros)):
        print(f'{numeros[i]} ', end='')
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print('...')
    sleep(1)
    print(f'\nApós a soma temos: {soma}')

      
numeros = list()
    
sorteia()'''

# Guanabará

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista...', end='')
    for contador in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('Pronto')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de: {lista}, temos {soma}')


numeros = list()

sorteia(numeros)
somaPar(numeros)

#print(numeros)
#sum - somar todos os valores
