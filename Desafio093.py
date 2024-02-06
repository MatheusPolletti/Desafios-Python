# Meu

'''jogador = dict()

gols = list()

total = 0

jogador['Nome'] = str(input('Digite seu nome: ')).strip().title()

jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for cont in range(jogos):
    gol = int(input(f'Quantos gols ele fez na partida {cont + 1}? '))
    jogador['Gols'] = gols
    gols.append(gol)
    total += gol

jogador['Total'] = total

print('='*56)
print(jogador)
print('='*92)
print(f'O nome do jogador é {jogador["Nome"]} e ele fez {jogador['Gols']} gols, sendo um total de {jogador["Total"]} gols.')
print('='*92)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas: ')
for c, g in enumerate(gols):
    print(f'{'--> ':>5}Na partida {c + 1}, ele fez {g} gols')
print(f'Sendo um total de {jogador['Total']} gols.')'''

# Guanabará

# sum() soma de algo dentro

jogador = dict()

partidas = list()

jogador['Nome'] = str(input('Nome do jogador: ')).strip()

tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(tot):
    partidas.append(int(input(f'Quantos gols ele fez na {c + 1}° partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print(jogador)

for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')

for indice, valor in enumerate(jogador['Gols']):
    print(f'  ==> Na partida {indice + 1}, ele fez {valor} gols')
print(f'Foi um total de {jogador["Total"]} gols')