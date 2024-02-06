# Meu

'''from time import sleep
# Sleep não funciona dentro do for com end = '' ?

def linha():
    print('='*30)


def contador():
    linha()
    print('Contagem de 1 até 10 de 1 em 1: ')
    sleep(1)
    for c in range (1, 11):
        print(f'\033[35m{c}\033[m', end = ' ')
    print()
    linha()
    print('Contagem de 10 até 0 de 2 em 2: ')
    for c in range (10, -1, -2):
        print(f'\033[35m{c}\033[m', end = ' ')
    print('\nAgora é sua vez de fazer uma contagem!')
    i = int(input('\nDigite o valor de ínicio da contagem: '))
    f = int(input('Digite o valor do fim da contagem: '))
    p = int(input('Digite o valor de passo da contagem: '))
    if p == 0:
        print(f'\033[31mNós faremos uma contagem de {i} até {f} com passo de 1, com o passo {p} é impossível!\033[m')
        p = 1
    if f > i:
        for usuario in range(i, f + 1, p):
            print(f'\033[34m{usuario} \033[m', end = '')
    elif f < i:
        if p > 0:
            for usuario in range(i, f - 1, -p):
                print(f'\033[34m{usuario} \033[m', end = '')
        if p <0:
            for usuario in range(i, f - 1, p):
                print(f'\033[34m{usuario} \033[m', end = '')


contador()'''

# Guanabará

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            #sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            #sleep(0.5)
            cont -= p
    print('Fim')


contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem: ')

ini = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)