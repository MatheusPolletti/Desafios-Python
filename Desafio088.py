# Meu

'''from random import randint
from time import sleep

print('-'*17)
print('Jogo da Mega-Sena')
print('-'*17)

contador = n = 0

numeros = list()

jogos = int(input('Quantos jogos você quer jogar? '))

print(f'\nSorteando {jogos} jogos!!!\n')

while contador < jogos:
    for i in range(6):
        n = randint(1, 60)
        while True:
            if n in numeros:
                n = randint(1, 60)
            else:
                break
        numeros.append(n)
    sleep(1)
    numeros.sort()
    print(f'JOGO {contador + 1} : {numeros}\n')
    numeros.clear()
    contador += 1'''

# Guanabará

from random import randint
from time import sleep

total = contador = 0

lista = list()
jogos = list()

quantia = int(input('Quantos jogos você quer? '))

while total < quantia:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'Sortando {quantia} jogos')

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

