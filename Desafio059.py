from time import sleep

print('\033[34m')
print('-'*25)
print('Menu Matemático Polletti')
print('-' * 25, '\033[m\n\n')

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

comando = 0

while comando != 5:
    print('\033[36m')
    print('='*32)
    print('Escolha o comando que você quer:\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do Programa')
    comando = int(input('Qual sua opção? '))
    print('='*32)
    print('\033[m')
    if comando == 1:
        r = v1 + v2
        print('{0} + {1} = {2}'.format(v1, v2, r))
    elif comando == 2:
        r = v1 * v2
        print('{0} * {1} = {2}'.format(v1, v2, r))
    elif comando == 3:
        if v1 > v2:
            print('O primeiro valor {0} é maior que o segundo valor {1}'.format(v1, v2))
        elif v2 > v1:
            print('O segundo valor {0} é maior que o primeiro valor {1}'.format(v2, v1))
        else:
            print('Os dois valores são iguais, {0} e {1}'.format(v1, v2))
    elif comando == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif comando == 5:
        print('\033[31mVocê está saindo do programa\033[m\n')
    elif comando > 5 or comando < 1:
        print('\033[31mComando inválido\033[m')
    sleep(2)

print('\033[31mVocê saiu do Programa!\033[m\n')

'''
Como guanabará fez(Mais ou menos)

from time import sleep

print('\033[34m')
print('-'*25)
print('Menu Matemático Polletti')
print('-' * 25, '\033[m\n\n')

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

comando = 0

while comando != 5:
    print('\033[36m')
    print('='*32)
    print('Escolha o comando que você quer:\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do Programa')
    comando = int(input('Qual sua opção? '))
    print('='*32)
    print('\033[m')
    if comando == 1:
        r = v1 + v2
        print('{0} + {1} = {2}'.format(v1, v2, r))
    elif comando == 2:
        r = v1 * v2
        print('{0} * {1} = {2}'.format(v1, v2, r))
    elif comando == 3:
        if v1 > v2:
            print('O primeiro valor {0} é maior que o segundo valor {1}'.format(v1, v2))
        elif v2 > v1:
            print('O segundo valor {0} é maior que o primeiro valor {1}'.format(v2, v1))
        elif v1 == v2:
            print('Os dois valores são iguais, {0} e {1}'.format(v1, v2))
    elif comando == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif comando == 5:
        print('\033[31mVocê está saindo do programa\033[m\n')
    else comando > 5 or comando < 1:
        print('Comando inválido')
    sleep(2)

print('\033[31mVocê saiu do Programa!\033[m\n')
'''