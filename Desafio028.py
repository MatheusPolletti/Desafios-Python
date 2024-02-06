from random import randint, randrange
from time import sleep

print('Jogo da Adivinhação')

numUsuario = int(input('Digite um número entre 0 e 5: '))
sleep(2) # Faz ter um delay de 2 segundos

# Como eu fiz
#numComputador = randrange(1, 6, 1)

# O guanabará fez usando o comando:
numComputador = randint(0, 5)

if numUsuario == numComputador:
    print('Parabéns!! Você acertou!!')
else:
    print('Infelizmente você errou! O número escolhido pelo computador foi: {0}'.format(numComputador))