'''
from random import randint
from time import sleep

print('\033[34m----- Jokenpô -----\033[m\n')
print('Opções:
1 - Pedra
2 - Papel
3 - Tesoura\n')
jogador = int(input('Digite qual opção você quer para jogar: ' ))

maquina = randint(1, 3)
# items = 'Pedra', 'Papel', 'Tesoura'
# .format(items[maquina])

print('\n\033[36mJo\033[m')
sleep(1)
print('\033[33mken\033[m')
sleep(1)
print('\033[34mpô\033[m')
sleep(1)

if jogador == 1 and maquina == 3:
    print('\nVocê jogou Pedra e a máquina jogou Tesoura.')
    print('\n\033[32mVocê venceu!!!\033[m')
elif jogador == 1 and maquina == 2:
    print('\nVocê jogou Pedra e a máquina jogou Papel.')
    print('\033[31mVocê Perdeu\033[m')
elif jogador == 2 and maquina == 1:
    print('\nVocê jogou Papel e a máquina jogou Pedra.')
    print('\n\033[32mVocê venceu!!!\033[m')
elif jogador == 2 and maquina == 3:
    print('\nVocê jogou Papel e a máquina jogou Tesoura.')
    print('\033[31m\nVocê Perdeu\033[m')
elif jogador == 3 and maquina == 2:
    print('\nVocê jogou Tesoura e a máquina jogou Papel.')
    print('\n\033[32mVocê venceu!!!\033[m')
elif jogador == 3 and maquina == 1:
    print('\nVocê jogou Tesoura e a máquina jogou Pedra.')
    print('\033[31m\nVocê Perdeu\033[m')
elif jogador == maquina:
    print('\n\033[34;41mAmbos escolheram o mesmo jogo! Escolha novamente.\033[m')
else:
    print('\n\033[30mA sua jogada não é válida\033[m')
sleep(10)
'''

from random import choices
from time import sleep

maquinaLista = ['papel', 'pedra', 'tesoura']
vitoria = 0

while True:
    print(f'{"\033[34m----- Jokenpô -----\033[m":^50}\n')
    jogador = str(input('Qual é a sua jogada? Pedra, Papel ou Tesoura? ')).strip().lower()

    maquina = str(choices(maquinaLista, weights=None, k = 1))
    maquina = maquina[2:-2]

    print('\n\033[36mJo\033[m')
    sleep(1)
    print('\033[33mken\033[m')
    sleep(1)
    print('\033[34mpô\033[m')
    sleep(1)

    if maquina == jogador:
        print(f'\033[33m\nO jogo deu empate\nA máquina jogou {maquina} e você jogou {jogador}\n\033[m')
    elif jogador == 'pedra' and maquina == 'papel':
        print(f'\033[31m\nVocê Perdeu\nA máquina jogou {maquina} e você jogou {jogador}.\033[m')
        break
    elif jogador == 'pedra' and maquina == 'tesoura':
        print(f'\n\033[32mVocê venceu!!!\nA máquina jogou {maquina} e você jogou {jogador}.\n\033[m')
        vitoria += 1
    elif jogador == 'papel' and maquina == 'pedra':
        print(f'\n\033[32mVocê venceu!!!\nA máquina jogou {maquina} e você jogou {jogador}.\n\033[m')
        vitoria += 1
    elif jogador == 'papel' and maquina == 'tesoura':
        print(f'\033[31m\nVocê Perdeu\nA máquina jogou {maquina} e você jogou {jogador}.\033[m')
        break
    elif jogador == 'tesoura' and maquina == 'papel':
        print(f'\n\033[32mVocê venceu!!!\nA máquina jogou {maquina} e você jogou {jogador}.\n\033[m')
        vitoria += 1
    elif jogador == 'tesoura' and maquina == 'pedra':
        print(f'\033[31m\nVocê Perdeu\nA máquina jogou {maquina} e você jogou {jogador}.\033[m')
        break
    else:
        print(f'\n\033[31mA sua jogada não é válida.\nNão reconhecemos {jogador}.\n\033[m')

print(f'\n\033[32mVocê venceu {vitoria} rodadas\033[m')

sleep(10)
