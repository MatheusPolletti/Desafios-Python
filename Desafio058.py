from time import sleep
from random import randint

jogador = int(input('Digite um número entre 0 e 10 para jogar: '))
maquina = randint(1, 10)
tentivas = 1

sleep(1)

while jogador != maquina:
    if jogador > maquina:   
        sleep(1)
        jogador = int(input('Menos...Tente mais uma vez: '))
    else:
        sleep(1)
        jogador = int(input('Mais...Tente mais uma vez: '))
    tentivas += 1

print('Parabéns!! A máquina jogou {0} e você jogou {1}. Você acertou em {2} tentativas'.format(maquina, jogador, tentivas))

sleep(10)

# Guanabará fez assim:
'''
from random import randint

computador = randint(0, 10)
print(computador)
print('Adivinhe o número pensado pelo seu computador')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite um número entre 0 e 10 para jogar: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')    

print('\nAcertou com {0} tentativas'.format(palpites))
'''