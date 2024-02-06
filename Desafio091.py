# Meu

'''from random import randint
from time import sleep

valores = dict()
c = 1

print('Os valores sorteados são: ')

for j in range(1, 5):
    valores[f'jogador{j}'] =  randint(1, 6)
    sleep(1)
    print(f'O jogador{j} tirou {valores[f"jogador{j}"]}')

# sorted(valores) Organiza pelo nome
    
print('\nRanking dos Jogadores: ')

for i in sorted(valores, key = valores.get, reverse=True): # Key é do sorted que define o que vai pegar pra organizar, 
    print(f'{c}° Lugar: {i} com {valores[i]}')
    c += 1'''

# Guanabará

from random import randint
from time import sleep
from operator import itemgetter # Para pegar o valor do randint

jogo = {'jogadorUm': randint(1,6),
        'jogadorDois': randint(1,6),
        'jogadorTrês': randint(1,6),
        'jogadorQuatro': randint(1,6),}

ranking = list()

print('Valores sorteados:')
for chave, valor in jogo.items():
    sleep(1)
    print(f'A {chave} tirou {valor} no dado')

ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True) # key = itemgetter(1) seleciona o randint

for indice, valor in enumerate(ranking):
    print(f'\nO {indice + 1}° é : {valor[0]} com {valor[1]} pontos')