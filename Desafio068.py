'''
print('\033[34m')
print('-'*24)
print('\033[36m', end='')
print('Vamos jogar Par ou Ímpar', end='')
print('\033[m')
print('\033[34m', end='')
print('-'*24, '\033[m\n')

from random import randint

jogadas = 0

while True:
    jogadorValor = int(input('Diga um valor: '))
    jogadorJogada  = str(input('Digite se você quer par ou impar [p/i]: ')).strip().lower()[0]
    maquinaValor = randint(1, 5)
    jogadas += 1
    resultado = maquinaValor + jogadorValor
    if jogadorValor > 5 or jogadorValor < 0:
        print('\033[31mO sistema só reconhece valores de 0 até 5\033[m')
        jogadas -= 1
    elif jogadorJogada in 'p':
        if resultado % 2 == 0:
            print(f'O resultado é {resultado}, você venceu!')
        elif resultado % 2 != 0:
            print(f'O resultado é {resultado}, você perdeu!')
            break
    elif jogadorJogada in 'i':
        if resultado % 2 != 0:
            print(f'O resultado é {resultado}, você venceu!')
        elif resultado % 2 == 0:
            print(f'O resultado é {resultado}, você perdeu')
            break
    else:
        print(f'A jogada não é valida, {jogadorJogada} não é reconhecido pelo nosso sistema')
        jogadas -= 1

print(f'Fim do jogo, você perdeu após {jogadas} jogadas.')
'''

# Guanabará

from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Com total de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você venceu! ')
            v += 1
        else:
            print('Você perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! ')
            v += 1
        else:
            print('Você perdeu')
            break

print(f'Você venceu {v} vezes')